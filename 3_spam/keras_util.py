
from keras.callbacks import Callback
import os


def show_accuracy(f):
    if f == 1.0:
        f = 0.9999999999

    try:
        assert 0 <= f < 1
        s = '%.5f' % f
        return s[2:]
    except:
        return 'xxxx'


class EarlyTermination(Exception):
    pass


def is_hopeless(accs):
    if len(accs) < 5:
        return False

    for i in range(len(accs) - 5, len(accs) - 1):
        a = accs[i]
        b = accs[i + 1]
        if a < b: