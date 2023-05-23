import typing

from graphilter.utils import SignalBase


class SignalChain(SignalBase):
    def __init__(self, signals: typing.List[SignalBase] = None):
        super().__init__(base_signal=signals[0])
        self._signals = signals
        
        self._setup_signals()
        
    def _setup_signals(self):
        for i in range(len(self._signals)-1):
            self._signals[i+1].set_input_signal(self._signals[i])
            
        
    def process(self):
        for signal in self._signals:
            signal.process()
            self._processed_signal = signal.processed_signal