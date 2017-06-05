import numpy as np
import matplotlib.pyplot as plt
import math

# variables
time = np.arange(-1, 1, 1/1000)
num_wavelets = 5
lowest_frequency = 2
highest_frequency = 30

# frequencies of our wavelets
frequencies = np.linspace(lowest_frequency, highest_frequency, num_wavelets)

# array to hold data of wavelets
morlet_family = np.zeros((num_wavelets, len(time)))

# loop to iterate through and create each wavelet
i = 0
while (i < num_wavelets):
    # create sine wave
    sine = np.sin(2 * math.pi * frequencies[i] * time)
    # create gaussian wave
    s = num_wavelets/(2 * math.pi * frequencies[i])
    gaussian = np.exp(-time**2/(2*s**2))
    # convolve them
    morlet_family[i][:] = sine * gaussian
    # plot each morlet wavelet
    plt.plot(time, morlet_family[i])
    # increment counter
    i += 1

plt.legend(['2 Hz', '9 Hz', '16 Hz', '23 4Hz', '30 Hz'], loc = "upper right")
plt.show()
