import numpy as np
import matplotlib.pyplot as plt
import math

# variables
time = np.arange(-1, 1, 1/1000)
freq = 4

# create sine wave
sine = np.cos(2 * math.pi * freq * time)

# plot sine wave
plt.plot(time, sine)
plt.show()

# create Gausian wave
s= 4/(2 * math.pi * freq)
gaussian = np.exp(-time**2/(2*s**2))

# plot Gaussian wave
plt.plot(time, gaussian)
plt.show()

# plot Morlet wave
plt.plot(time, sine * gaussian)
plt.show()
