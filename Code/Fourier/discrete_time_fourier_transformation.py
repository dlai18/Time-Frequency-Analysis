import numpy as np
import matplotlib.pyplot as plt
import math

# variables
srate = 1000                # sampling rate
speriod = 1/srate           # sampling period
length_of_signal = 1500
time = np.arange(0, length_of_signal, speriod) * speriod

# complex sine wave
sine = 0.7 * np.sin(2 * math.pi * 50 * time)
       + np.sin(2 * math.pi * 120 * time)

# add noise to sine wave
noise = sine + 2 * np.random.randn(len(time))

plt.plot(1000*time[0:49], noise[0:49])
plt.show()

fourier = np.fft.fft(noise)        # fourier transform
P2 = abs(fourier/length_of_signal) # two sided power spectrum
P1 = P2[0:length_of_signal/2 + 1]  # one sided power spectrum
P1[1:-2] = 2 * P1[1:-2]

f = srate * np.arange(0, length_of_signal/2 + 1)/length_of_signal

plt.plot(f, P1)
plt.show()
