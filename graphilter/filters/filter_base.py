import typing

import numpy as np
from graphilter.utils import SignalBase


class FilterBase(SignalBase):
    def __init__(
        self,
        *,
        base_signal: SignalBase = None,
        window_size: int = 1,
        filter_function: typing.Callable[[np.array], np.array]
    ):
        super().__init__(base_signal=base_signal)

        self._window_size = window_size
        self._filter_function = filter_function

    def process(self):
        self._processed_signal = self._filter_function(self._signal)
        
        self.send_processed_to_outputs()
