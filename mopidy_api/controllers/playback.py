"""
This file was generated programatically,
based on JSON describing all available methods.
"""

from .connection import 


def seek():
    """ Seeks to time position given in milliseconds.
    
    :param time_position: time position in milliseconds
    :type time_position: int
    :rtype: :class:`True` if successful, else :class:`False` """


def pause():
    """ Pause playback. """


def set_state():
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


def get_state():
    """ Get The playback state. """


def play():
    """ Play the given track, or if the given tl_track and tlid is
    :class:`None`, play the currently active track.
    
    Note that the track **must** already be in the tracklist.
    
    :param tl_track: track to play
    :type tl_track: :class:`mopidy.models.TlTrack` or :class:`None`
    :param tlid: TLID of the track to play
    :type tlid: :class:`int` or :class:`None` """


def get_stream_title():
    """ Get the current stream title or :class:`None`. """


def get_current_tlid():
    """ Get the currently playing or selected TLID.
    
    Extracted from :meth:`get_current_tl_track` for convenience.
    
    Returns a :class:`int` or :class:`None`.
    
    .. versionadded:: 1.1 """


def get_current_tl_track():
    """ Get the currently playing or selected track.
    
    Returns a :class:`mopidy.models.TlTrack` or :class:`None`. """


def get_volume():
    """ .. deprecated:: 1.0
        Use :meth:`core.mixer.get_volume()
        <mopidy.core.MixerController.get_volume>` instead. """


def next():
    """ Change to the next track.
    
    The current playback state will be kept. If it was playing, playing
    will continue. If it was paused, it will still be paused, etc. """


def get_current_track():
    """ Get the currently playing or selected track.
    
    Extracted from :meth:`get_current_tl_track` for convenience.
    
    Returns a :class:`mopidy.models.Track` or :class:`None`. """


def set_volume():
    """ .. deprecated:: 1.0
        Use :meth:`core.mixer.set_volume()
        <mopidy.core.MixerController.set_volume>` instead. """


def stop():
    """ Stop playing. """


def get_mute():
    """ .. deprecated:: 1.0
        Use :meth:`core.mixer.get_mute()
        <mopidy.core.MixerController.get_mute>` instead. """


def resume():
    """ If paused, resume playing the current track. """


def get_time_position():
    """ Get time position in milliseconds. """


def previous():
    """ Change to the previous track.
    
    The current playback state will be kept. If it was playing, playing
    will continue. If it was paused, it will still be paused, etc. """


def set_mute():
    """ .. deprecated:: 1.0
        Use :meth:`core.mixer.set_mute()
        <mopidy.core.MixerController.set_mute>` instead. """

