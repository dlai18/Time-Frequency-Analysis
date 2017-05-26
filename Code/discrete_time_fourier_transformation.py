import numpy as np
import matplotlib.pyplot as plt
import math

srate = 1000
speriod = 1/srate
length_of_signal = 1500
time = np.arange(0, length_of_signal, speriod)

sine = 0.7 * np.sin(2 * math.pi * 50 * time) + np.sin(2 * math.pi * 120 * time)

noise = sine + 2 * np.random.randn(len(time))

plt.plot(1000 * time[0:50], noise[0:50])
plt.show()

fourier = fft(noise)
P2 = abs(fourier/length_of_signal)
P1 = P2[0:length_of_signal/2 + 1]
P1[2:end-1] = 2*P1[2:end-1]
f = srate*[0:length_of_signal/2]/length_of_signal
plt.plot(f, P1)
plt.show()
