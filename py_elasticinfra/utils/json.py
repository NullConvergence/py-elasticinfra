import json
from collections import OrderedDict


def read_json(fname, dic=True):
    with fname.open('rt') as handle:
        if dic is True:
            return json.load(handle, object_hook=OrderedDict)
        return json.load(handle)


def write_json(content, fname):
    with fname.open('wt') as handle:
        json.dump(content, handle, indent=4, sort_keys=False)
