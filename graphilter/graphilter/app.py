import numpy as np
import matplotlib.pyplot as plt

from graphilter.generators import Cos, Sin, GeneratorConfig
from graphilter.utils import SignalChain

def main():
    base = Cos(start=-10 * np.pi, end=10 * np.pi, step=5000)
    noise = Sin(
        base_signal=base,
        config=GeneratorConfig(
            outer_coeff=0.1, inner_coeff=20, inner_offset=np.pi    
        )
    )
    slow_wave = Sin(
        base_signal=noise,
        config=GeneratorConfig(
            outer_coeff=0.5, inner_coeff=0.1
        )
    )
    
    sig_chain = SignalChain([base, noise, slow_wave])
    sig_chain.process()


    plt.plot(sig_chain.x, sig_chain.processed_signal)
    plt.show()


if __name__ == "__main__":
    main()
