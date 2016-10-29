# Exercise_07

## 摘要

## 背景介绍

## 题目
* Problem 3.12.<br>
In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the force; that is, at times ![](http://latex.codecogs.com/gif.latex?t%5Capprox%202%5Cpi%20n/%5COmega%20_D), where n is an interger. At these values of t the driving force passed throught zero [see (3.8)]. However, we could just as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times ![](http://latex.codecogs.com/gif.latex?%5Cpi/4) out-of-phase with this force, etc. Construct the Poincaré sections for these cases and compare them with Figure 3.9.

* Problem 3.13.<br>
Write a program to calculate and compare the brhavior of two, nearly indentical pedulums. Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent from the slope of a plot of ![](http://latex.codecogs.com/gif.latex?log%28%5CDelta%20%5Ctheta%20%29) as a function of t.

* Problem 3.14.<br>
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent compare with that found in Figure 3.7?


## 正文
* 初始条件微小变化对结果的影响（problem 3.13）
  物理摆摆动过程中，当F_D较小时，初始值的微小变化对结果影响很小；若F_D较大，则混沌现象发生，初始值对结果影响巨大。下面我们同时摆动两个物理摆，它们除不一样外，其他参数都相同，它们的![]()-s 图如下：
  ![]()![]()
  为更好地表现结果，该图的纵坐标使用lg为刻度。整个程序代码如下：
```
# -*- coding: utf-8 -*-
import pylab as pl
import numpy as np

class pendulum(object):    
    def __init__(self, F_D, theta):
        #all units are in SI.
        self.theta = [theta]
        self.theta1 = [theta + 0.001]
        self.omega = [0]
        self.omega1 = [0]
        self.F_D = F_D
        self.t = [0]
        self.dt = 0.04
        self.delta_theta = [0.001]
        
    def calculate(self):
        l = 9.8
        g = 9.8
        q1 = 0.5
        q2 = 0.5
        self.omega_D = float(2)/3
        while(self.t[-1] < 150):
            temp1 = self.omega[-1] - ((g / l) * np.sin(self.theta[-1]) + q1 * self.omega[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega.append(temp1)
            temp2 = self.theta[-1] + temp1 * self.dt
            while(temp2 > np.pi):
                temp2 -= 2 * np.pi
            while(temp2 < -np.pi):
                temp2 += 2 * np.pi
            self.theta.append(temp2)
            
            temp3 = self.omega1[-1] - ((g / l) * np.sin(self.theta1[-1]) + q2 * self.omega1[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega1.append(temp3)
            temp4 = self.theta1[-1] + temp3 * self.dt 
            while(temp4 > np.pi):
                temp4 -= 2 * np.pi
            while(temp4 < -np.pi):
                temp4 += 2 * np.pi 
            self.theta1.append(temp4)
            
            self.t.append(self.t[-1] + self.dt)
            self.delta_theta.append(abs(self.theta[-1] - self.theta1[-1]))
             
    def show_results1(self):
        pl.semilogy(self.t, self.delta_theta)
        pl.title(r'$\Delta \theta$ versus time($F_D$=%.1f)'%self.F_D)
        pl.xlabel(r'time($s$)')
        pl.ylabel(r'$\Delta \theta$ (radians)')
        pl.show()
        
a=pendulum(1.2, 0.2)
a.calculate()
a.show_results1()
```

* 阻尼系数的微小改变对结果的影响（problem 3.14）
  如果我们让第二个摆的阻尼系数![]()改变，其他参数不变，结果如图：
  ![]()![]()![]()
  程序代码如下：
```
# -*- coding: utf-8 -*-
import pylab as pl
import numpy as np

class pendulum(object):    
    def __init__(self, F_D, theta):
        #all units are in SI.
        self.theta = [theta]
        self.theta1 = [theta + 0.001]
        self.omega = [0]
        self.omega1 = [0]
        self.F_D = F_D
        self.t = [0]
        self.dt = 0.04
        self.delta_theta = [0.001]
        
    def calculate(self):
        l = 9.8
        g = 9.8
        q1 = 0.5
        q2 = 0.6
        self.omega_D = float(2)/3
        while(self.t[-1] < 50):
            temp1 = self.omega[-1] - ((g / l) * np.sin(self.theta[-1]) + q1 * self.omega[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega.append(temp1)
            temp2 = self.theta[-1] + temp1 * self.dt
            while(temp2 > np.pi):
                temp2 -= 2 * np.pi
            while(temp2 < -np.pi):
                temp2 += 2 * np.pi
            self.theta.append(temp2)
            
            temp3 = self.omega1[-1] - ((g / l) * np.sin(self.theta1[-1]) + q2 * self.omega1[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega1.append(temp3)
            temp4 = self.theta1[-1] + temp3 * self.dt 
            while(temp4 > np.pi):
                temp4 -= 2 * np.pi
            while(temp4 < -np.pi):
                temp4 += 2 * np.pi 
            self.theta1.append(temp4)
            
            self.t.append(self.t[-1] + self.dt)
            self.delta_theta.append(abs(self.theta[-1] - self.theta1[-1]))
            
    def show_results1(self):
        p, = pl.semilogy(self.t, self.delta_theta)
        pl.title(r'$\Delta \theta$ versus time($F_D$=%.1f)'%self.F_D)
        pl.xlabel(r'time($s$)')
        pl.ylabel(r'$\Delta \theta$ (radians)')
        pl.legend([p],['$\Delta$q=0.1'],loc='best')
        pl.show()
        
a=pendulum(0.5, 0.2)
a.calculate()
a.show_results1()
```
  
* 空间相位图
In the section(3), we have talked what is chaos and we have already known that the trajectory of chaos is hard to predict. But it is not all right. In fact, if we plot \theta as a function of t, and plot tthe angular velocity \omega as a function of \theta(Plot in phase space.). Strange things will ap
  当混沌现象发生时，通过![]()图我们很难看出其中的规律，但这并不意味着混沌现象完全没有规律可循。当我们画出一个摆的![]()图时，似乎能看出一些规律。
  ![]()![]()
  
```
# -*- coding: utf-8 -*-
import pylab as pl
import numpy as np

class pendulum(object):    
    def __init__(self, F_D, theta):
        #all units are in SI.
        self.theta = [theta]
        self.theta1 = [theta + 0.001]
        self.omega = [0]
        self.omega1 = [0]
        self.F_D = F_D
        self.t = [0]
        self.dt = 0.04
        self.delta_theta = [0.001]
        
    def calculate(self):
        l = 9.8
        g = 9.8
        q1 = 0.5
        q2 = 0.5
        self.omega_D = float(2)/3
        while(self.t[-1] < 150):
            temp1 = self.omega[-1] - ((g / l) * np.sin(self.theta[-1]) + q1 * self.omega[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega.append(temp1)
            temp2 = self.theta[-1] + temp1 * self.dt
            while(temp2 > np.pi):
                temp2 -= 2 * np.pi
            while(temp2 < -np.pi):
                temp2 += 2 * np.pi
            self.theta.append(temp2)
            
            temp3 = self.omega1[-1] - ((g / l) * np.sin(self.theta1[-1]) + q2 * self.omega1[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega1.append(temp3)
            temp4 = self.theta1[-1] + temp3 * self.dt 
            while(temp4 > np.pi):
                temp4 -= 2 * np.pi
            while(temp4 < -np.pi):
                temp4 += 2 * np.pi 
            self.theta1.append(temp4)
            
            self.t.append(self.t[-1] + self.dt)
            self.delta_theta.append(abs(self.theta[-1] - self.theta1[-1]))
        
    def show_results2(self):
        pl.plot(self.theta, self.omega, '.')
        pl.title(r'$\omega$ versus $\theta$($F_D$=%.1f)'%self.F_D)
        pl.xlabel(r'$\theta$(radians)')
        pl.ylabel(r'$\omega$(radians/$s$)')
        pl.show()
        
a=pendulum(1.2, 0.2)
a.calculate()
a.show_results2()
```

* 庞加莱截面（problem 3.12）
  ![]()![]()
  ![]()![]()
```
# -*- coding: utf-8 -*-
import pylab as pl
import numpy as np

class pendulum(object):    
    def __init__(self, F_D, theta):
        #all units are in SI.
        self.theta = [theta]
        self.theta1 = [theta + 0.001]
        self.omega = [0]
        self.omega1 = [0]
        self.F_D = F_D
        self.t = [0]
        self.dt = 0.04
        self.delta_theta = [0.001]
        
    def calculate(self):
        l = 9.8
        g = 9.8
        q1 = 0.5
        q2 = 0.5
        self.omega_D = float(2)/3
        while(self.t[-1] < 5000):
            temp1 = self.omega[-1] - ((g / l) * np.sin(self.theta[-1]) + q1 * self.omega[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega.append(temp1)
            temp2 = self.theta[-1] + temp1 * self.dt
            while(temp2 > np.pi):
                temp2 -= 2 * np.pi
            while(temp2 < -np.pi):
                temp2 += 2 * np.pi
            self.theta.append(temp2)
            
            temp3 = self.omega1[-1] - ((g / l) * np.sin(self.theta1[-1]) + q2 * self.omega1[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega1.append(temp3)
            temp4 = self.theta1[-1] + temp3 * self.dt 
            while(temp4 > np.pi):
                temp4 -= 2 * np.pi
            while(temp4 < -np.pi):
                temp4 += 2 * np.pi 
            self.theta1.append(temp4)
            
            self.t.append(self.t[-1] + self.dt)
            self.delta_theta.append(abs(self.theta[-1] - self.theta1[-1]))
            
        self.theta_x = []
        self.omega_y = []
        for i in range(int((self.t[-1] * self.omega_D) / (2 * np.pi))):
            k = int((0.5 + (2 * np.pi * i ) / (self.omega_D * self.dt)) // 1)
            self.theta_x.append(self.theta[k])
            self.omega_y.append(self.omega[k])
        
    def show_results2(self):
        o, = pl.plot(self.theta_x, self.omega_y, '.')
        pl.title(r'$\omega$ versus $\theta$($F_D$=%.1f)'%self.F_D)
        pl.xlabel(r'$\theta$(radians)')
        pl.ylabel(r'$\omega$(radians/$s$)')
        pl.legend([o],[r't$\approx$2$\pi$n/$\Omega_D$'],loc = 'best')
        pl.show()
        
a=pendulum(1.2, 0.2)
a.calculate()
a.show_results2()
```  

## 结论

## 致谢
