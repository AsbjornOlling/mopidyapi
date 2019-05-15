MopidyAPI
=========

`MopidyAPI` is a Python (3.6+) library for interacting with
[Mopidy](https://www.mopidy.com/) via its [JSON RPC
API](https://docs.mopidy.com/en/latest/api/http/).

`MopidyAPI` uses HTTP to call RPC methods, and websockets to listen for events.

It is compatible with all functions present in Mopidy 2.2.

## Installation

```
pip install mopidyapi
```

## Usage

`MopidyAPI` contains functions mapping to each of [the Mopidy v2.2 core API functions.](https://docs.mopidy.com/en/release-2.2/api/core/)

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

Instantiate a `MopidyAPI` object.
By default, it connects to Mopidy at `localhost:6680`,
so you might not need to give the constructor any arguments.

```python
from mopidyapi import MopidyAPI
m = MopidyAPI(host='my.mopidy.host.com', port=6680)
```

You can also pass `use_websockets=False`, to prevent starting the websocket listener,
which runs in a separate thread. However, event listening (described below) won't work with this set.


### Calling RPC methods

All of the functions described in the
[Mopidy 2.2 core API documentation](http://docs.mopidy.com/en/latest/api/core/)
are available in `MopidyAPI`.

For example, you can pause the music by calling `m.playback.pause()` (where `m = MopidyAPI()`).

Functions will generally return python native [`namedtuple`](https://docs.python.org/3.7/library/collections.html#collections.namedtuple)
representations of the returned data. 


### Event listening

You can use function decorators to mark specific functions to be called when an event arrives.
The events used are described in [Mopidy's core events documentation.](https://docs.mopidy.com/en/latest/api/core/#core-events)

```python
from mopidyapi import MopidyAPI
m = MopidyAPI()

@m.on_event('volume_changed')
def on_volume_changed(event):
	print('event')

```


## License

This project is licensed under the GPLv3.
See the `LICENSE` file for details.

