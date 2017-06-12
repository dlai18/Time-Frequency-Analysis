import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

# variables for sine wave
srate = 1000                # sampling rate
speriod = 1/srate           # sampling period
length_of_signal = 1500
time = np.arange(0, length_of_signal, speriod) * speriod

# complex sine wave
sine = np.sin(2 * math.pi * 50 * time) + np.sin(2 * math.pi * 120 * time)

# add noise to sine wave
noise = sine + 2 * np.random.randn(len(time))

plt.plot(1000*time[0:500], noise[0:500])
plt.plot(time, sine)

# variables for filter
center_frequency = 10
frequency_spread = 4
transwid = .10
nyquist = 500

# vector of frequencies that define the shape of the response
ffrequencies = [0, ((1 - transwid) * (center_frequency - frequency_spread))/nyquist, (center_frequency - frequency_spread)/nyquist, (center_frequency + frequency_spread)/nyquist, ((1 + transwid) * (center_frequency + frequency_spread))/nyquist, nyquist/nyquist]

# ideal filter response amplitude
ideal = [0, 0, 1, 1, 0, 0]

# create kernel filter
filterweights = signal.firls(201, ffrequencies, ideal)

# apply filter to data
filter_result = signal.filtfilt(filterweights, 1, noise)

# convolve the data with the filter
convolve_result = np.convolve(noise, filterweights, 'same')

plt.plot(1000*time[0:500], convolve_result[0:500], 'r')
plt.legend(['noise', 'sine', 'filtered'], loc='upper right')
plt.show()
