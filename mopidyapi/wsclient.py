
# std lib
import logging
import asyncio
import json
from threading import Thread
from collections import namedtuple
from time import sleep
from functools import partial

# deps
import websockets
from websockets.exceptions import ConnectionClosed

# app imports
from .parsedata import deserialize_mopidy


class MopidyWSClient:
    """ Mopidy Websocket API Client """
    def __init__(self, host='localhost', port=6680, logger=None,
                 reconnect_time=0.5, flask_object=None):
        # typical, boring constructor stuff
        self.logger = logger if logger else logging.getLogger(__name__)
        self.ws_url = f'ws://{host}:{port}/mopidy/ws'
        self.reconnect_time = reconnect_time
        self._event_callbacks = {}

        if flask_object is not None:
            # get non-proxy flask object, to pass app context into thread
            logger.debug("Using Flask object inside Mopidy listener.")
            self.flask_object = flask_object._get_current_object()
        else:
            # avoid AttributeError when accessing later
            self.flask_object = None

        # start websocket listener in a separate thread
        self.logger.info("Creating Mopidy Websocket connection...")
        self.wsthread = Thread(target=self._websocket_runner,
                               args=(asyncio.new_event_loop(),),
                               name="WSListener", daemon=True)
        self.wsthread.start()

    def _websocket_runner(self, loop):
        """ Method to run in websocket handler thread.
        Receives websocket messages using the library 'websockets'.
        Since 'websockets' uses asyncio, it needs an event loop.
        """
        async def packethandler():
            try:
                async with websockets.connect(self.ws_url) as ws:
                    while True:
                        msg = await ws.recv()
                        self._on_message(msg)
            except (ConnectionError, ConnectionClosed, OSError) as e:
                # reconnect on connection errors
                self.logger.warning(
                    f"Mopidy connection error (reconnecting): {e}")
                sleep(self.reconnect_time)

        while True:
            # run listener (forever)
            loop.run_until_complete(packethandler())

    def _on_message(self, msgstr: str):
        """ Method to be called on every arriving websocket message. """
        msg = json.loads(msgstr)
        if 'event' in msg:
            self._route_event(msg)
        else:
            self.logger.debug(f"Not routing packet: {msgstr}")

    def _route_event(self, event: dict):
        """ Pass event data to the functions registered
        in the _event_callbacks dict.
        """
        evname = event['event']
        self.logger.debug(f"Routing event: {evname}")
        callbacks = self._event_callbacks.get(evname, [])
        for cb in callbacks:
            # deserialize into neat named tuples
            nt = namedtuple(evname, event)
            neatdata = nt(**{k: deserialize_mopidy(event[k]) for k in event})

            # call the callback
            if self.flask_object is not None:
                # allow event handlers to use flask obj
                # despite running in separate thread
                with self.flask_object.app_context():
                    cb(neatdata)
            else:
                # regular callback (all cases but flask apps)
                cb(neatdata)

    def on_event(self, event: str):
        """ Function decorator, to listen for events.
        Decorated function is added to callbacks dict,
        to be called when specified event arrives.
        """
        return partial(self.add_callback, event)

    def add_callback(self, event, f):
        """ Add function to callback dict, to be called
            when specific event arrives.
            Event callbacks dict is of type Set - to avoid
            the same function being entered multiple times.
            TODO: check for invalid/unsupported event names
        """
        cbs = self._event_callbacks
        if event in cbs:
            cbs[event].add(f)
        else:
            cbs[event] = set([f])
        return f

    def del_callback(self, event=None, f=None):
        """ Remove event / function.
        1. Remove complete event, if function is None.
        2. Remove function from all events, if event is None.
        3. Remove function from event.
        """
        cbs = self._event_callbacks
        if event and f is None:
            # Remove entire event
            del cbs[event]
        elif event is None and f:
            # Remove given method from all events
            for fs in cbs.values():
                if f in fs:
                    fs.remove(f)
        elif event and f:
            # Remove given method from given event
            cbs[event].remove(f)
