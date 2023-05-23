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
        f_s=100,
        base_signal: typing.Optional[SignalBase] = None,
        config: GeneratorConfig = None,
        generator_function: typing.Callable[[np.array], None]
    ):
        self._config = config if config is not None else GeneratorConfig()
        self._generator_function = generator_function

        if base_signal is not None:
            super().__init__(base_signal=base_signal)
        else:
            super().__init__(start=start, end=end, f_S=f_s)
            self._x = np.linspace(self._start, self._end, f_s)
            self._signal = np.zeros(f_s)

    def process(self):
        self._processed_signal = (
            self._signal
            + self._config.amplitude
            * (
                self._generator_function(
                    self._config.frequency * self._x + self._config.phase
                )
                ** self._config.power
            )
            + self._config.y_offset
        )

        self.send_processed_to_outputs()
