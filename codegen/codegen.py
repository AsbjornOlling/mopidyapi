""" Mopidy API Controller Code Generator.

Usage:
    codegen.py [--outdir <outdir>] [--template <template>] [--rpcurl <rpcurl>]

Options:
    --outdir <outdir>       Directory to output generated files [default: ./code].
    --template <template>   Jinja2 template to generate code [default: ./controller.tpl].
    --rpcurl <rpcurl>       Mopidy RPC URL. [default: http://localhost:6680/mopidy/rpc].
"""

# std lib
from typing import Set
from pathlib import Path

# deps
from requests import post
from jinja2 import Template
from docopt import docopt


def get_rpc_methods(rpcurl):
    """ Get JSON of available methods from running
    Mopidy instance, using the JSON RPC via HTTP POST.
    """
    r = post(rpcurl, json={'jsonrpc': '2.0',
                           'id': 0,
                           'method': 'core.describe'})
    assert 200 == r.status_code, f"HTTP {r.status_code} from Mopidy."
    result = r.json()
    methods = result['result']
    return methods


def get_controller_names(methods: dict) -> Set:
    """ Return list of controller names, extracted from
    the 'core.controller.method' format method names.
    """
    # remove 'core.method' format names
    ctrlmethods = filter(lambda x: x.count('.') == 2,
                         methods.keys())
    return {m.split('.')[1] for m in ctrlmethods}


def group_by_controller(methods: dict) -> dict:
    """ Return a dict with methods grouped by controller """
    grouped = {}
    for c in get_controller_names(methods):
        grouped[c] = {m: methods[m] for m in methods.keys() if c in m}
    return grouped


def render_code(name, methods, template=None, outdir=None):
    """ Render code with Jinja2, then write to file. """
    assert template is not None, "Keyword argument 'template' must be set."
    assert outdir is not None, "Keyword argument 'outdir' must be set."
    code = template.render(name=name, methods=methods)

    # write to file
    assert Path(outdir).is_dir(), f"{outdir} is not a directory."
    with open(f"{outdir}/{name}.py", 'w') as f:
        f.write(code)


if __name__ == '__main__':
    # get cli command using docopt
    args = docopt(__doc__)

    # get rpc methods json using http
    methods = get_rpc_methods(args['--rpcurl'])

    # group by controller name
    grouped = group_by_controller(methods)

    # read template
    with open(args['--template']) as f:
        tplstr = f.read()
        tpl = Template(tplstr)

    # render and write to file
    for c in grouped.keys():
        print(f"Generating {c}...")
        render_code(c, grouped[c], template=tpl,
                    outdir=args['--outdir'])
