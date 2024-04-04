Here I have included a basic pulse object and pulse synthesis into samples

Some sample tasks you could do are

1. Define a function that takes a Pulse object and outputs the waveform array and time array. This function should take care if the pulse start times and duration do not align with the sampling rate.
2. Using the function from task 1, test and ensure that multiple pulses are aligned with each other.
3. A device is usually limited in playback memory, adjust your function in task 1 such that the waveform array is added into a memory buffer at the correct position.
