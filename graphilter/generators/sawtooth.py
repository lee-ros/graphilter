import typing
import numpy as np
from graphilter.generators import GeneratorConfig
from graphilter.utils import SignalBase
from . import GeneratorBase, GeneratorConfig


class Sawtooth(GeneratorBase):
    def __init__(
        self,
        *,
        start=0,
        end=0,
        f_s=100,
        base_signal: SignalBase | None = None,
        config: GeneratorConfig = None,
    ):
        super().__init__(
            start=start,
            end=end,
            f_s=f_s,
            base_signal=base_signal,
            config=config,
            generator_function=self._generate_sawtooth_wave,
        )
        
    def _generate_sawtooth_wave(self, t):
        k = np.arange(1, 99)
        f = np.zeros_like(t)
        
        for i in range(len(t)):
            f[i] = np.sum(np.sin(2 * np.pi * k * t[i]/k))
        f = (-2 / np.pi) * f
        return (t % np.pi) / np.pi
