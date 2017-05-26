import numpy as np
import matplotlib.pyplot as plt

signal = np.zeros(100)
signal[40:60] = 1
kernel = [1, 0.8, 0.6, 0.4, 0.2]
convolution = np.convolve(signal, kernel, 'same')

plt.plot(convolution)
plt.show()
