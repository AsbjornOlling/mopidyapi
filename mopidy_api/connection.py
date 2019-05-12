""" Mopidy connection handling

This module contains functions to conenct and
interact with the Mopidy JSON RPC API,
as well as the Mopidy Websocket API for events.
"""


# deps
from requests import post
from loguru import logger
from flask import current_app as app

# exceptions
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError


def mopidy_post(command: str, *args, **kwargs):
    """ Call the Mopidy HTTP JSON RPC API, by sending
    a HTTP POST with a specific JSON object.
    """
    helpstr = ("Check that MOPIDY_RPC_URL is set right "
               "and that Mopidy is running and accessible.")

    # assemble rpc command
    rpccmd = {'jsonrpc': '2.0',
              'id': 1,
              'method': command}
    if kwargs:
        rpccmd['params'] = kwargs
    elif args:
        rpccmd['params'] = list(args)

    try:
        logger.debug(f"Sending Mopidy RPC: {rpccmd}")

        # do the HTTP POST to mopidy
        r = post(app.config['MOPIDY_RPC_URL'],
                 json=rpccmd).json()

        # assert: no errors :^)
        assert 'error' not in r, r.get('error', None)
        return r['result']

    # a whole bunch of error handling
    except AssertionError as ex:
        err = f"Mopidy error: {ex}"
        logger.error(err)
        # abort(500, err)
    except ConnectionError as ex:
        err = f"Mopidy connection error: {ex} {helpstr}"
        logger.error(err)
        # abort(500, err)
    except JSONDecodeError:
        err = f"Got weird response from Mopidy. {helpstr}"
        logger.error(err)
        # abort(500, err)
