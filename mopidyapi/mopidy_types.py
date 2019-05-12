""" Mopidy API Types

This module contains the named tuple types,
representing the json objects returned by the Mopidy API.
and a neat-o recursive funciton to turn mopidy format into
the named tuples.
"""

# std lib
from collections import namedtuple
from typing import Dict, List

# mopidy json object types
Track = namedtuple(
    'Track',
    ['uri',
     'name',
     'album',
     'artists',
     'length'])
Album = namedtuple(
    'Album',
    ['uri',
     'name'])
Artist = namedtuple(
    'Artist',
    ['uri',
     'name'])
SearchResult = namedtuple(
    'SearchResult',
    ['uri',
     'artists',  # list of tracks that match artist
     'tracks',   # list of tracks that match tracks
     'albums'])  # ...
TlTrack = namedtuple(
    'TlTrack',
    ['tlid',  # (playlist position, track)
     'track'])

# registry over all mopidy types
MopidyTypes = {
    'SearchResult': SearchResult,
    'TlTrack':      TlTrack,
    'Track':        Track,
    'Album':        Album,
    'Artist':       Artist
}


def deserialize_mopidy(data):
    """ Recursively turn the structure of mopidy dicts
    into an identical structure of namedtuples.
    """
    # first detect type of data
    if isinstance(data, Dict) and '__model__' in data:
        model = data['__model__']

        # get namedtuple constructor from MopidyTypes dict
        assert model in MopidyTypes, f"Unknown mopidy type: {data}"
        nt = MopidyTypes[model]

        # recurse on dict, keeping only fields defined in the named tuples
        recd = {k: deserialize_mopidy(data.get(k, None)) for k in nt._fields}

        # make tuple
        return nt(**recd)

    elif isinstance(data, List):
        # recurse on list
        return list(map(deserialize_mopidy, data))

    elif isinstance(data, str) or isinstance(data, int) or data is None:
        # strings, ints, and None should be the only primitives here
        return data
    else:
        raise ValueError(f"Uncaught type: {type(data)}")
