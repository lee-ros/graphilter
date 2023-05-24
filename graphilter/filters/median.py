from filters import FilterBase
import numpy as np
from utils.signal_base import SignalBase


class Median(FilterBase):
    def __init__(self, *, base_signal: SignalBase = None, window_size: int = 1):
        super().__init__(
            base_signal=base_signal,
            window_size=window_size,
            filter_function=self._median,
        )

    def _median(self, data):
        filtered_data = np.zeros_like(data)
        half_window = self._window_size // 2

        padded_data = np.pad(data, half_window, mode="edge")

        for i in range(len(data)):
            window = padded_data[i : i + self._window_size]
            sorted_window = np.sort(window)
            filtered_data[i] = sorted_window[half_window]

        return filtered_data
