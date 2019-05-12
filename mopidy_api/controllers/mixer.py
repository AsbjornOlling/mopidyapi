"""
This file was generated programatically,
based on JSON describing all available methods.
"""

from .connection import 


def set_mute():
    """ Set mute state.
    
    :class:`True` to mute, :class:`False` to unmute.
    
    Returns :class:`True` if call is successful, otherwise :class:`False`. """


def get_volume():
    """ Get the volume.
    
    Integer in range [0..100] or :class:`None` if unknown.
    
    The volume scale is linear. """


def get_mute():
    """ Get mute state.
    
    :class:`True` if muted, :class:`False` unmuted, :class:`None` if
    unknown. """


def set_volume():
    """ Set the volume.
    
    The volume is defined as an integer in range [0..100].
    
    The volume scale is linear.
    
    Returns :class:`True` if call is successful, otherwise :class:`False`. """

