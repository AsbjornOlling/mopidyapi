
# std lib
import logging
import asyncio
import json
from threading import Thread
from collections import namedtuple

# deps
import websockets

# app imports
from .mopidy_types import deserialize_mopidy


class MopidyWSClient:
    """ Mopidy Websocket API Client """
    def __init__(self, ws_url='localhost:6680', logger=None):
        # typical, boring constructor stuff
        self.logger = logger if logger else logging.getLogger(__name__)
        self.ws_url = ws_url
        self._event_callbacks = {}

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
            async with websockets.connect(self.ws_url) as ws:
                while True:
                    msg = await ws.recv()
                    self._on_message(msg)

        # run listener forever, reconnect on exceptions
        while True:
            try:
                loop.run_until_complete(packethandler())
            except Exception as e:
                raise e
                self.logger.warning(
                    f"Websocket connection error (reconnecting): {e}")

    def _on_message(self, msgstr: str):
        """ Method to be called on every arriving websocket message. """
        msg = json.loads(msgstr)
        if 'event' in msg.keys():
            self._route_event(msg)
        else:
            self.logger.debug(f"Received unknown type packet: {msg}")

    def _route_event(self, event: dict):
        """ Pass event data to the functions registered
        in the _event_callbacks dict.
        """
        evname = event['event']
        self.logger.debug(f"Routing event: {evname}")
        callbacks = self._event_callbacks.get(evname, [])
        for cb in callbacks:
            # deserialize into neat named tuples
            nt = namedtuple(evname, event.keys())
            neatdata = nt(**{k: deserialize_mopidy(event[k]) for k in event})
            # call the callback
            cb(neatdata)

    def on_event(self, event: str):
        """ Function decorator, to listen for events.
        Decorated function is added to callbacks dict,
        to be called when specified event arrives.
        TODO: check for invalid/unsupported event names
        """
        cbs = self._event_callbacks

        def decorator(f):
            """ Appends function to the event callbacks dict. """
            if event in cbs.keys():
                cbs[event].add(f)
            else:
                cbs[event] = set([f])
            return f

        return decorator
