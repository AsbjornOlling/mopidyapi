""" Mopidy API Types

This module contains the named tuple types,
representing the json objects returned by the Mopidy API.
and a neat-o recursive funciton to turn mopidy format into
the named tuples.
"""

# std lib
from collections import namedtuple


def deserialize_mopidy(data):
    """ Recursively turn the structure of mopidy dicts
    into an identical structure of namedtuples.
    """
    # first detect type of data
    if isinstance(data, dict) and '__model__' in data:
        # define namedtuple based on keys in dict
        fields = [k for k in data if k != '__model__']
        nt = namedtuple(data['__model__'], fields)

        # recurse on dict
        recd = {k: deserialize_mopidy(data[k]) for k in fields}

        # make namedtuple from resulting dict
        return nt(**recd)

    elif isinstance(data, list):
        # recurse on list
        return [deserialize_mopidy(d) for d in data]

    elif isinstance(data, dict):
        # recurse on dict (dict w/o __model__ field)
        return {k: deserialize_mopidy(v) for k, v in data.items()}

    elif isinstance(data, (str, int)) or data is None:
        return data

    else:
        raise ValueError(f"Uncaught type: {type(data)}")


def serialize_mopidy(data):
    """ Recursively turn a MopidyAPI namedtuple
    into Mopidy-understandable JSON. """
    if isinstance(data, tuple):
        # get dict from tuple
        ddict = data._asdict()

        # recurse on dict
        mopdict = {k: serialize_mopidy(ddict[k]) for k in ddict}

        # write type in dict and return
        mopdict['__model__'] = type(data).__name__
        return mopdict

    if isinstance(data, dict):
        # recurse on dict
        return {k: serialize_mopidy(data[k]) for k in data}

    elif isinstance(data, list):
        # recurse on list
        return [serialize_mopidy(x) for x in data]

    elif isinstance(data, str) or isinstance(data, int) or data is None:
        # strings, ints, and None should be the only primitives here
        return data

    else:
        raise ValueError(f"Uncaught type: {type(data)}")
