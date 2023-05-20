import typing

import numpy as np

from graphilter.generators import GeneratorConfig
from graphilter.utils import SignalBase


class GeneratorBase(SignalBase):
    def __init__(
        self,
        *,
        start=0,
        end=0,
        step=100,
        base_signal: typing.Optional[SignalBase] = None,
        config: GeneratorConfig = None,
        generator_function: typing.Callable[[np.array], None]
    ):
        self._config = config if config is not None else GeneratorConfig()
        self._generator_function = generator_function

        if base_signal is not None:
            super().__init__(base_signal=base_signal)
        else:
            super().__init__(start=start, end=end, step=step)
            self._x = np.linspace(self._start, self._end, step)
            self._signal = np.zeros(step)

    def process(self):
        self._processed_signal = (
            self._signal
            + self._config.outer_coeff
            * (
                self._generator_function(
                    self._config.inner_coeff * self._x + self._config.inner_offset
                )
                ** self._config.power
            )
            + self._config.outer_offset
        )

        self.send_processed_to_outputs()
