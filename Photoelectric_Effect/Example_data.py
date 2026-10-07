# Use data acquired on 07/17/23
# First order:
# Yellow: 0.730, 0.725, 0.723
# Green: 0.838, 0.834, 0.834
# Blue: 1.436, 1.438, 1.438
# Violet: 1.578, 1.579, 1.580
# UV: 1.795, 1.794, 1.798
#
# Second order:
# Yellow: 0.627
# Green: 0.720
# Blue: 1.385
# Violet: 1.508
# UV: 1.753

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a*x+b

c = 299792458.0
h = 6.62607015e-34
e = 1.602e-19

first_order = np.array([0.730, 0.838, 1.436, 1.578, 1.795])
second_order = np.array([0.627, 0.720, 1.385, 1.508, 1.753])

wavelengths = np.array([578.0e-9, 546.1e-9, 435.8e-9, 404.7e-9, 365.5e-9])
freq = c/wavelengths

popt1, pcov1 = curve_fit(func, freq, first_order)
perr1 = np.sqrt(np.diag(pcov1))
popt2, pcov2 = curve_fit(func, freq, second_order)
perr2 = np.sqrt(np.diag(pcov2))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.scatter(freq, first_order)
ax1.plot(freq, popt1[1]+popt1[0]*freq)

ax2 = fig.add_subplot(122)
ax2.scatter(freq, second_order)
ax2.plot(freq, popt2[1]+popt2[0]*freq)

print(f'The work function for the first order is {popt1[1]*e:.3e} +/- {perr1[1]*e:.3e}')
print(f'Planck constant for the first order is {popt1[0]*e:.3e} +/- {perr1[0]*e:.3e}')
print(f'The work function for the second order is {popt2[1]:.3e} +/- {perr2[1]*e:.3e}')
print(f'Planck constant for the second order is {popt2[0]*e:.3e} +/- {perr2[0]*e:.3e}')

plt.show()
