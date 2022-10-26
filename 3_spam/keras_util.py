
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
