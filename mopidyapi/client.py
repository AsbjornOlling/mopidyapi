
# std lib
import logging

# deps
from requests import post

# app
from .parsedata import deserialize_mopidy, serialize_mopidy
from .wsclient import MopidyWSClient
from .exceptions import MopidyError
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
    def __init__(self, host='localhost', port=6680, use_websocket=True,
                 logger=None, flask_object=None):
        # boring constructor stuff
        self.logger = (logger if logger is not None
                       else logging.getLogger(__name__))
        self.logger.debug("Creating MopidyAPI client object...")

        # get rpc addresses
        self.http_url = f'http://{host}:{port}/mopidy/rpc'

        # load controllers (which encapsulate rpc methods)
        self.history = history.HistoryController(self)
        self.library = library.LibraryController(self)
        self.mixer = mixer.MixerController(self)
        self.playback = playback.PlaybackController(self)
        self.playlists = playlists.PlaylistsController(self)
        self.tracklist = tracklist.TracklistController(self)

        if use_websocket:
            # start websocket connection, and borrow a decorator
            self.wsclient = MopidyWSClient(host=host, port=port,
                                           logger=self.logger,
                                           flask_object=flask_object)
            self.on_event = self.wsclient.on_event
            self.add_callback = self.wsclient.add_callback
            self.del_callback = self.wsclient.del_callback

    def rpc_call(self, command: str, *args, **kwargs):
        """ Call the Mopidy HTTP JSON RPC API, (by sending
        a HTTP POST with a specific JSON object).
        Response JSON is deserialized into namedtuples
        before returning.
        """
        self.logger.debug(f"Calling Mopidy method: {command}")

        # assemble rpc command
        rpcjson = {'jsonrpc': '2.0',
                   'id': 0,
                   'method': command}
        if kwargs:
            rpcjson['params'] = serialize_mopidy(kwargs)
        elif args:
            rpcjson['params'] = serialize_mopidy(list(args))

        try:
            # do the HTTP POST to mopidy
            r = post(self.http_url,
                     json=rpcjson).json()

            # assert: no errors :^)
            # fail if error, pass error message to MopidyError exception
            errmsg = r.get('error', {}).get('data', {}).get('message')
            assert 'error' not in r, errmsg

            # dict -> namedtuples and return
            return deserialize_mopidy(r['result'])

        # a whole bunch of error handling
        except AssertionError as ex:
            err = f"Mopidy error: {ex}"
            self.logger.error(err)
            raise MopidyError(str(ex))
        except ConnectionError as ex:
            err = f"Mopidy connection error: {ex} "
            self.logger.error(err)
            raise ex
        except JSONDecodeError as ex:
            err = f"Could not decode json from Mopidy: {str(ex)}"
            self.logger.error(err)
            raise ConnectionError(ex)
