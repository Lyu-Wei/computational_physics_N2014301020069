# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
GM=4*(math.pi**2)
perihelion=0.39*(1-0.206)
class orbits(object):
    def __init__(self,e=0.206,time=5,dt=0.0001,vcoefficient=1,beta=2,alpha=0.01):
        self.alpha=alpha
        self.beta=beta
        self.vcoefficient=vcoefficient
        self.e=e
        self.a=perihelion/(1-e)
        self.x0=self.a*(1+e)
        self.y0=0
        self.vx0=0
        self.vy0=self.vcoefficient*math.sqrt((GM*(1-e))/(self.a*(1+e)))
        self.X=[self.x0]
        self.Y=[self.y0]
        self.Vx=[self.vx0]
        self.Vy=[self.vy0]
        self.T=[0]
        self.dt=dt
        self.time=time
        self.ThetaPrecession=[]
        self.TimePrecession=[]
        
    def calculate(self):
        while self.T[-1]<self.time:
            r=math.sqrt(self.X[-1]**2+self.Y[-1]**2)
            newVx=self.Vx[-1]-(GM*(1+self.alpha/r**2)*self.X[-1]/r**(1+self.beta))*self.dt
            newX=self.X[-1]+newVx*self.dt
            newVy=self.Vy[-1]-(GM*(1+self.alpha/r**2)*self.Y[-1]/r**(1+self.beta))*self.dt
            newY=self.Y[-1]+newVy*self.dt
            if abs(newX*newVx+newY*newVy)<0.0014 and r<self.a:
                theta=math.acos(self.X[-1]/r)*180/math.pi
                if (self.Y[-1]/r)<0:
                    theta=360-theta
                theta=abs(theta-180)
                self.ThetaPrecession.append(theta)
                self.TimePrecession.append(self.T[-1])
            self.Vx.append(newVx)
            self.Vy.append(newVy)
            self.X.append(newX)
            self.Y.append(newY)
            self.T.append(self.T[-1]+self.dt)
        
    def show_results(self):
        p1,=plt.plot(self.X,self.Y)
        plt.legend([p1],['t=T'],loc='upper right',frameon=False)
        plt.grid(True)
        plt.title('Simulation of the precession of Mercury')
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.xlim(-0.6,0.6)
        plt.ylim(-0.6,0.6)
        plt.scatter(0,0)
        plt.show()
        
    def orientation(self):
        p2,=plt.plot(self.TimePrecession,self.ThetaPrecession,'g.-')
        plt.legend([p2],[r''],loc='upper left',frameon=False)
        plt.xlabel('time(yr)')
        plt.ylabel(r'$\theta$(degrees)')
        plt.ylim(0,20)
        plt.title('Orbit orentation versus time')
        
        plt.show()
        
        
a=orbits()
a.calculate()
a.show_results()
a.orientation()