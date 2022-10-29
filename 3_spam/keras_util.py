
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
            return False

    return True


class SaveModelsAndTerminateEarly(Callback):
    def on_epoch_begin(self, _1, _2):
        self.batch_accuracies = []
        self.epoch_accuracies = []

    def set_params(self, model_save_dir, resume_epoch=None):
        self.model_save_dir = model_save_dir
        if resume_epoch:
            self.epoch_offset = resume_epoch
        else:
            self.epoch_offset = 0

        self.acc_to_beat = 0.0
        self.epochs_left = None
