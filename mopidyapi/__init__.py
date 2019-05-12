"""
MopidyAPI
~~~~~~~~~
MopidyAPI is a Python (3.6+) library for interacting with Mopidy,
using its JSON RPC API.
"""

__all__ = ['client', 'wsclient', 'mopidy_types']
__version__ = '0.1.0'

from .httpclient import MopidyClient
from .wsclient import MopidyWSClient
