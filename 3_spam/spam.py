
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