from typing import Tuple


import numpy as np


from pulse import Pulse

# CONSTANT DEFINITION
SAMPLING_RATE = 5898.24E6
NS_UNIT = 1E-9
MHZ_UNIT = 1E6
MAX_SAMPLES = 65536


buffer = np.zeros(MAX_SAMPLES)
pulses = [
    Pulse(start=0, duration=50e-9, frequency=50e6, amplitude=1, phase=0),
    Pulse(start=50e-9, duration=50e-9, frequency=50e6, amplitude=1, phase=0),
    Pulse(start=1e-6, duration=50e-9, frequency=50e6, amplitude=1, phase=0)
]

for pulse in pulses:
    #buffer =
    pass
