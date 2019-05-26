
# std lib
from collections import namedtuple


def test_deserialize():
    """ Test turning Mopidy JSON into namedtuples """
    from mopidyapi.parsedata import deserialize_mopidy
    testtrack = {
        '__model__': 'Track',
        'name': 'Get Got',
        'disc_no': 1,
        'uri': 'spotify:track:781V2Y5LPtcpgONEOadadE',
        'length': 172000,
        'track_no': 1,
        'date': '2012',
        'bitrate': 320,
        'artists': [
            {'__model__': 'Artist',
             'name': 'Death Grips',
             'uri': 'spotify:artist:5RADpgYLOuS2ZxDq7ggYYH'}
        ],
        'album': {
            '__model__': 'Album',
            'uri': 'spotify:album:1PQDjdBpHPikAodJqjzm6a',
            'name': 'The Money Store',
            'date': '2012',
            'artists': [
                {
                 '__model__': 'Artist',
                 'name': 'Death Grips',
                 'uri': 'spotify:artist:5RADpgYLOuS2ZxDq7ggYYH'
                }
            ]
        }
    }
    result = deserialize_mopidy(testtrack)

    # check type
    assert type(result).__name__ == 'Track'
    assert isinstance(result, tuple)
    # check track attribute
    assert result.name == "Get Got"

    # check types of nested elements
    assert type(result.artists[0]).__name__ == "Artist"
    assert type(result.album).__name__ == "Album"

    # check deeply nested attribute
    assert result.album.artists[0].name == "Death Grips"


def test_serialize():
    """ Test turning nametuples into Mopidy JSON """
    from mopidyapi.parsedata import serialize_mopidy
    Album = namedtuple('Album', ['uri', 'name', 'date', 'artists'])
    Artist = namedtuple('Artist', ['name', 'uri'])
    testalbum = Album(uri='spotify:album:1PQDjdBpHPikAodJqjzm6a',
                      name='The Money Store',
                      date='2012',
                      artists=[
                          Artist(name="Death Grips",
                                 uri="spotify:artist:5RADpgYLOuS2ZxDq7ggYYH")])

    result = serialize_mopidy(testalbum)
    # check type
    assert isinstance(result, dict)
    assert result['__model__'] == 'Album'
    assert result['name'] == "The Money Store"
    # check nested value
    assert result['artists'][0]['name'] == "Death Grips"

