# -*- coding: utf-8 -*-

import pylab as pl
import numpy
import random
class trajectories(object):
    def __init__(self, v_0 = 2, time_step = 0.1, g = 0.0098, v_wind = 10.0 / 3600, distance_from_target = 100):
        # units of time and ditance are s and km
        self.vx = []
        self.vy = []
        self.v_0 = v_0
        self.x = []
        self.y = []
        self.g = g
        self.dt = time_step
        self.target = distance_from_target
        self.v_wind = v_wind
        self.s = []
        self.angle = []
        
    def calculate(self):
        R = 6371
        B = 0.04
        a = 6.5
        alpha = 2.5
        T_0 = 300
        for i in numpy.arange(0,90,0.1):
            self.x.append([0])
            self.y.append([0])
            self.vx.append([self.v_0 * numpy.cos((float(i) / 180) * numpy.pi)])
            self.vy.append([self.v_0 * numpy.sin((float(i) / 180) * numpy.pi)])
            while (self.y[-1][-1] > 0) or (self.x[-1][-1] == 0):
                v = numpy.sqrt(abs(self.vx[-1][-1] - self.v_wind) ** 2 + (self.vy[-1][-1]) ** 2)
                self.x[-1].append(self.x[-1][-1] + self.vx[-1][-1] * self.dt)
                self.y[-1].append(self.y[-1][-1] + self.vy[-1][-1] * self.dt)
                self.vx[-1].append(self.vx[-1][-1] - ((1 - a * self.y[-1][-1] / T_0) ** alpha) * B * v * (self.vx[-1][-1] - self.v_wind) * self.dt)
                self.vy[-1].append(self.vy[-1][-1] - (self.g * ((float(R) / (R + self.y[-1][-1])) ** 2) + ((1 - a * self.y[-1][-1] / T_0) ** alpha) * B * v * self.vy[-1][-1]) * self.dt)
            if self.y[-1][-1] < 0:
                r = - (self.y[-1][-2] / self.y[-1][-1])
                self.x[-1][-1] = (self.x[-1][-2] + r * self.x[-1][-1]) / (r + 1)  
            self.s.append(abs(self.target-self.x[-1][-1]))    
        for i in numpy.arange(0,90,0.1):
            if self.s[int(i*10)] == min(self.s):
                print i
                print self.x[int(i*10)][-1]
                self.angle.append(i)
           
    def show_results(self):
        for i in numpy.arange(0,90,0.1):
            if self.s[int(i*10)] == min(self.s):
                pl.plot(self.x[int(i*10)], self.y[int(i*10)])
        pl.title('Trajectory of cannon shell')
        pl.annotate(r'$v_0$=%.2f$km/s$'%self.v_0,xy=(8,10))
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.ylim(0,)
        pl.show()     
 
    def with_deviations(self):
        R = 6371
        B = 0.04
        a = 6.5
        alpha = 2.5
        T_0 = 300
        self.vx = []
        self.vy = []
        self.x = []
        self.y = []
        self.v_0 = [self.v_0]
        self.v_wind = [self.v_wind]
        self.s = []
        for i in range(100):
            self.v_0.append(self.v_0[0] * random.uniform(0.95,1.05))
            self.v_wind.append(self.v_wind[0] * random.uniform(0.9,1.1))
            self.angle.append(self.angle[0]+random.uniform(-2,2))
            self.x.append([0])
            self.y.append([0])
            self.vx.append([self.v_0[-1] * numpy.cos((float(self.angle[-1]) / 180) * numpy.pi)])
            self.vy.append([self.v_0[-1] * numpy.sin((float(self.angle[-1]) / 180) * numpy.pi)])
            while (self.y[-1][-1] > 0) or (self.x[-1][-1] == 0):
                v = numpy.sqrt((self.vx[-1][-1] - self.v_wind[-1]) ** 2 + (self.vy[-1][-1]) ** 2)
                self.x[-1].append(self.x[-1][-1] + self.vx[-1][-1] * self.dt)
                self.y[-1].append(self.y[-1][-1] + self.vy[-1][-1] * self.dt)
                self.vx[-1].append(self.vx[-1][-1] - ((1 - a * self.y[-1][-1] / T_0) ** alpha) * B * v * (self.vx[-1][-1] - self.v_wind[-1]) * self.dt)
                self.vy[-1].append(self.vy[-1][-1] - (self.g * ((float(R) / (R + self.y[-1][-1])) ** 2) + ((1 - a * self.y[-1][-1] / T_0) ** alpha) * B * v * self.vy[-1][-1]) * self.dt)
            if self.y[-1][-1] < 0:
                r = - (self.y[-1][-2] / self.y[-1][-1])
                self.x[-1][-1] = (self.x[-1][-2] + r * self.x[-1][-1]) / (r + 1)  
            self.s.append(abs(self.target-self.x[-1][-1]))
        for i in range(100):
            pl.plot(self.x[i], self.y[i])
        pl.title('Trajectory of cannon shell with deviations')
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.ylim(0,)
        pl.show()
        a = 0
        for i in range(100):
            a = a + self.s[i] ** 2
        s_2 = float(a) / 100
        x = [0, 100]
        y = [100, 100]
        pl.plot(x, y, 'r', linewidth = 2)
        for i in range(100):
            pl.plot(i + 1, self.x[i][-1], 'bo')
        pl.annotate(r'$s^{2}=$%.2f'%s_2,xy=(80,70))
        pl.title('result of n experimentations')
        pl.xlabel('order numbers of experimentations')
        pl.ylabel('$x_{l}(km)$')
        pl.xlim(0,100)
        pl.ylim(60, 140)
        pl.show()
   
        
a = trajectories()
a.calculate()
a.show_results()
a.with_deviations()