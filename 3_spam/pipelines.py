from camacho.base import Transformer
from camacho.pipelines import TransformerPipeline
from camacho.preprocess.sequence.coders import IntCoder
from camacho.preprocess.binarize.onehot import AtomBinarizer


class ExtractFrontBackText(Transfo