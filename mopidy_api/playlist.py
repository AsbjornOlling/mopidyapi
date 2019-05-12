""" playlist.py
Functions to report back about the state of mopidy
"""
# std lib
from typing import List

# deps
from loguru import logger

# app imports
from .connection import mopidy_post
from .mopidy_types import deserialize_mopidy, TlTrack


def get_playlist() -> List[TlTrack]:
    """ Get playlist from Mopidy.
    Results in a list of TlTrack tuples.
    """
    logger.info("Getting playlist from mopidy...")
    mplist = mopidy_post('core.tracklist.get_tl_tracks')

    # parse into namedtuple types (tuples defined in .types)
    plist: List[TlTrack] = deserialize_mopidy(mplist)
    return plist


def get_playlist_uris() -> List[str]:
    """ Return list of uris in current Mopidy playlist. """
    return [t.track.uri for t in get_playlist()]


def add_uri(uri: str):
    """ Add track to Mopidy's currently
    playing tracklist by URI.
    """
    logger.info(f"Adding {uri} to Mopidy playlist.")
    result = mopidy_post('core.tracklist.add', uri=uri)
    logger.debug(f"Got: {result}")
