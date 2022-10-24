
import json
import random


def each_json(fn, max_count):
    print 'Pulling samples from file: %s' % fn
    i = 0
    with open(fn) as f:
        for line in f:
            if i == max_count:
                break
            j = json.loads(line)
            yield j
            i += 1
    assert i == max_count


def all_impermium_one_source(