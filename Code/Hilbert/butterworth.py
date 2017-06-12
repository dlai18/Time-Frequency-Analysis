import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

center_frequency = 10
nyquist = 500

# create sine wave
time = np.arange(-1, 1, 1/1000)
sine_wave = np.cos(2 * math.pi * center_frequency * time) * np.exp(-time**2/(2*(3/(2* math.pi * center_frequency))**2))

frequency_spread = 4
transwid = 0.10

# construct filter kernel
ffrequencies = [0, ((1-transwid) * (center_frequency - frequency_spread))/nyquist, (center_frequency - frequency_spread)/nyquist, (center_frequency + frequency_spread)/nyquist, ((1 + transwid) * (center_frequency + frequency_spread))/nyquist, nyquist/nyquist]
ideal = [0, 0, 1, 1, 0, 0]
filterweights = signal.firls(251, ffrequencies, ideal)

forward_filt = signal.lfilter(filterweights, 1, sine_wave)
reverse_filt = signal.lfilter(filterweights, 1, forward_filt[-1:])
final_filt_result = reverse_filt[-1:]

plt.plot(sine_wave)
plt.plot(forward_filt)
plt.plot(reverse_filt)
plt.show()

# butterworth filter
b, a = signal.butter(5, [(center_frequency - 6)/nyquist, (center_frequency + 6)/nyquist], 'bandpass')
butter_filter = signal.filtfilt(b, a, sine_wave)

plt.plot(time, butter_filter)
plt.show()
