"""
MopidyAPI
~~~~~~~~~
MopidyAPI is a Python (3.6+) library for interacting with Mopidy,
using its JSON RPC API.
"""

__all__ = ['client', 'wsclient']
__version__ = '0.5.0'

from .client import MopidyAPI
from .wsclient import MopidyWSClient
