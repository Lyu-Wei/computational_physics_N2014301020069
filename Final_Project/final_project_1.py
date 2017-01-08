# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


steps = np.linspace(0, 100, 101)
y0 = np.zeros(101)
x1 = np.zeros(101)
x2 = np.zeros(101)

for i in range(1,101):
    r = np.random.rand()
    if r<0.75:
        x1[i] = x1[i-1] + 1
    else:
        x1[i] = x1[i-1] - 1
       
for i in range(1,101):
    r = np.random.rand()
    if r<0.75:
        x2[i] = x2[i-1] + 1
    else:
        x2[i] = x2[i-1] - 1



 


plt.scatter(steps, x1,c='y')
plt.scatter(steps, x2,c='g')
plt.plot(steps, y0)
plt.xlim(0,100)
#plt.ylim(-40, 40)
plt.grid(True)
plt.xlabel('step number')
plt.ylabel('x')
plt.title('Random walk in one dimension')
plt.annotate('Inequle probability', xy=(20, 5))

plt.show()

