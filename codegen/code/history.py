"""
This file was generated programatically,
based on JSON describing all available methods.
"""

from .connection import 


def get_length():
    """ Get the number of tracks in the history.
    
    :returns: the history length
    :rtype: int """


def get_history():
    """ Get the track history.
    
    The timestamps are milliseconds since epoch.
    
    :returns: the track history
    :rtype: list of (timestamp, :class:`mopidy.models.Ref`) tuples """

