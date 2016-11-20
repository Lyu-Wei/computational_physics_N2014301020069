# Exercise_09

## 摘要
　　台球桌上的球的运动轨迹也可以产生混沌现象。

## 背景介绍
* 混沌<br>
　　混沌理论是关于非线性系统在一定参数条件下展现分岔、周期运动与非周期运动相互纠缠，以至于通向某种非周期有序运动的理论。<br>
* 台球桌问题<br>
　　我们假设一个水平无摩擦的桌子，桌上有一个球，其与桌边缘的碰撞是完全弹性碰撞。<br>
　　不考虑桌边缘的墙，台球运动方程是：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/4ll.png)<br>
　　考虑球与墙的碰撞有：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/5ll.png)<br>
　　于是得到碰撞后的球速度：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/6ll.png)<br>

## 题目
problem 3.30<br>
Investigate the Lyapunov exponent of the stadium billiard for several values of α. You can do this qualitatively by examining the behavior for only one set of initial conditions for each value of α you consider, or more quantitatively by averaging over a range of initial conditions for each value of α.

## 正文
　　首先我们考虑桌子是正方形的情况，球轨迹如图（[代码链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/Exercise_09.py)）：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/e91.png)<br>
　　然后我们考虑圆形桌子和运动场形的桌子，球轨迹如图（[代码链接（左图）](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/Exercise_09b.py)[代码链接（右图）](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/Exercise_09c.py)）：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/e96.jpg)<br>
　　比较α不同时的运动场形桌子的相空间图（[代码链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/Exercise_09d.py)）：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/e94.png)
　　比较α不同时的运动场形桌子中两个相近初始条件的球轨迹（[代码链接](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/Exercise_09e.py)）：<br>
　　![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_09/e95.png)<br>

## 结论
　　完成了problem 3.30，进一步了解了混沌现象。

## 致谢
　　感谢课本。
