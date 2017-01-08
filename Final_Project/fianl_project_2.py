# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
xave = np.zeros(101)

x = np.zeros(10000)

for j in range(101):
    for i in range(10000):
        r = np.random.rand()
        if r<0.75:
            x[i] = x[i] + 1
        else:
            x[i] = x[i] - 1
    xave[j] = sum(x)/10000

a = np.polyfit(steps, xave,1)
poly = np.poly1d(a)
fit = poly(steps)
    
plt.plot(steps, xave, '.')
plt.plot(steps, fit)
plt.xlim(0,100)
#plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number (= time)')
plt.ylabel('<x>')
plt.title('Random walk in one dimension')
plt.annotate('<x> versus time   10000 walkers', xy=(20, 0.5))
plt.annotate('Inequle probability', xy=(20, 10))
plt.show()

