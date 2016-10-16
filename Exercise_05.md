# Exercise_05

## 摘要
  斜抛运动轨迹是一个经典的物理模型，我们也可以把它看作是理想的炮弹轨迹。本文介绍了使用欧拉方法计算在无阻力条件下的炮弹轨迹的过程，并将计算结果与精确解进行了对比（problem 2.6）。


## 背景介绍
* 抛体运动<br>
  根据牛顿第二定律有方程组：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3D0%20%5C%5C%5C%5C%20%5Cfrac%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3D-g)
  
  
* 二次常微分方程的欧拉方法<br>
  首先每一个二次常微分方程都可写为两个一次常微分方程：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cfrac%7Bdx%7D%7Bdt%7D%3Dv_x%2C%5Cfrac%7Bdv_x%7D%7Bdt%7D%3D0%20%5C%5C%5C%5C%20%5Cfrac%7Bdy%7D%7Bdt%7D%3Dv_y%2C%5Cfrac%7Bdv_y%7D%7Bdt%7D%3D-g)<br>
  我们可以得到如下形式的等式：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci%7D%5CDelta%20t%2Cv_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci%7D%5CDelta%20t%2Cv_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t)
  
  
* 落点<br>
  若地面以上最后一点为n，地面以下第一点为n+1，则落点坐标为<br>
  ![](http://latex.codecogs.com/gif.latex?x%3D%5Cfrac%7Bx_%7Bn%7D&plus;rx_%7Bn&plus;1%7D%7D%7Br&plus;1%7D%2Cy_%7Bl%7D%3D0)<br>
  其中<br>
  ![](http://latex.codecogs.com/gif.latex?r%3D-%5Cfrac%7By_%7Bn%7D%7D%7By_%7Bn&plus;1%7D%7D)
  

## 题目
* problem 2.6<br>
  Use the Euler method to calculate cannon shell trajectories ignoring both air drag angd the effect of air density (actually, ignoring the former automatically rules out the latter). Compare your results with those in Figure 2.4, and with the exact solution.
  
## 正文
* 炮弹轨迹模型<br>
  设定初始条件及主要参数：![](http://latex.codecogs.com/gif.latex?v_%7B0%7D%3D0.7km/s%2Cg%3D0.0098km/s%5E%7B2%7D%2C%5CDelta%20t%3D0.5)<br>
  根据背景介绍中所给的方程和欧拉方法，可以编写出以下程序计算若干个初始角度时的炮弹轨迹：<br>
```
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
```
  计算结果如图所示：<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_05a.png)
  
* 结果与精确解比较<br>
  方程精确解为：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20x%3Dv_%7B0%7Dcos%5Ctheta%20%5Ccdot%20t%20%5C%5C%20y%3Dv_%7B0%7Dsin%5Ctheta%20%5Ccdot%20t-%5Cfrac%7B1%7D%7B2%7Dgt%5E%7B2%7D)<br>
  编写检验程序如下：<br>
```
class exact_results_check(trajectories):
    def show_results(self):
        self.etx = []
        self.ety = []
        for i in self.angle:
            self.etx.append([0])
            self.ety.append([0])
            while (self.ety[-1][-1] > 0) or (self.etx[-1][-1] == 0):
                self.etx[-1].append(self.v_0 * math.cos((float(i) / 180) * math.pi) * self.dt * len(self.etx[-1]))
                self.ety[-1].append(self.v_0 * math.sin((float(i) / 180) * math.pi) * self.dt * len(self.ety[-1]) - 0.5 * self.g * (self.dt * len(self.ety[-1])) ** 2 )
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
```
  在![](http://latex.codecogs.com/gif.latex?%5CDelta%20t%3D0.5)时，检验结果如下：<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_05b.png)<br>
  若![](http://latex.codecogs.com/gif.latex?%5CDelta%20t%3D0.05)，精确解和数值解的轨迹基本重合：<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_05c.png)
  
## 程序代码
  [完整代码链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_05%2B.py)
  
## 结论
  计算所得结果与课本FIGURE 2.4左图基本一致，![](http://latex.codecogs.com/gif.latex?%5CDelta%20t)取值越小，数值解与精确解越接近。


## 致谢
  感谢蔡浩老师提供了课件。
