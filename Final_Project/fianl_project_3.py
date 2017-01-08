# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
n = 10000
steps = np.linspace(0, 100, 101)
x2ave = np.zeros(101)
x = np.zeros(n)
x_2 = np.zeros(n)

for j in range(1,101):
    for i in range(n):
        r = np.random.rand()
        if r<0.75:
            x[i] = x[i] + 1
        else:
            x[i] = x[i] - 1
        x_2[i] = x[i] ** 2    
    x2ave[j] = sum(x_2)/n

a = np.polyfit(steps, x2ave,2)
poly = np.poly1d(a)
fit = poly(steps)
    
plt.plot(steps, x2ave, '.')
plt.plot(steps, fit)
plt.xlim(0, 100)
#plt.ylim(0, 100)
plt.grid(True)
plt.xlabel('step number (= time)')
plt.ylabel(r'<$x^2$>')
plt.title('Random walk in one dimension')
plt.annotate(r'<$x^2$> versus time  10000 walkers', xy=(20, 1800))
plt.annotate('Inequle probability', xy=(20, 1700))

plt.show()

