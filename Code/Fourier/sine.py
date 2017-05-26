import numpy as np
import matplotlib.pyplot as plt
import math

srate = 500
freq = [3, 10, 5, 15, 35]
amplitude = [5, 15, 10, 5, 7]
phases = [math.pi/7, math.pi/8, math.pi, math.pi/2, -math.pi/4]
time = np.arange(-1, 1, 1/srate)

sine_wave = np.zeros((len(freq), len(time)))

i = 0
while i < len(freq):
    sine_wave[i:][:] = amplitude[i] * np.sin(2 * math.pi * freq[i] * time + phases[i])
    i += 1

plt.plot(sum(sine_wave))
plt.suptitle('Sum of sine waves')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.show()
