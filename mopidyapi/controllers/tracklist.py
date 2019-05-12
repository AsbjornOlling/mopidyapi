"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class TracklistController:
    def __init__(self, client):
        self.client = client

    def index(self, *args, **kwargs):
        """ The position of the given track in the tracklist.
    
    If neither *tl_track* or *tlid* is given we return the index of
    the currently playing track.
    
    :param tl_track: the track to find the index of
    :type tl_track: :class:`mopidy.models.TlTrack` or :class:`None`
    :param tlid: TLID of the track to find the index of
    :type tlid: :class:`int` or :class:`None`
    :rtype: :class:`int` or :class:`None`
    
    .. versionadded:: 1.1
        The *tlid* parameter """
        return self.client.rpc_call('core.tracklist.index', *args, **kwargs)

    def shuffle(self, *args, **kwargs):
        """ Shuffles the entire tracklist. If ``start`` and ``end`` is given only
    shuffles the slice ``[start:end]``.
    
    Triggers the :meth:`mopidy.core.CoreListener.tracklist_changed` event.
    
    :param start: position of first track to shuffle
    :type start: int or :class:`None`
    :param end: position after last track to shuffle
    :type end: int or :class:`None` """
        return self.client.rpc_call('core.tracklist.shuffle', *args, **kwargs)

    def next_track(self, *args, **kwargs):
        """ The track that will be played if calling
    :meth:`mopidy.core.PlaybackController.next()`.
    
    For normal playback this is the next track in the tracklist. If repeat
    is enabled the next track can loop around the tracklist. When random is
    enabled this should be a random track, all tracks should be played once
    before the tracklist repeats.
    
    :param tl_track: the reference track
    :type tl_track: :class:`mopidy.models.TlTrack` or :class:`None`
    :rtype: :class:`mopidy.models.TlTrack` or :class:`None` """
        return self.client.rpc_call('core.tracklist.next_track', *args, **kwargs)

    def get_random(self, *args, **kwargs):
        """ Get random mode.
    
    :class:`True`
        Tracks are selected at random from the tracklist.
    :class:`False`
        Tracks are played in the order of the tracklist. """
        return self.client.rpc_call('core.tracklist.get_random', *args, **kwargs)

    def get_length(self, *args, **kwargs):
        """ Get length of the tracklist. """
        return self.client.rpc_call('core.tracklist.get_length', *args, **kwargs)

    def get_next_tlid(self, *args, **kwargs):
        """ The tlid of the track that will be played if calling
    :meth:`mopidy.core.PlaybackController.next()`.
    
    For normal playback this is the next track in the tracklist. If repeat
    is enabled the next track can loop around the tracklist. When random is
    enabled this should be a random track, all tracks should be played once
    before the tracklist repeats.
    
    :rtype: :class:`int` or :class:`None`
    
    .. versionadded:: 1.1 """
        return self.client.rpc_call('core.tracklist.get_next_tlid', *args, **kwargs)

    def previous_track(self, *args, **kwargs):
        """ Returns the track that will be played if calling
    :meth:`mopidy.core.PlaybackController.previous()`.
    
    For normal playback this is the previous track in the tracklist. If
    random and/or consume is enabled it should return the current track
    instead.
    
    :param tl_track: the reference track
    :type tl_track: :class:`mopidy.models.TlTrack` or :class:`None`
    :rtype: :class:`mopidy.models.TlTrack` or :class:`None` """
        return self.client.rpc_call('core.tracklist.previous_track', *args, **kwargs)

    def add(self, *args, **kwargs):
        """ Add tracks to the tracklist.
    
    If ``uri`` is given instead of ``tracks``, the URI is looked up in the
    library and the resulting tracks are added to the tracklist.
    
    If ``uris`` is given instead of ``uri`` or ``tracks``, the URIs are
    looked up in the library and the resulting tracks are added to the
    tracklist.
    
    If ``at_position`` is given, the tracks are inserted at the given
    position in the tracklist. If ``at_position`` is not given, the tracks
    are appended to the end of the tracklist.
    
    Triggers the :meth:`mopidy.core.CoreListener.tracklist_changed` event.
    
    :param tracks: tracks to add
    :type tracks: list of :class:`mopidy.models.Track` or :class:`None`
    :param at_position: position in tracklist to add tracks
    :type at_position: int or :class:`None`
    :param uri: URI for tracks to add
    :type uri: string or :class:`None`
    :param uris: list of URIs for tracks to add
    :type uris: list of string or :class:`None`
    :rtype: list of :class:`mopidy.models.TlTrack`
    
    .. versionadded:: 1.0
        The ``uris`` argument.
    
    .. deprecated:: 1.0
        The ``tracks`` and ``uri`` arguments. Use ``uris``. """
        return self.client.rpc_call('core.tracklist.add', *args, **kwargs)

    def get_eot_tlid(self, *args, **kwargs):
        """ The TLID of the track that will be played after the current track.
    
    Not necessarily the same TLID as returned by :meth:`get_next_tlid`.
    
    :rtype: :class:`int` or :class:`None`
    
    .. versionadded:: 1.1 """
        return self.client.rpc_call('core.tracklist.get_eot_tlid', *args, **kwargs)

    def set_single(self, *args, **kwargs):
        """ Set single mode.
    
    :class:`True`
        Playback is stopped after current song, unless in ``repeat`` mode.
    :class:`False`
        Playback continues after current song. """
        return self.client.rpc_call('core.tracklist.set_single', *args, **kwargs)

    def remove(self, *args, **kwargs):
        """ Remove the matching tracks from the tracklist.
    
    Uses :meth:`filter()` to lookup the tracks to remove.
    
    Triggers the :meth:`mopidy.core.CoreListener.tracklist_changed` event.
    
    :param criteria: on or more criteria to match by
    :type criteria: dict
    :rtype: list of :class:`mopidy.models.TlTrack` that was removed
    
    .. deprecated:: 1.1
        Providing the criteria  via ``kwargs``. """
        return self.client.rpc_call('core.tracklist.remove', *args, **kwargs)

    def get_single(self, *args, **kwargs):
        """ Get single mode.
    
    :class:`True`
        Playback is stopped after current song, unless in ``repeat`` mode.
    :class:`False`
        Playback continues after current song. """
        return self.client.rpc_call('core.tracklist.get_single', *args, **kwargs)

    def set_consume(self, *args, **kwargs):
        """ Set consume mode.
    
    :class:`True`
        Tracks are removed from the tracklist when they have been played.
    :class:`False`
        Tracks are not removed from the tracklist. """
        return self.client.rpc_call('core.tracklist.set_consume', *args, **kwargs)

    def get_previous_tlid(self, *args, **kwargs):
        """ Returns the TLID of the track that will be played if calling
    :meth:`mopidy.core.PlaybackController.previous()`.
    
    For normal playback this is the previous track in the tracklist. If
    random and/or consume is enabled it should return the current track
    instead.
    
    :rtype: :class:`int` or :class:`None`
    
    .. versionadded:: 1.1 """
        return self.client.rpc_call('core.tracklist.get_previous_tlid', *args, **kwargs)

    def slice(self, *args, **kwargs):
        """ Returns a slice of the tracklist, limited by the given start and end
    positions.
    
    :param start: position of first track to include in slice
    :type start: int
    :param end: position after last track to include in slice
    :type end: int
    :rtype: :class:`mopidy.models.TlTrack` """
        return self.client.rpc_call('core.tracklist.slice', *args, **kwargs)

    def get_repeat(self, *args, **kwargs):
        """ Get repeat mode.
    
    :class:`True`
        The tracklist is played repeatedly.
    :class:`False`
        The tracklist is played once. """
        return self.client.rpc_call('core.tracklist.get_repeat', *args, **kwargs)

    def get_version(self, *args, **kwargs):
        """ Get the tracklist version.
    
    Integer which is increased every time the tracklist is changed. Is not
    reset before Mopidy is restarted. """
        return self.client.rpc_call('core.tracklist.get_version', *args, **kwargs)

    def move(self, *args, **kwargs):
        """ Move the tracks in the slice ``[start:end]`` to ``to_position``.
    
    Triggers the :meth:`mopidy.core.CoreListener.tracklist_changed` event.
    
    :param start: position of first track to move
    :type start: int
    :param end: position after last track to move
    :type end: int
    :param to_position: new position for the tracks
    :type to_position: int """
        return self.client.rpc_call('core.tracklist.move', *args, **kwargs)

    def get_consume(self, *args, **kwargs):
        """ Get consume mode.
    
    :class:`True`
        Tracks are removed from the tracklist when they have been played.
    :class:`False`
        Tracks are not removed from the tracklist. """
        return self.client.rpc_call('core.tracklist.get_consume', *args, **kwargs)

    def get_tl_tracks(self, *args, **kwargs):
        """ Get tracklist as list of :class:`mopidy.models.TlTrack`. """
        return self.client.rpc_call('core.tracklist.get_tl_tracks', *args, **kwargs)

    def get_tracks(self, *args, **kwargs):
        """ Get tracklist as list of :class:`mopidy.models.Track`. """
        return self.client.rpc_call('core.tracklist.get_tracks', *args, **kwargs)

    def clear(self, *args, **kwargs):
        """ Clear the tracklist.
    
    Triggers the :meth:`mopidy.core.CoreListener.tracklist_changed` event. """
        return self.client.rpc_call('core.tracklist.clear', *args, **kwargs)

    def set_random(self, *args, **kwargs):
        """ Set random mode.
    
    :class:`True`
        Tracks are selected at random from the tracklist.
    :class:`False`
        Tracks are played in the order of the tracklist. """
        return self.client.rpc_call('core.tracklist.set_random', *args, **kwargs)

    def filter(self, *args, **kwargs):
        """ Filter the tracklist by the given criterias.
    
    A criteria consists of a model field to check and a list of values to
    compare it against. If the model field matches one of the values, it
    may be returned.
    
    Only tracks that matches all the given criterias are returned.
    
    Examples::
    
        # Returns tracks with TLIDs 1, 2, 3, or 4 (tracklist ID)
        filter({'tlid': [1, 2, 3, 4]})
    
        # Returns track with URIs 'xyz' or 'abc'
        filter({'uri': ['xyz', 'abc']})
    
        # Returns track with a matching TLIDs (1, 3 or 6) and a
        # matching URI ('xyz' or 'abc')
        filter({'tlid': [1, 3, 6], 'uri': ['xyz', 'abc']})
    
    :param criteria: on or more criteria to match by
    :type criteria: dict, of (string, list) pairs
    :rtype: list of :class:`mopidy.models.TlTrack`
    
    .. deprecated:: 1.1
        Providing the criteria via ``kwargs``. """
        return self.client.rpc_call('core.tracklist.filter', *args, **kwargs)

    def eot_track(self, *args, **kwargs):
        """ The track that will be played after the given track.
    
    Not necessarily the same track as :meth:`next_track`.
    
    :param tl_track: the reference track
    :type tl_track: :class:`mopidy.models.TlTrack` or :class:`None`
    :rtype: :class:`mopidy.models.TlTrack` or :class:`None` """
        return self.client.rpc_call('core.tracklist.eot_track', *args, **kwargs)

    def set_repeat(self, *args, **kwargs):
        """ Set repeat mode.
    
    To repeat a single track, set both ``repeat`` and ``single``.
    
    :class:`True`
        The tracklist is played repeatedly.
    :class:`False`
        The tracklist is played once. """
        return self.client.rpc_call('core.tracklist.set_repeat', *args, **kwargs)
