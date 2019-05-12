"""
This file was generated programatically,
based on JSON describing all available methods.
"""

from ..connection import mopidy_post

{% for m in methods %}
def {{ m.split('.')[-1] }}():
    """ {{ methods[m]['description'].replace('\n','\n    ') }} """

{% endfor %}
