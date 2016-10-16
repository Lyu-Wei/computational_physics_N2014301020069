# -*- coding: utf-8 -*-

import pylab as pl
import math
class trajectories(object):
    def __init__(self, v_0 = 0.7, time_step = 0.5, g = 0.0098):
        self.vx = []
        self.vy = []
        self.v_0 = v_0
        self.x = []
        self.y = []
        self.t = [0]
        self.g = g
        self.angle = [30, 35, 40, 45, 50, 55]
        self.dt = time_step
    def calculate(self):
        for i in self.angle:
            self.x.append([0])
            self.y.append([0])
            self.vx.append([self.v_0 * math.cos((float(i) / 180) * math.pi)])
            self.vy.append([self.v_0 * math.sin((float(i) / 180) * math.pi)])
            while (self.y[-1][-1] > 0) or (self.x[-1][-1] == 0):
                self.vx[-1].append(self.vx[-1][-1])
                self.vy[-1].append(self.vy[-1][-1] - self.g * self.dt)
                self.x[-1].append(self.x[-1][-1] + self.vx[-1][-1] * self.dt)
                self.y[-1].append(self.y[-1][-1] + self.vy[-1][-1] * self.dt)
            if self.y[-1][-1] < 0:
                r = - (self.y[-1][-2] / self.y[-1][-1])
                self.x[-1][-1] = (self.x[-1][-2] + r * self.x[-1][-1]) / (r + 1)  
    def show_results(self):
        for i in range(len(self.angle)):
            pl.plot(self.x[i], self.y[i])
            pl.annotate(r'%d$^o$'%self.angle[i],xy=(20, 2 * i + 7))
        pl.title('Trajectory of cannon shell (no drag)')
        pl.annotate(r'$v_0$=%.2f$km/s$'%self.v_0,xy=(45,15))
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.xlim(0, 60)
        pl.ylim(0, 20)
        pl.show()
a = trajectories()
a.calculate()
a.show_results()
        
class exact_results_check(trajectories):
    def show_results(self):
        self.etx = []
        self.ety = []
        for i in self.angle:
            self.etx.append([0])
            self.ety.append([0])
            while (self.ety[-1][-1] > 0) or (self.etx[-1][-1] == 0):
                self.etx[-1].append(self.v_0 * math.cos((float(i) / 180) * math.pi) * self.dt * len(self.etx[-1]))
                self.ety[-1].append(self.v_0 * math.sin((float(i) / 180) * math.pi) * self.dt * len(self.etx[-1]) - 0.5 * self.g * (self.dt * len(self.ety[-1])) ** 2 )
            if self.ety[-1][-1] < 0:
                r1 = - (self.ety[-1][-2] / self.ety[-1][-1])
                self.etx[-1][-1] = (self.etx[-1][-2] + r1 * self.etx[-1][-1]) / (r1 + 1)
        for i in range(len(self.angle)):
            p1, = pl.plot(self.x[i], self.y[i])
            pl.annotate(r'%d$^o$'%self.angle[i],xy=(20, 2 * i + 7))
        for i in range(len(self.angle)):
            p2, = pl.plot(self.etx[i], self.ety[i],'--')
        pl.title('Trajectory of cannon shell (no drag)')
        pl.annotate(r'$v_0$=%.2f$km/s$'%self.v_0,xy=(2,15))
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.xlim(0, 60)
        pl.ylim(0, 20)
        pl.legend([p1, p2], ['numerical solutions', 'analytic solutions '], loc="best")
        pl.show()
        
b = exact_results_check()
b.calculate()
b.show_results()        