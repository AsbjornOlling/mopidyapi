""" Mopidy API Types

This module contains the named tuple types,
representing the json objects returned by the Mopidy API.
and a neat-o recursive funciton to turn mopidy format into
the named tuples.
"""

# std lib
from collections import namedtuple
from typing import Dict, List

from loguru import logger


@logger.catch()
def deserialize_mopidy(data):
    """ Recursively turn the structure of mopidy dicts
    into an identical structure of namedtuples.
    """
    # first detect type of data
    if isinstance(data, Dict) and '__model__' in data:
        # found object dict. get name of object and fields
        model = data['__model__']
        fields = [k for k in data.keys() if k != '__model__']

        # define namedtuple based on keys in dict
        nt = namedtuple(model, fields)

        # recurse on dict
        recd = {k: deserialize_mopidy(data[k]) for k in fields}

        # make tuple from recused dict
        return nt(**recd)

    elif isinstance(data, List):
        # recurse on list
        return list(map(deserialize_mopidy, data))

    elif isinstance(data, str) or isinstance(data, int) or data is None:
        # strings, ints, and None should be the only primitives here
        return data
    else:
        raise ValueError(f"Uncaught type: {type(data)}")
