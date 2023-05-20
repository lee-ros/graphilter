from abc import abstractmethod
import typing

import numpy as np


class SignalInput:
    def __init__(self):
        self._signal


class SignalBase:
    def __init__(
        self,
        *,
        start=0,
        end=0,
        step=1000,
        base_signal: typing.Optional["SignalBase"] = None
    ):
        self._outputs: typing.List[SignalBase] = []
        self._x: np.array = None
        self._signal: np.array = None
        self._processed_signal: np.array = None

        if base_signal is not None:
            self.set_input_signal(base_signal)
        else:
            self._start = start
            self._end = end
            self._step = step


    @property
    def x(
        self,
    ):
        return self._x

    @property
    def signal(
        self,
    ):
        return self._signal

    @property
    def processed_signal(
        self,
    ):
        return self._processed_signal

    def set_input_signal(self, input: "SignalBase"):
        if input is None:
            return
        if not isinstance(input, SignalBase):
            raise TypeError("Input must be of base class SignalBase")

        input._outputs.append(self)
        
        self._signal = input.processed_signal
        self._x = input.x

    def add_output(self, output: "SignalBase"):
        if output is None:
            return
        if not isinstance(output, SignalBase):
            raise TypeError("Output must be of base class SignalBase")

        self._outputs.append(output)
        output.set_input_signal(self)
        
    def send_processed_to_outputs(self):
        for output in self._outputs:
            output._signal = self._processed_signal 

    @abstractmethod
    def process(self):
        ...
