"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class MixerController:
    def __init__(self, client):
        self.client = client

    def set_mute(self, *args, **kwargs):
        """ Set mute state.
    
    :class:`True` to mute, :class:`False` to unmute.
    
    Returns :class:`True` if call is successful, otherwise :class:`False`. """
        return self.client.rpc_call('core.mixer.set_mute', *args, **kwargs)

    def get_volume(self, *args, **kwargs):
        """ Get the volume.
    
    Integer in range [0..100] or :class:`None` if unknown.
    
    The volume scale is linear. """
        return self.client.rpc_call('core.mixer.get_volume', *args, **kwargs)

    def get_mute(self, *args, **kwargs):
        """ Get mute state.
    
    :class:`True` if muted, :class:`False` unmuted, :class:`None` if
    unknown. """
        return self.client.rpc_call('core.mixer.get_mute', *args, **kwargs)

    def set_volume(self, *args, **kwargs):
        """ Set the volume.
    
    The volume is defined as an integer in range [0..100].
    
    The volume scale is linear.
    
    Returns :class:`True` if call is successful, otherwise :class:`False`. """
        return self.client.rpc_call('core.mixer.set_volume', *args, **kwargs)
