# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as py
class hyperion:
    def __init__(self,theta0,vyc):
        self.gm=4*math.pi**2
        self.xc=[1]
        self.yc=[0]
        self.theta=[theta0]
        self.omega=[0]
        self.vxc=[0]
        self.vyc=[vyc]
        self.dt=0.0001
        self.t=[0]
        
    def run(self):
        while self.t[-1]<=20:
            r=math.sqrt((self.xc[-1])**2+(self.yc[-1])**2)
            vxc_new=self.vxc[-1]-self.gm*self.xc[-1]*self.dt/r**3
            vyc_new=self.vyc[-1]-self.gm*self.yc[-1]*self.dt/r**3
            omega_new=self.omega[-1]-12*(math.pi**2)*(self.xc[-1]*math.sin(self.theta[-1])-self.yc[-1]*math.cos(self.theta[-1]))*(self.xc[-1]*math.cos(self.theta[-1])+self.yc[-1]*math.sin(self.theta[-1]))*self.dt/r**5
    
            self.vxc.append(vxc_new)
            self.vyc.append(vyc_new)
            self.omega.append(omega_new)
    
            self.xc.append(self.xc[-1]+self.vxc[-1]*self.dt)
            self.yc.append(self.yc[-1]+self.vyc[-1]*self.dt)
    
            theta_new=self.theta[-1]+self.omega[-1]*self.dt

  
            while theta_new > math.pi:
                theta_new -=2*(math.pi)
            while theta_new < -math.pi:
                theta_new +=2*(math.pi)
  

            self.theta.append(theta_new)
            self.t.append(self.t[-1]+self.dt)
        
    def plot1(self):
        py.plot(self.t,self.theta,'y')
        py.xlim(0,20)
        py.title(r'Hyperion $\theta$ versus time')
        py.xlabel('time(yr)')
        py.ylabel(r'$\theta$(radians)')
        py.show
        
    def plot2(self):
        py.plot(self.t,self.omega,'r')
        py.xlim(0,10)
        py.title(r'Hyperion $\omega$ versus time')
        py.xlabel('time(yr)')
        py.ylabel('$\omega$(radians/yr)')
        py.show
    
    def plot3(self):
        py.scatter(self.theta,self.omega,s=0.01)
        py.xlim(-4,4)
        py.title(r'Hyperion $\omega$ versus $\theta$')
        py.xlabel(r'$\theta$(radians)')
        py.ylabel(r'$\omega$(radians/yr)')
        py.show
        
A=hyperion(0,5)
A.run()
A.plot1()
A.plot2()
A.plot3()


