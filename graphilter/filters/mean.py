from filters import FilterBase
import numpy as np
from utils.signal_base import SignalBase


class Mean(FilterBase):
    def __init__(self, *, base_signal: SignalBase = None, window_size: int = 1):
        super().__init__(
            base_signal=base_signal,
            window_size=window_size,
            filter_function=self._mean,
        )

    def _mean(self, data):
        filtered_data = np.zeros_like(data)
        half_window = self._window_size // 2

        padded_data = np.pad(data, half_window, mode="edge")

        for i in range(len(data)):
            window = padded_data[i - half_window : i + half_window]
            window_mean = np.sum(window) / len(window)
            filtered_data[i] = window_mean

        return filtered_data
