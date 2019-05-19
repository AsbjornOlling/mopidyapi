"""
MopidyAPI
~~~~~~~~~
MopidyAPI is a Python (3.6+) library for interacting with Mopidy,
using its JSON RPC API.
"""

__all__ = ['httpclient', 'wsclient']
__version__ = '0.4.2'

from .httpclient import MopidyAPI
from .wsclient import MopidyWSClient
