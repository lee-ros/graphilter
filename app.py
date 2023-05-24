import numpy as np
import matplotlib.pyplot as plt

from graphilter import (
    generators,
    filters,
    utils,
)


def main():
    # base = generators.Sawtooth(end=5, f_s=1000)

    base = generators.Cos(start=-10 * np.pi, end=10 * np.pi, f_s=5000)
    noise = generators.Sin(
        config=generators.GeneratorConfig(amplitude=0.1, frequency=50, phase=np.pi),
    )
    slow_wave = generators.Sin(
        config=generators.GeneratorConfig(amplitude=0.5, frequency=0.1)
    )
    
    median = filters.Median(window_size=25)
    mean = filters.Mean(window_size=25)

    sig_chain = utils.SignalChain([base, noise, median, mean])
    sig_chain.process()

    plt.plot(sig_chain.x, sig_chain.processed_signal)
    plt.show()


if __name__ == "__main__":
    main()
