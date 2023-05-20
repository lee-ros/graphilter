import typing

from graphilter.utils import SignalBase


class SignalChain(SignalBase):
    def __init__(self, signals: typing.List[SignalBase] = None):
        super().__init__(base_signal=signals[0])
        self._signals = signals
        
    def process(self):
        for signal in self._signals:
            signal.process()
            self._processed_signal = signal.processed_signal