"""
MopidyAPI
~~~~~~~~~
MopidyAPI is a Python (3.6+) library for interacting with Mopidy,
using its JSON RPC API.
"""

__all__ = ['client', 'wsclient', 'exceptions']
__version__ = '0.6.4'

from .client import MopidyAPI
from .wsclient import MopidyWSClient
