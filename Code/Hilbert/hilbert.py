import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

time = np.arange(0, 1, 0.001)
cosine = np.cos(2 * math.pi * 5 * time)

plt.plot(time, cosine)
plt.plot(time, signal.hilbert(cosine).imag)
plt.plot(time, signal.hilbert(cosine).real)
plt.plot(time, np.angle(signal.hilbert(cosine)))
plt.show()

# generate random numbers
n = 21
randomnums = np.random.randn(n, 1)
print(randomnums)

# compute fourier transform
fourier = np.fft.fft(randomnums)
print(fourier)
complexfourier = fourier * 1j

# find positive and negative frequencies
positive = np.arange(1, math.floor(n/2) + n%2)
negative = np.arange(math.ceil(n/2) + 1 + ~(n%2), n)

# rotate fourier coefficients
fourier[positive] = fourier[positive] + -1j * complexfourier[positive]
fourier[negative] = fourier[negative] + 1j * complexfourier[negative]

# find inverse fft
hilbert_fourier = np.fft.ifft(fourier)
hilbert_sci = signal.hilbert(randomnums)

plt.plot(np.angle(hilbert_fourier))
plt.plot(np.angle(hilbert_sci))
plt.show()
