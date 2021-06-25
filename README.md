MopidyAPI
=========

`MopidyAPI` is a Python (3.6+) library for interacting with
[Mopidy](https://www.mopidy.com/) via its [JSON RPC
API](https://docs.mopidy.com/en/latest/api/http/).

`MopidyAPI` uses HTTP to call RPC methods, and websockets to listen for events.

It is compatible with all functions present in Mopidy 3.0.1.

## Installation

```
pip install mopidyapi
```

## Usage

`MopidyAPI` contains functions mapping to each of [the Mopidy v3.0.1 core API functions.](https://docs.mopidy.com/en/latest/api/core/)

For example `mopidy.core.PlaybackController.pause()` in the documentation maps to `MopidyAPI.playback.pause()` here.

### Quick example

```python
>>> from mopidyapi import MopidyAPI
>>> m = MopidyAPI()
>>> tracks = m.tracklist.get_tracks()
>>> tracks[0].name

	'I've Seen Footage'

>>> tracks[0].artists

	[Artist(name='Death Grips', uri='spotify:artist:5RADpgYLOuS2ZxDq7ggYYH')]

>>> tracks[0]._fields

	('album',
	 'name',
	 'disc_no',
	 'uri',
	 'length',
	 'track_no',
	 'artists',
	 'date',
	 'bitrate')
```


### Connecting to Mopidy

To connect to Mopidy, you need to instantiate a `MopidyAPI` object.
By default, it will connect to Mopidy at `localhost:6680`,
so you might not need to give the constructor any arguments.

```python
from mopidyapi import MopidyAPI
m = MopidyAPI(host='my.mopidy.host.com', port=6680)
```

You can also pass `use_websockets=False`, to prevent starting the websocket listener,
which runs in a separate thread. However, event listening (described below) won't work with this set.


### Calling Mopidy functions

All of the functions described in the
[Mopidy 3.0.1 core API documentation](http://docs.mopidy.com/en/latest/api/core/)
are available in `MopidyAPI`.

Functions named in the Mopidy docs as `core.<ControllerName>Controller.<functionname>()`,
will be under the name `MopidyAPI.<controllername>.<functionname>()`

For example, you can pause the music by calling `m.playback.pause()`,
or you could search for a song by calling e.g. `m.library.search(artist='Rick Astley')`, where `m = MopidyAPI()`.

Functions will return
[Python native `namedtuple`](https://docs.python.org/3.7/library/collections.html#collections.namedtuple)
representations of the returned data.


### Event listening

You can use function decorators to mark specific functions to be called when an event arrives. See example below.

The events used are described in [Mopidy's core events documentation.](https://docs.mopidy.com/en/latest/api/core/#core-events)

```python
from mopidyapi import MopidyAPI
m = MopidyAPI()

@m.on_event('volume_changed')
def print_volume(event):
    print(f"Volume changed to: {event.volume}")

@m.on_event('track_playback_started')
def print_newtracks(event):
    print(f"Started playing track: {event.track.name}")

```

Like with function calls, the events passed are [namedtuples.](https://docs.python.org/3.7/library/collections.html#collections.namedtuple)

If you need to add and remove callbacks more dynamically, you can use the `add_callback` and `del_callback` functions.

`del_callback` accepts two keyword arguments:
- `event`: an event name string to remove all callbacks for
- `f`: a callback function to remove

You can use one or both. Here's an example of passing a function to `del_callback`:

```python
from mopidyapi import MopidyAPI
m = MopidyAPI()

def print_volume(event):
    """ Print volume only once. Delete callback after first call """
    print(f"Volume changed to: {event.volume}")
    m.del_callback(f=print_volume)

m.add_callback('volume_changed', print_volume)
```

An important caveat with both the event listener decorators and add methods,
is that it will not warn you in any way, if you use an invalid event name (e.g. you misspell the event name).

## Note on the choice of `namedtuples`

### Why `namedtuples`?

The choice of namedtuples might seem unusual (or even inconvenient),
but they have a number of advantages over dictionaries for this application:

**1. Less verbose than dicts.**

`event.tl_track.track.album.name`

is shorter and easier on the eyes than

`event['tl_track']['track']['album']['name']`

**2. They print much more neatly.**

`Artist(name='Death Grips', uri='spotify:artist:5RADpgYLOuS2ZxDq7ggYYH')`

is much better than

`{'name': 'Death Grips', 'uri': 'spotify:artist:5RADpgYLOuS2ZxDq7ggYYH'}`.

**3. `namedtuples` accurately represent the immutable nature of the data.**

Being allowed to mutate the data coming from Mopidy might give one the idea that this would change the data inside Mopidy, which is obviously not the case.


### ...but, I know dicts!

Okay, so if you need `.keys()`, you can use `._fields()` instead,
and if you absolutely need a dict, you can use `._asdict()`,
which will return an actual dict.


## Contributing

Please do tell me about bugs via the [github issue tracker](https://github.com/AsbjornOlling/mopidyapi).

Also feel free to write, if you're just in the mood to help me improve this project. I don't bite :)


## License

This project is licensed under the GPLv3.
See the `LICENSE` file for details.
