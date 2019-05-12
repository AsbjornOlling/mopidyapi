
# std lib
import logging

# deps
from requests import post

# app
from .wsclient import MopidyWSClient
from .mopidy_types import deserialize_mopidy
from .controllers import (
    history,
    library,
    mixer,
    playback,
    playlists,
    tracklist
)

# exceptions
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError


class MopidyAPI:
    """ Mopidy API Client.
    Capable of doing Mopidy RPC calls using http,
    and starts an instance of MopidyWSClient to listen
    for events.
    """
    def __init__(self, host='localhost', port=6680,
                 use_websocket=True, logger=None):
        # boring constructor stuff
        self.logger = logger if logger else logging.getLogger(__name__)

        # get rpc addresses
        self.http_url = f'http://{host}:{port}/mopidy/rpc'
        self.ws_url = f'ws://{host}:{port}/mopidy/ws'

        # load controllers (which encapsulate rpc methods)
        self.history = history.HistoryController(self)
        self.library = library.LibraryController(self)
        self.mixer = mixer.MixerController(self)
        self.playback = playback.PlaybackController(self)
        self.playlists = playlists.PlaylistsController(self)
        self.tracklist = tracklist.TracklistController(self)

        if use_websocket:
            # start websocket connection, and borrow a decorator
            self.wsclient = MopidyWSClient(ws_url=self.ws_url,
                                           logger=self.logger)
            self.on_event = self.wsclient.on_event

    def rpc_call(self, command: str, *args, **kwargs):
        """ Call the Mopidy HTTP JSON RPC API, (by sending
        a HTTP POST with a specific JSON object).
        Response JSON is deserialized into namedtuples
        before returning.
        """
        helpstr = ("Check that is set right "
                   "and that Mopidy is running and accessible.")

        # assemble rpc command
        rpcjson = {'jsonrpc': '2.0',
                   'id': 0,
                   'method': command}
        if kwargs:
            rpcjson['params'] = kwargs
        elif args:
            rpcjson['params'] = list(args)

        try:
            self.logger.debug(f"Sending Mopidy RPC: {rpcjson}")

            # do the HTTP POST to mopidy
            r = post(self.http_url,
                     json=rpcjson).json()

            # assert: no errors :^)
            assert 'error' not in r, r.get('error', None)

            # dict -> namedtuples and return
            return deserialize_mopidy(r['result'])

        # a whole bunch of error handling
        except AssertionError as ex:
            err = f"Mopidy error: {ex['data']['message']}"
            self.logger.error(err)
        except ConnectionError as ex:
            err = f"Mopidy connection error: {ex} {helpstr}"
            self.logger.error(err)
        except JSONDecodeError:
            err = f"Got weird response from Mopidy. {helpstr}"
            self.logger.error(err)
