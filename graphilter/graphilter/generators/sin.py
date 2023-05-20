import typing
import numpy as np

from graphilter.generators import GeneratorBase, GeneratorConfig
from graphilter.utils import SignalBase


class Sin(GeneratorBase):
    def __init__(
        self,
        *,
        start=0,
        end=0,
        step=100,
        base_signal: typing.Optional[SignalBase] = None,
        config: GeneratorConfig = None,
    ):
        super().__init__(
            start=start, end=end, step=step, base_signal=base_signal, config=config, generator_function=np.sin
        )
