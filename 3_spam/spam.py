
#!/usr/bin/env python

from argparse import ArgumentParser
import datasets
from glob import glob
from keras_util import EarlyTermination, SaveModelsAndTerminateEarly
import networks
import numpy as np
import pipelines
import random


def parse_args():
    ap = ArgumentParser()
    ap.add_argument('--source', type=str, default='fyre')
    ap.add_argument('--samples_per_class', type=int, default=5000)
    ap.add_argument('--network', type=str, default='dense_0_256_6')
    return ap.parse_args()


def get_epoch(f):
    x = f.index('epoch_') + len('epoch_')
    e = f[x:]
    e = e[:e.index('_')]
    return int(e)


def get_last_checkpoint(d):
    ff = glob(d + '/*')
    if not ff:
        return None, 0

    ff.sort()
    f = ff[-1]

    return f, get_epoch(f) + 1


def transform_data((train, val, test), X_tf, y_tf):
    train = (X_tf.fit_transform(train[0]),
             y_tf.fit_transform(train[1]))
    val = (X_tf.transform(val[0]), y_tf.transform(val[1]))
    test = (X_tf.transform(test[0]), y_tf.transform(test[1]))