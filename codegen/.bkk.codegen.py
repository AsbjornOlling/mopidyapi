"""
This script will query mopidy for all available JSON RPC methods, by
calling the 'core.describe' method. It then generates classes for each
of the controllers, containing the correct methods.
"""

# std lib
from typing import List, Set
from collections import defaultdict

# deps
from requests import post
from pprint import pprint as print

MOPIDY_RPC_URL = 'http://localhost:6680/mopidy/rpc'


def get_mopidy_methods() -> dict:
    """ Get JSON RPC methods from Mopidy via HTTP. """
    r = post(MOPIDY_RPC_URL,
             json={'jsonrpc': '2.0',
                   'id': 1,
                   'method': 'core.describe'})
    assert 200 == r.status_code, "Could not connect to Mopidy."
    data = r.json()
    assert 'error' not in data.keys(), f"Got mopidy error: {data.get('error')}"
    methods = data['result']
    return methods


def controller_names(methods: dict) -> Set[str]:
    """ Get from rpc methods dict to list of controllers """
    # skip 'core.method' methods
    # only keep 'core.controller.method' methods
    controller_methods = filter(lambda m: m.count('.') == 2, methods)

    # 'core.controller.method' -> 'controller', keep unique
    controllers = {m.split('.')[1] for m in controller_methods}
    return controllers


def group_by_controller(methods: dict) -> dict:
    """ Returns dict of all methods, sorted into
    keys representing their respective controllers.
    """
    grouped = {}
    for c in controller_names(methods):
        # get methods belonging to controller
        cmethods = filter(lambda m: c in m, methods)
        # add the entire method entries to the grouping dict
        grouped[c] = {m.split('.')[-1]: methods[m] for m in cmethods}
    return grouped


if __name__ == '__main__':
    # get complete rpc methods dict
    methods = get_mopidy_methods()
    grouped = group_by_controller(methods)
    print(grouped)
