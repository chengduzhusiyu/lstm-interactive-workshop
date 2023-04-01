from camacho.base import Transformer
from camacho.pipelines import TransformerPipeline
from camacho.preprocess.sequence.coders import IntCoder
from camacho.preprocess.binarize.onehot import AtomBinarizer


class ExtractFrontBackText(Transformer):
    def __init__(self, length=128):
        self.length = length

    def transform(self, jj):
        n = self.length / 2
      