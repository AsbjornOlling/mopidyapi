"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class LibraryController:
    def __init__(self, client):
        self.client = client

    def lookup(self, *args, **kwargs):
        """ Lookup the given URIs.
    
    If the URI expands to multiple tracks, the returned list will contain
    them all.
    
    :param uri: track URI
    :type uri: string or :class:`None`
    :param uris: track URIs
    :type uris: list of string or :class:`None`
    :rtype: list of :class:`mopidy.models.Track` if uri was set or
        {uri: list of :class:`mopidy.models.Track`} if uris was set.
    
    .. versionadded:: 1.0
        The ``uris`` argument.
    
    .. deprecated:: 1.0
        The ``uri`` argument. Use ``uris`` instead. """
        return self.client.rpc_call('core.library.lookup', *args, **kwargs)

    def get_distinct(self, *args, **kwargs):
        """ List distinct values for a given field from the library.
    
    This has mainly been added to support the list commands the MPD
    protocol supports in a more sane fashion. Other frontends are not
    recommended to use this method.
    
    :param string field: One of ``track``, ``artist``, ``albumartist``,
        ``album``, ``composer``, ``performer``, ``date`` or ``genre``.
    :param dict query: Query to use for limiting results, see
        :meth:`search` for details about the query format.
    :rtype: set of values corresponding to the requested field type.
    
    .. versionadded:: 1.0 """
        return self.client.rpc_call('core.library.get_distinct', *args, **kwargs)

    def refresh(self, *args, **kwargs):
        """ Refresh library. Limit to URI and below if an URI is given.
    
    :param uri: directory or track URI
    :type uri: string """
        return self.client.rpc_call('core.library.refresh', *args, **kwargs)

    def browse(self, *args, **kwargs):
        """ Browse directories and tracks at the given ``uri``.
    
    ``uri`` is a string which represents some directory belonging to a
    backend. To get the intial root directories for backends pass
    :class:`None` as the URI.
    
    Returns a list of :class:`mopidy.models.Ref` objects for the
    directories and tracks at the given ``uri``.
    
    The :class:`~mopidy.models.Ref` objects representing tracks keep the
    track's original URI. A matching pair of objects can look like this::
    
        Track(uri='dummy:/foo.mp3', name='foo', artists=..., album=...)
        Ref.track(uri='dummy:/foo.mp3', name='foo')
    
    The :class:`~mopidy.models.Ref` objects representing directories have
    backend specific URIs. These are opaque values, so no one but the
    backend that created them should try and derive any meaning from them.
    The only valid exception to this is checking the scheme, as it is used
    to route browse requests to the correct backend.
    
    For example, the dummy library's ``/bar`` directory could be returned
    like this::
    
        Ref.directory(uri='dummy:directory:/bar', name='bar')
    
    :param string uri: URI to browse
    :rtype: list of :class:`mopidy.models.Ref`
    
    .. versionadded:: 0.18 """
        return self.client.rpc_call('core.library.browse', *args, **kwargs)

    def search(self, *args, **kwargs):
        """ Search the library for tracks where ``field`` contains ``values``.
    ``field`` can be one of ``uri``, ``track_name``, ``album``, ``artist``,
    ``albumartist``, ``composer``, ``performer``, ``track_no``, ``genre``,
    ``date``, ``comment`` or ``any``.
    
    If ``uris`` is given, the search is limited to results from within the
    URI roots. For example passing ``uris=['file:']`` will limit the search
    to the local backend.
    
    Examples::
    
        # Returns results matching 'a' in any backend
        search({'any': ['a']})
    
        # Returns results matching artist 'xyz' in any backend
        search({'artist': ['xyz']})
    
        # Returns results matching 'a' and 'b' and artist 'xyz' in any
        # backend
        search({'any': ['a', 'b'], 'artist': ['xyz']})
    
        # Returns results matching 'a' if within the given URI roots
        # "file:///media/music" and "spotify:"
        search({'any': ['a']}, uris=['file:///media/music', 'spotify:'])
    
        # Returns results matching artist 'xyz' and 'abc' in any backend
        search({'artist': ['xyz', 'abc']})
    
    :param query: one or more queries to search for
    :type query: dict
    :param uris: zero or more URI roots to limit the search to
    :type uris: list of string or :class:`None`
    :param exact: if the search should use exact matching
    :type exact: :class:`bool`
    :rtype: list of :class:`mopidy.models.SearchResult`
    
    .. versionadded:: 1.0
        The ``exact`` keyword argument, which replaces :meth:`find_exact`.
    
    .. deprecated:: 1.0
        Previously, if the query was empty, and the backend could support
        it, all available tracks were returned. This has not changed, but
        it is strongly discouraged. No new code should rely on this
        behavior.
    
    .. deprecated:: 1.1
        Providing the search query via ``kwargs`` is no longer supported. """
        return self.client.rpc_call('core.library.search', *args, **kwargs)

    def find_exact(self, *args, **kwargs):
        """ Search the library for tracks where ``field`` is ``values``.
    
    .. deprecated:: 1.0
        Use :meth:`search` with ``exact`` set. """
        return self.client.rpc_call('core.library.find_exact', *args, **kwargs)

    def get_images(self, *args, **kwargs):
        """ Lookup the images for the given URIs
    
    Backends can use this to return image URIs for any URI they know about
    be it tracks, albums, playlists. The lookup result is a dictionary
    mapping the provided URIs to lists of images.
    
    Unknown URIs or URIs the corresponding backend couldn't find anything
    for will simply return an empty list for that URI.
    
    :param uris: list of URIs to find images for
    :type uris: list of string
    :rtype: {uri: tuple of :class:`mopidy.models.Image`}
    
    .. versionadded:: 1.0 """
        return self.client.rpc_call('core.library.get_images', *args, **kwargs)
