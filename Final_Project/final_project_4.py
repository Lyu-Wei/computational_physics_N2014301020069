# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation



class random_walk_2D (object):
     def __init__(self, steps,particle_num):
         self.step_num = steps
         self.particle_num = particle_num
         self.steps = np.linspace(0, steps, steps+1)
         self.x1 = np.zeros(steps)
         self.y1 = np.zeros(steps)
         self.p_x = np.zeros(particle_num) 
         self.p_y = np.zeros(particle_num)
         
     def calculate1 (self):
         for i in range(1,self.step_num):
             r = np.random.rand()
             if (r < 0.25):             
                 self.x1[i] = self.x1[i-1] + 1
                 self.y1[i] = self.y1[i-1]
             elif (0.25 <= r < 0.5):
                 self.x1[i] = self.x1[i-1] - 1
                 self.y1[i] = self.y1[i-1]
             elif (0.5 <= r < 0.75):
                 self.x1[i] = self.x1[i-1] 
                 self.y1[i] = self.y1[i-1] + 1
             else:
                 self.x1[i] = self.x1[i-1] 
                 self.y1[i] = self.y1[i-1] - 1
            
    
     def show_results1 (self):
         #plt.scatter(self.x1, self.y1)
         #plt.scatter(steps, x2,c='r')
         plt.plot(self.x1, self.y1,'y')
         plt.scatter(0, 0, s = 50, c = 'k')
         plt.xlim(-100,100)
         plt.ylim(-100,100)
         plt.grid(True)
         plt.xlabel('x')
         plt.ylabel('y')
         plt.title('Random walk in 2-dimension')
        
         plt.show()
         
     def calculate2 (self):
         for j in range(self.step_num):
             for i in range(self.particle_num):
                 r = np.random.rand()
                 if (r < 0.25):             
                     self.p_x[i] = self.p_x[i] + 1
                     self.p_y[i] = self.p_y[i]
                 elif (0.25 <= r < 0.5):
                     self.p_x[i] = self.p_x[i] - 1
                     self.p_y[i] = self.p_y[i]
                 elif (0.5 <= r < 0.75):
                     self.p_x[i] = self.p_x[i] 
                     self.p_y[i] = self.p_y[i] + 1
                 else:
                     self.p_x[i] = self.p_x[i] 
                     self.p_y[i] = self.p_y[i] - 1

     def show_results2 (self):
         plt.scatter(self.p_x, self.p_y)
         #plt.scatter(steps, x2,c='r')
         #plt.plot(self.x1, self.y1, 'r')
         #plt.scatter(0, 0, s = 50, c = 'r')
         plt.xlim(-300,300)
         plt.ylim(-200,200)
         plt.grid(True)
         plt.xlabel('x')
         plt.ylabel('y')
         plt.title('Diffusion in 2D')
         plt.annotate('t=%.0f'%self.step_num, xy=(-200, 150))
         
         plt.show()
         
     def show_results3(self):
         fig = plt.figure() 
         ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20)) 
         line, = ax.plot([], [], '.') 
 
         def init(): 
             line.set_data([], []) 
             return line, 
             
         def animate(i): 
             x =i 
             y =i
             line.set_data(x, y) 
             return line, 
            
         animation.FuncAnimation(fig, animate, init_func=init, 
                            frames=200, interval=200, blit=True) 
            
         plt.show() 
         
a = random_walk_2D(100000, 100)
a.calculate1()
#a.show_results1()
a.calculate2()
a.show_results2()