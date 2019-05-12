"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class PlaylistsController:
    def __init__(self, client):
        self.client = client

    def save(self, *args, **kwargs):
        """ Save the playlist.
    
    For a playlist to be saveable, it must have the ``uri`` attribute set.
    You must not set the ``uri`` atribute yourself, but use playlist
    objects returned by :meth:`create` or retrieved from :attr:`playlists`,
    which will always give you saveable playlists.
    
    The method returns the saved playlist. The return playlist may differ
    from the saved playlist. E.g. if the playlist name was changed, the
    returned playlist may have a different URI. The caller of this method
    must throw away the playlist sent to this method, and use the
    returned playlist instead.
    
    If the playlist's URI isn't set or doesn't match the URI scheme of a
    current backend, nothing is done and :class:`None` is returned.
    
    :param playlist: the playlist
    :type playlist: :class:`mopidy.models.Playlist`
    :rtype: :class:`mopidy.models.Playlist` or :class:`None` """
        return self.client.rpc_call('core.playlists.save', *args, **kwargs)

    def get_playlists(self, *args, **kwargs):
        """ Get the available playlists.
    
    :rtype: list of :class:`mopidy.models.Playlist`
    
    .. versionchanged:: 1.0
        If you call the method with ``include_tracks=False``, the
        :attr:`~mopidy.models.Playlist.last_modified` field of the returned
        playlists is no longer set.
    
    .. deprecated:: 1.0
        Use :meth:`as_list` and :meth:`get_items` instead. """
        return self.client.rpc_call('core.playlists.get_playlists', *args, **kwargs)

    def refresh(self, *args, **kwargs):
        """ Refresh the playlists in :attr:`playlists`.
    
    If ``uri_scheme`` is :class:`None`, all backends are asked to refresh.
    If ``uri_scheme`` is an URI scheme handled by a backend, only that
    backend is asked to refresh. If ``uri_scheme`` doesn't match any
    current backend, nothing happens.
    
    :param uri_scheme: limit to the backend matching the URI scheme
    :type uri_scheme: string """
        return self.client.rpc_call('core.playlists.refresh', *args, **kwargs)

    def lookup(self, *args, **kwargs):
        """ Lookup playlist with given URI in both the set of playlists and in any
    other playlist sources. Returns :class:`None` if not found.
    
    :param uri: playlist URI
    :type uri: string
    :rtype: :class:`mopidy.models.Playlist` or :class:`None` """
        return self.client.rpc_call('core.playlists.lookup', *args, **kwargs)

    def delete(self, *args, **kwargs):
        """ Delete playlist identified by the URI.
    
    If the URI doesn't match the URI schemes handled by the current
    backends, nothing happens.
    
    Returns :class:`True` if deleted, :class:`False` otherwise.
    
    :param uri: URI of the playlist to delete
    :type uri: string
    :rtype: :class:`bool`
    
    .. versionchanged:: 2.2
        Return type defined. """
        return self.client.rpc_call('core.playlists.delete', *args, **kwargs)

    def create(self, *args, **kwargs):
        """ Create a new playlist.
    
    If ``uri_scheme`` matches an URI scheme handled by a current backend,
    that backend is asked to create the playlist. If ``uri_scheme`` is
    :class:`None` or doesn't match a current backend, the first backend is
    asked to create the playlist.
    
    All new playlists must be created by calling this method, and **not**
    by creating new instances of :class:`mopidy.models.Playlist`.
    
    :param name: name of the new playlist
    :type name: string
    :param uri_scheme: use the backend matching the URI scheme
    :type uri_scheme: string
    :rtype: :class:`mopidy.models.Playlist` or :class:`None` """
        return self.client.rpc_call('core.playlists.create', *args, **kwargs)

    def get_uri_schemes(self, *args, **kwargs):
        """ Get the list of URI schemes that support playlists.
    
    :rtype: list of string
    
    .. versionadded:: 2.0 """
        return self.client.rpc_call('core.playlists.get_uri_schemes', *args, **kwargs)

    def get_items(self, *args, **kwargs):
        """ Get the items in a playlist specified by ``uri``.
    
    Returns a list of :class:`~mopidy.models.Ref` objects referring to the
    playlist's items.
    
    If a playlist with the given ``uri`` doesn't exist, it returns
    :class:`None`.
    
    :rtype: list of :class:`mopidy.models.Ref`, or :class:`None`
    
    .. versionadded:: 1.0 """
        return self.client.rpc_call('core.playlists.get_items', *args, **kwargs)

    def filter(self, *args, **kwargs):
        """ Filter playlists by the given criterias.
    
    Examples::
    
        # Returns track with name 'a'
        filter({'name': 'a'})
    
        # Returns track with URI 'xyz'
        filter({'uri': 'xyz'})
    
        # Returns track with name 'a' and URI 'xyz'
        filter({'name': 'a', 'uri': 'xyz'})
    
    :param criteria: one or more criteria to match by
    :type criteria: dict
    :rtype: list of :class:`mopidy.models.Playlist`
    
    .. deprecated:: 1.0
        Use :meth:`as_list` and filter yourself. """
        return self.client.rpc_call('core.playlists.filter', *args, **kwargs)

    def as_list(self, *args, **kwargs):
        """ Get a list of the currently available playlists.
    
    Returns a list of :class:`~mopidy.models.Ref` objects referring to the
    playlists. In other words, no information about the playlists' content
    is given.
    
    :rtype: list of :class:`mopidy.models.Ref`
    
    .. versionadded:: 1.0 """
        return self.client.rpc_call('core.playlists.as_list', *args, **kwargs)
