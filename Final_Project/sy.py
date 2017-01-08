# -*- coding: utf-8 -*-
"""
Created on Sat Jan 07 21:35:02 2017

@author: lenovo
"""

import numpy as np 
from matplotlib import pyplot as plt 
from matplotlib import animation 


steps=1000

ssteps = np.linspace(0, steps, steps+1)
x1 = np.zeros(steps)
y1 = np.zeros(steps)

for i in range(1,steps):
    r = np.random.rand()
    if (r < 0.25):             
        x1[i] = x1[i-1] + 1
        y1[i] = y1[i-1]
    elif (0.25 <= r < 0.5):
        x1[i] = x1[i-1] - 1
        y1[i] = y1[i-1]
    elif (0.5 <= r < 0.75):
        x1[i] = x1[i-1] 
        y1[i] = y1[i-1] + 1
    else:
        x1[i] = x1[i-1] 
        y1[i] = y1[i-1] - 1



fig = plt.figure() 
ax = plt.subplot(xlim=(-20, 20), ylim=(-20, 20)) 
line, = ax.plot([],[],'o') 
 
def init(): 
  line.set_data([], []) 
  return line, 
 
def animate(i): 
  x =x1[i] 
  y =y1[i]
  line.set_data(x, y) 
  return line, 

anim = animation.FuncAnimation(fig, animate, init_func=init, 
                frames=200, interval=200, blit=True) 
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Random walk in 2-dimension')
plt.show() 