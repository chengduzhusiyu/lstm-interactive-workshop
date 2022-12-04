from keras.models import Sequential
from keras.layers.advanced_activations import PReLU
from keras.layers.core import Activation, Dense, Dropout, Flatten, \
    TimeDistributedDense
from keras.layers.embeddings import Embedding
from keras.layers.normalization import BatchNormalization
import numpy as np


def mak