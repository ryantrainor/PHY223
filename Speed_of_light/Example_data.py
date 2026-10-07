# Use data acquired on 07/17/23
# Frequency of source is 3.975 MHz.
# A full period is 252 ns. 
# Distance (m) | delay (ns)
# 3.18 | -80
# 5.01 | -74
# 6.41 | -70
# 7.85 | -66
# 9.23 | -62
# 10.95 | -56
# 12.87 | -32 (Not sure what happened here. Maybe I bounced the light off the floor.)
# 14.73 | -46
# 16.55 | -40
# 18.37 | -34
# 21.09 | -26

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a*x+b

distance = np.array([3.18, 5.01, 6.41, 7.85, 9.23, 10.95, 14.73, 16.55, 18.37, 21.09])
dt = np.array([-80., -74., -70., -66., -62., -56., -46., -40., -34., -26.])*1e-9

popt, pcov = curve_fit(func, dt, distance)
perr = np.sqrt(np.diag(pcov))

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(dt, distance)
ax1.plot(dt, popt[1]+popt[0]*dt)

print(f'The speed of light is {popt[0]:.3e} +\- {perr[0]:.3e}')

plt.show()
