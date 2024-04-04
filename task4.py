from typing import List, Tuple


import numpy as np
import matplotlib.pyplot as plt


from dataclasses import dataclass
from pulse import Pulse

SAMPLES_PER_ADDRESS = 16
NUM_SAMPLES = 131072
SAMPLING_RATE = 5898.24E6

@dataclass
class JumpRegister:
    repeat: int
    from_address: int
    to_address: int

def render(waveform: np.ndarray, registers: List[JumpRegister]) -> np.ndarray:

    """Renders the waveform playback with the jump register logic

    Arguments:
        waveform (np.ndarray): Numpy array containing waveform samples
        registers (JumpRegisters[]): Array of jump registers

    Returns:
        waveform_output (np.ndarray): Numpy array containing true DAC output
    """

    num_address = len(waveform) << 4
    address_map = waveform.reshape((num_address, SAMPLES_PER_ADDRESS))
    output = np.array([])

    address = 0
    while address < num_address:

        output = np.concatenate((output, address_map[address]))
        
        # Add jump register logic here

        address += 1

    return output

def waveform_generation(sequence: List[Pulse]) -> Tuple[np.ndarray, List[JumpRegister]]:
    """Synthesizes the given sequence of pulses into a numpy array and jump registers if needed.
    """
    pass

if __name__ == "__main__":

    sequence = [
        Pulse(0, 5000, 1, 100e6, 0, "Rectangular", 1),
        Pulse(20000, 5000, 1, 100e6, 0, "Rectangular", 1),
        Pulse(40000, 5000, 1, 100e6, 0, "Rectangular", 1)
    ]

    waveform, regs = waveform_generation(sequence)
    output = render(waveform, regs)
    time_array = np.arange(len(output)) / SAMPLING_RATE * 1E9

    plt.scatter(time_array, waveform)
    plt.grid()
    plt.xlabel("TIme [ns]")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
