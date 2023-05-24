import typing
import numpy as np

from graphilter.generators import GeneratorBase, GeneratorConfig
from graphilter.utils import SignalBase


class Cos(GeneratorBase):
    def __init__(
        self,
        *,
        start=0,
        end=0,
        f_s=100,
        base_signal: typing.Optional[SignalBase] = None,
        config: GeneratorConfig = None,
    ):
        super().__init__(
            start=start, end=end, f_s=f_s, base_signal=base_signal, config=config, generator_function=np.cos
        )
