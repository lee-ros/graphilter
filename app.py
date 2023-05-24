import numpy as np
import matplotlib.pyplot as plt

from graphilter.generators import Cos, Sin, GeneratorConfig, Sawtooth
from graphilter.utils import SignalChain


def main():
    base = Sawtooth(end=20, f_s=5000)

    # base = Cos(start=-10 * np.pi, end=10 * np.pi, f_s=10000)
    noise = Sin(
        config=GeneratorConfig(amplitude=0.1, frequency=20, phase=np.pi),
    )
    slow_wave = Sin(
        config=GeneratorConfig(amplitude=0.5, frequency=0.1)
    )

    sig_chain = SignalChain([base])
    sig_chain.process()

    plt.plot(sig_chain.x, sig_chain.processed_signal)
    plt.show()


if __name__ == "__main__":
    main()
