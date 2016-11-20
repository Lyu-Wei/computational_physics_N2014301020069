# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
class billiard_circle(object):
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt,alpha):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
        self.alpha=alpha
    def calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (np.sqrt( self.x[i]**2+(self.y[i]-self.alpha)**2 ) > 1.0) and self.y[i]>self.alpha:
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y-self.alpha)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect1(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            elif (np.sqrt( self.x[i]**2+(self.y[i]+self.alpha)**2 ) > 1.0) and self.y[i]<-self.alpha:
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+(y+self.alpha)**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect2(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            elif (self.x[i] < -1.0) and self.y[i]>-self.alpha and self.y[i]<self.alpha:
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif (self.x[i] > 1.0) and self.y[i]>-self.alpha and self.y[i]<self.alpha:
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            self.t.append(self.t[i - 1] + self.dt)
              
        return self.x, self.y,self.t
        
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt    
    def reflect1(self,x,y,vx,vy):
        module = np.sqrt(x**2+(y-self.alpha)**2)  
        x = x/module
        y = (y-self.alpha)/module+self.alpha
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*(y-self.alpha))/v
        cos2 = (vx*(y-self.alpha)-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*(y-self.alpha)
        vy_n = vt*(y-self.alpha)-vc*x
        return vx_n,vy_n
    
    def reflect2(self,x,y,vx,vy):
        module = np.sqrt(x**2+(y+self.alpha)**2)  
        x = x/module
        y = (y+self.alpha)/module-self.alpha
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*(y+self.alpha))/v
        cos2 = (vx*(y+self.alpha)-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*(y+self.alpha)
        vy_n = vt*(y+self.alpha)-vc*x
        return vx_n,vy_n
        
sub1=plt.subplot(221)
A1=billiard_circle(0,0,1,0.6,4000,0.01,0)
x1,y1,t1=A1.calculate()
A2=billiard_circle(0.00001,0,1,0.6,4000,0.01,0)
x2,y2,t2=A2.calculate()
delta=[]
for i in range(len(x1)):
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2)
sub1.semilogy(t1, x1)
sub1.set_title('$\\alpha=0$')
plt.xlabel('time')
plt.ylabel('separation')

sub2=plt.subplot(222)
A1=billiard_circle(0,0,1,0.6,4000,0.01,0.01)
x1,y1,t1=A1.calculate()
A2=billiard_circle(0.00001,0,1,0.6,4000,0.01,0.01)
x2,y2,t2=A2.calculate()
delta=[]
for i in range(len(x1)):
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2)
sub2.semilogy(t1, x1)
sub2.set_title('$\\alpha=0.01$')
plt.xlabel('time')
plt.ylabel('separation')

sub3=plt.subplot(223)
A1=billiard_circle(0,0,1,0.6,4000,0.01,0.1)
x1,y1,t1=A1.calculate()
A2=billiard_circle(0.00001,0,1,0.6,4000,0.01,0.1)
x2,y2,t2=A2.calculate()
delta=[]
for i in range(len(x1)):
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2)
sub3.semilogy(t1, x1)
sub3.set_title('$\\alpha=0.1$')
plt.xlabel('time')
plt.ylabel('separation')

sub4=plt.subplot(224)
A1=billiard_circle(0,0,1,0.6,4000,0.01,1)
x1,y1,t1=A1.calculate()
A2=billiard_circle(0.00001,0,1,0.6,4000,0.01,1)
x2,y2,t2=A2.calculate()
delta=[]
for i in range(len(x1)):
    x1[i]=np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2)
sub4.semilogy(t1, x1)
sub4.set_title('$\\alpha=1$')
plt.xlabel('time')
plt.ylabel('separation')