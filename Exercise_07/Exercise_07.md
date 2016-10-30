# Exercise_07

## 摘要
　　本文介绍了使用物理摆系统制造混沌现象，并通过Δθ-t图，ω-θ图和庞加莱截面研究混沌现象的过程。<br>

## 背景介绍
* 物理摆方程<br>
　　一个非线性的、有阻尼的、受迫的摆又被称为物理摆，它包含了许多有趣的现象，其运动的微分方程为：<br>
　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%5E2%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7Dt%7D&plus;F_Dsin%28%5COmega%20_Dt%29)。<br>
　　我们可以将这个二阶微分方程写成两个一阶微分方程：<br>
　　![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%5Comega%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta%20-q%5Cfrac%7B%5Cmathrm%7Bd%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7Dt%7D&plus;F_Dsin%28%5COmega%20_Dt%29%2C%20%5C%5C%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20%5Ctheta%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Comega.)<br>
　　我们再运用eular—cromer方法有：<br>
　　![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Comega_%7Bi&plus;1%7D%3D%5Comega_i-%5B%28g/l%29sin%5Ctheta_i&plus;q%5Comega_i-F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t%20%5C%5C%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)<br>
　　如果![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D)不在区间[-π,π]范围内，加上或者减掉2π使它保持在这个范围中。<br>
　　![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_%7Bi%7D&plus;%5CDelta%20t)<br>
* 混沌<br>
　　混沌理论是关于非线性系统在一定参数条件下展现分岔、周期运动与非周期运动相互纠缠，以至于通向某种非周期有序运动的理论。在强迫力较大时，物理摆的运动轨迹将出现混沌现象。<br>
* 庞加莱截面<br>
　　其基本思想是在多维相空间(x,,dx, ldt,xZ,d²x /dt²,...dR /dt)中适当选取一截面，在此截面上某一对共扼变量如xdx, ldt取固定值，称此截面为庞加莱截面。<br>
　　观测运动轨迹与此截面的截点(庞加莱点)，设它们依次为P1,P2,P3…。原来相空间的连续轨迹在庞加莱截面上便表现为一些离散点之间的映射Pn。由它们可得到关于运动特性的信息。如不考虑初始阶段的暂态过渡过程，只考虑庞加莱截面的稳态图像，当庞加莱截面上只有一个不动点和少数离散点时，可判定运动是周期的;当庞加莱截面上是一封闭曲线时，可判定运动是准周期的;当庞加莱截面上是成片的密集点，且有层次结构时，可判定运动处于混沌状态。<br>
  

## 题目
* Problem 3.12.<br>
In constructing the Poincaré section in Figure 3.9 we plotted points only at times that were in phase with the force; that is, at times ![](http://latex.codecogs.com/gif.latex?t%5Capprox%202%5Cpi%20n/%5COmega%20_D), where n is an interger. At these values of t the driving force passed throught zero [see (3.8)]. However, we could just as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times ![](http://latex.codecogs.com/gif.latex?%5Cpi/4) out-of-phase with this force, etc. Construct the Poincaré sections for these cases and compare them with Figure 3.9.

* Problem 3.13.<br>
Write a program to calculate and compare the brhavior of two, nearly indentical pedulums. Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent from the slope of a plot of ![](http://latex.codecogs.com/gif.latex?log%28%5CDelta%20%5Ctheta%20%29) as a function of t.

* Problem 3.14.<br>
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent compare with that found in Figure 3.7?


## 正文
* 初始条件微小变化对结果的影响（problem 3.13）<br>
　　物理摆摆动过程中，当强迫力较小时，初始值的微小变化对结果影响很小；若强迫力较大，则混沌现象发生，初始值对结果影响巨大。下面我们同时摆动两个物理摆，它们除θ(0)不一样外（Δθ=0.001），其他参数都相同(q=1/2,l=g=9.8,![](http://latex.codecogs.com/gif.latex?%5COmega_D)=2/3,dt=0.04,ω(0)=0,全为SI单位），它们的Δθ-s 图如下（此步在计算θ时不用使其保持在区间[-π，π]中）：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07n.jpg)<br>
　　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07n.jpg)<br>
　　经过模拟发现，当θ₁（0）取0.2时无法画出Figure3.7的右图，取θ₁（0）=0.16999，刻画出与其相似的图。这个现象也说明了混沌现象的神奇。<br>
　　为更好地表现结果，该图的纵坐标使用lg为刻度。整个程序代码如下：<br>
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

* 阻尼系数的微小改变对结果的影响（problem 3.14）<br>
　　如果我们让第二个摆的阻尼系数（q2）改变，其他参数不变（θ₁=0.2,Δθ=0.001,q=1/2,l=g=9.8,![](http://latex.codecogs.com/gif.latex?%5COmega_D)=2/3,dt=0.04,ω(0)=0），结果如图：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07c.png)<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07e.png)<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07d.png)<br>
　　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07c.png)<br>
　　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07e.png)<br>
　　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07d.png)<br>
　　第一幅图的Lyapunov指数约为-2.5，后两幅图的Lyapunov指数接近于0。<br>
　　程序代码如下：<br>
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
  
* 空间相位图<br>
　　当混沌现象发生时，通过θ-t图我们很难看出其中的规律，但这并不意味着混沌现象完全没有规律可循。当我们画出一个摆的ω-θ图时，似乎能看出一些规律。<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07k.jpg)<br>
　　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07k.jpg)<br>
  　当强迫力较小时，最终的轨道是独立于初始值的封闭曲线；强迫力较大时，空间相位轨迹很复杂却不是完全混乱的。<br>
  　该过程代码如下：<br>
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

* 庞加莱截面（problem 3.12）<br>
  　如果我们只画出某些时间点的相位点，则得到了庞加莱截面：<br>
　　强迫力为1.2时，<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07j.jpg)<br>
  　强迫力为0.5时，<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07h.jpg)<br>
  　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07j.jpg)<br>
  　[图片链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_07/Exercise_07h.jpg)<br>
  　根据背景介绍中对庞加莱截面的描述和上图可判断，强迫力为0.5时，物理摆做周期运动；强迫力为1.2时，物理摆运动处于混沌状态。<br>
  　该过程代码如下：<br>
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
　　通过Δθ-t图，我们发现，强迫力较小时，Lyapunov指数小于0，θ趋于0；强迫力较大时，Lyapunov指数大于0。通过空间相位图和庞加莱截面，我们知道了判断系统是否为混沌状态的直观方法。
  

## 致谢
　　感谢维基百科和百度百科。
