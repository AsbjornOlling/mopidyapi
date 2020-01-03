"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class PlaybackController:
    def __init__(self, client):
        self.client = client

    def get_current_tl_track(self, *args, **kwargs):
        """ Get the currently playing or selected track.
    
    Returns a :class:`mopidy.models.TlTrack` or :class:`None`. """
        return self.client.rpc_call('core.playback.get_current_tl_track', *args, **kwargs)

    def get_current_tlid(self, *args, **kwargs):
        """ Get the currently playing or selected TLID.
    
    Extracted from :meth:`get_current_tl_track` for convenience.
    
    Returns a :class:`int` or :class:`None`.
    
    .. versionadded:: 1.1 """
        return self.client.rpc_call('core.playback.get_current_tlid', *args, **kwargs)

    def get_current_track(self, *args, **kwargs):
        """ Get the currently playing or selected track.
    
    Extracted from :meth:`get_current_tl_track` for convenience.
    
    Returns a :class:`mopidy.models.Track` or :class:`None`. """
        return self.client.rpc_call('core.playback.get_current_track', *args, **kwargs)

    def get_state(self, *args, **kwargs):
        """ Get The playback state. """
        return self.client.rpc_call('core.playback.get_state', *args, **kwargs)

    def get_stream_title(self, *args, **kwargs):
        """ Get the current stream title or :class:`None`. """
        return self.client.rpc_call('core.playback.get_stream_title', *args, **kwargs)

    def get_time_position(self, *args, **kwargs):
        """ Get time position in milliseconds. """
        return self.client.rpc_call('core.playback.get_time_position', *args, **kwargs)

    def next(self, *args, **kwargs):
        """ Change to the next track.
    
    The current playback state will be kept. If it was playing, playing
    will continue. If it was paused, it will still be paused, etc. """
        return self.client.rpc_call('core.playback.next', *args, **kwargs)

    def pause(self, *args, **kwargs):
        """ Pause playback. """
        return self.client.rpc_call('core.playback.pause', *args, **kwargs)

    def play(self, *args, **kwargs):
        """ Play the given track, or if the given tl_track and tlid is
    :class:`None`, play the currently active track.
    
    Note that the track **must** already be in the tracklist.
    
    .. deprecated:: 3.0
        The ``tl_track`` argument. Use ``tlid`` instead.
    
    :param tl_track: track to play
    :type tl_track: :class:`mopidy.models.TlTrack` or :class:`None`
    :param tlid: TLID of the track to play
    :type tlid: :class:`int` or :class:`None` """
        return self.client.rpc_call('core.playback.play', *args, **kwargs)

    def previous(self, *args, **kwargs):
        """ Change to the previous track.
    
    The current playback state will be kept. If it was playing, playing
    will continue. If it was paused, it will still be paused, etc. """
        return self.client.rpc_call('core.playback.previous', *args, **kwargs)

    def resume(self, *args, **kwargs):
        """ If paused, resume playing the current track. """
        return self.client.rpc_call('core.playback.resume', *args, **kwargs)

    def seek(self, *args, **kwargs):
        """ Seeks to time position given in milliseconds.
    
    :param time_position: time position in milliseconds
    :type time_position: int
    :rtype: :class:`True` if successful, else :class:`False` """
        return self.client.rpc_call('core.playback.seek', *args, **kwargs)

    def set_state(self, *args, **kwargs):
        """ Set the playback state.
    
    Must be :attr:`PLAYING`, :attr:`PAUSED`, or :attr:`STOPPED`.
    
    Possible states and transitions:
    
    .. digraph:: state_transitions
    
        "STOPPED" -> "PLAYING" [ label="play" ]
        "STOPPED" -> "PAUSED" [ label="pause" ]
        "PLAYING" -> "STOPPED" [ label="stop" ]
        "PLAYING" -> "PAUSED" [ label="pause" ]
        "PLAYING" -> "PLAYING" [ label="play" ]
        "PAUSED" -> "PLAYING" [ label="resume" ]
        "PAUSED" -> "STOPPED" [ label="stop" ] """
        return self.client.rpc_call('core.playback.set_state', *args, **kwargs)

    def stop(self, *args, **kwargs):
        """ Stop playing. """
        return self.client.rpc_call('core.playback.stop', *args, **kwargs)
