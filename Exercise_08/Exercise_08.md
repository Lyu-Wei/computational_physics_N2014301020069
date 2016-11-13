# Exercise_08

## 摘要 
　　本文完成了problem 3.18，即画出了做多倍周期运动的摆的庞加莱截面。

## 背景介绍
* 混沌<br>
　　混沌理论是关于非线性系统在一定参数条件下展现分岔、周期运动与非周期运动相互纠缠，以至于通向某种非周期有序运动的理论。在强迫力较大时，物理摆的运动轨迹将出现混沌现象。<br>
* 庞加莱截面<br>
　　其基本思想是在多维相空间(x,,dx, ldt,xZ,d²x /dt²,...dR /dt)中适当选取一截面，在此截面上某一对共扼变量如xdx, ldt取固定值，称此截面为庞加莱截面。<br>
　　观测运动轨迹与此截面的截点(庞加莱点)，设它们依次为P1,P2,P3…。原来相空间的连续轨迹在庞加莱截面上便表现为一些离散点之间的映射Pn。由它们可得到关于运动特性的信息。如不考虑初始阶段的暂态过渡过程，只考虑庞加莱截面的稳态图像，当庞加莱截面上只有一个不动点和少数离散点时，可判定运动是周期的;当庞加莱截面上是一封闭曲线时，可判定运动是准周期的;当庞加莱截面上是成片的密集点，且有层次结构时，可判定运动处于混沌状态。<br>

## 题目
problem 3.18<br>
Calculate Piuncare sections for the pendulum as it undergose the period-doubling route to chaos. Plot ω versus θ, with one point plotted for each drive cycle, as in Figure 3.9. Do this for F_D=1.4, 1.44, and 1.465, using the other parameters as fiven in connection with Figure 3.10. You should find that after removing the points corresponding to the initial transient the attractor in the period-1 regime will contain only a single point. Likewise, if the behavior is period n, the attractor will contain n discrete points.

## 正文
　　这次作业在上次作业所用的程序上进行了修改，为了使结果更加精确，改程序的时间间隔被修改为π/300，这样在做庞加莱截面时，就能每次都恰好取到前面计算时已经计算出的点，而不需要做近似。<br>
　　并且为了排除摆刚刚开始运动时不稳定时留下的图像，我们从第100个点开始画庞加莱截面。<br>
　　结果如图（θ-t图和庞加莱截面图像）：<br>  
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_08/ex8-3.jpg)<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_08/ex8-6.jpg)<br>
　　程序代码：<br>
```
# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np

class pendulum(object):    
    def __init__(self, F_D, theta):
        #all units are in SI.
        self.theta = [theta]
        self.omega = [0]
        self.F_D = F_D
        self.t = [0]
        self.dt = np.pi /300
        self.delta_theta = [0.001]
        
    def calculate(self):
        l = 9.8
        g = 9.8
        q = 0.5
        self.omega_D = 2.0/3
        while(self.t[-1] < 5000):
            temp1 = self.omega[-1] - ((g / l) * np.sin(self.theta[-1]) + q * self.omega[-1] - self.F_D * np.sin(self.omega_D * self.t[-1])) * self.dt
            self.omega.append(temp1)
            temp2 = self.theta[-1] + temp1 * self.dt
            while(temp2 > np.pi):
                temp2 -= 2 * np.pi
            while(temp2 < -np.pi):
                temp2 += 2 * np.pi
            self.theta.append(temp2)
            
            self.t.append(self.t[-1] + self.dt)
            
        self.theta_x = []
        self.omega_y = []
        for i in range(100,int((self.t[-1] * self.omega_D) / (2 * np.pi))):
            k = int(((2 * np.pi * i ) / (self.omega_D * self.dt)) // 1)
            self.theta_x.append(self.theta[k])
            self.omega_y.append(self.omega[k])
     
    def show_results1(self):
        pl.plot(self.t, self.theta)
        pl.title(r'$\Delta \theta$ versus time($F_D$=%.3f)'%self.F_D)
        pl.xlabel(r'time($s$)')
        pl.ylabel(r'$\Delta \theta$ (radians)')
        pl.xlim(0,100)
        pl.show()
        
    def show_results2(self):
        pl.plot(self.theta_x, self.omega_y, '.')
        pl.title(r'$\omega$ versus $\theta$($F_D$=%.3f)'%self.F_D)
        pl.xlabel(r'$\theta$(radians)')
        pl.ylabel(r'$\omega$(radians/$s$)')
        pl.xlim(1,3)
        pl.ylim(-2,-1)
        pl.show()
        
a=pendulum(1.4,0.2)
a.calculate()
a.show_results1()
a.show_results2()
```

## 结论
　　通过所得图像进行观察我们可以看到，当摆的运动是混沌状态时，庞加莱截面是呈曲线的；当摆的运动是n倍周期运动时，庞加莱截面为n个独立的点。<br>
　　由于在我的电脑上一直装不了vpython，所以本次作业没用vpython。

## 致谢
　　感谢课本和课件。
