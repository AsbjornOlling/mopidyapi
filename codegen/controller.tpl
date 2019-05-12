"""
This file was generated programatically,
based on JSON describing all available methods.
"""


class {{ name.title() }}Controller:
    def __init__(self, client):
        self.client = client
{% for m in methods %}
    def {{ m.split('.')[-1] }}(self, *args, **kwargs):
        """ {{ methods[m]['description'].replace('\n','\n    ') }} """
        return self.client.rpc_call('{{ m }}', *args, **kwargs)
{% endfor %}
