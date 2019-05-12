"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class HistoryController:
    def __init__(self, client):
        self.client = client

    def get_length(self, *args, **kwargs):
        """ Get the number of tracks in the history.
    
    :returns: the history length
    :rtype: int """
        return self.client.rpc_call('core.history.get_length', *args, **kwargs)

    def get_history(self, *args, **kwargs):
        """ Get the track history.
    
    The timestamps are milliseconds since epoch.
    
    :returns: the track history
    :rtype: list of (timestamp, :class:`mopidy.models.Ref`) tuples """
        return self.client.rpc_call('core.history.get_history', *args, **kwargs)
