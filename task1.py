from typing import Tuple


import numpy as np


from pulse import Pulse

# CONSTANT DEFINITION
SAMPLING_RATE = 5898.24E6
NS_UNIT = 1E-9
MHZ_UNIT = 1E6

def generate_waveform(pulse: Pulse) -> Tuple(np.ndarray, np.ndarray):
    """This function generates a waveform array and time sampling point for the given pulse.
    """
    pass

if __name__ == "__main__":

    generate_waveform(Pulse(
        start=0,
        duration=50 * NS_UNIT,
        frequency=50 * MHZ_UNIT,
        amplitude=1,
        phase = 0
    ))
