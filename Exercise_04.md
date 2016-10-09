# Exercise_04

### 题目 
* problem 1.5<br>
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into type B, while nuclei of 
type B decay into type A. Strictly speaking, this is not a "decay" process, since it is possible for the type B nuclei to turn back 
into type A. A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which 
have equal energies. The corresponding rate equations are<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D),<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%5Cfrac%7BN_%7BA%7D%7D%7B%5Ctau%20%7D-%5Cfrac%7BN_%7BB%7D%7D%7B%5Ctau%20%7D),<br>
where for simplicity we have assumed that the two types of decay are characterized by the same time constant , ![](http://latex.codecogs.com/gif.latex?%7B%5Ctau%20%7D). Solve the system of equations for the numbers of nuclei, ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D), as functions of time. Consider different initial confitions, such as ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D%3D100), ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D%3D0), etc., and take ![](http://latex.codecogs.com/gif.latex?%5Ctau%20%3D1) s. Show that your numerical results are consistent with the idea that the system reaches a steady state in which ![](http://latex.codecogs.com/gif.latex?N_%7BA%7D) and ![](http://latex.codecogs.com/gif.latex?N_%7BB%7D) are constant. In such a steady state, the time derivatives ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BA%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) and ![](http://latex.codecogs.com/gif.latex?%7B%5Cmathrm%7Bd%7D%20N_%7BB%7D%7D/%7B%5Cmathrm%7Bd%7D%20t%7D) should vanish.

### 摘要
  本文介绍了运用欧拉方法解常微分方程，借助Python编写程序，解决problem 1.5 ——“双元素衰变问题”的过程。

### 背景介绍
* 原子核衰变<br>
  对于某一放射性元素集合体，在dt时间内衰变的原子数dN与此时刻母核数N(t)和dt乘积成正比，即：![](http://latex.codecogs.com/gif.latex?%5Cmathrm%7Bd%7D%20N%3D-%5Cfrac%7B1%7D%7B%5Ctau%20%7DN%5Cmathrm%7Bd%7Dt)。
积分运算后可得衰变规律方程：![](http://latex.codecogs.com/gif.latex?N%28t%29%3DN%280%29e%5E%7B-t/%5Ctau%20%7D)
，其中τ为一个时间常数，t=0时刻的放射性核数为N(0)，t时刻放射性核数为N(t)。

* 欧拉方法<br>
  在数学和计算机科学中，欧拉方法，命名自它的发明者莱昂哈德·欧拉，是一种一阶数值方法，用以对给定初值的常微分方程（即初值问题）求解。它是一种解决数值常微分方程的最基本的一类显型方法。<br>
  考虑计算这样的一个未知曲线的形状：它具有给定的起点并且满足一个给定的微分方程。 这里，所谓“微分方程”可以看作能够通过曲线上任意点的位置而计算出这一点的切线斜率的公式。<br>
  思路是，一开始只知道曲线的起点（假设为A0），曲线其他部分是未知的，不过通过微分方程,A0的斜率可以被计算出来，也就得到了切线。<br>
  顺着切线向前走一小步到点 A1。如果我们假设A1是曲线上的一点（实际上通常不是），那么同样的道理就可以确定下一条切线，依此类推。在经过几步之后，一条折线 A0A1A2A3...就被计算出来了。一般情况下，这条折线与原先的未知曲线偏离不远，并且任意小的误差都可以通过减少步长来得到。<br>
  具体到解衰变微分方程中：因为<br>![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN%7D%7Bdt%7D%5Cequiv%20%5Clim_%7B%5CDelta%20t%5Cto0%7D%5Cfrac%7BN%28t&plus;%5CDelta%20t%29-N%28t%29%7D%7B%5CDelta%20t%7D%5Capprox%5Cfrac%7BN%28t&plus;%5CDelta%20t%29-N%28t%29%7D%7B%5CDelta%20t%7D)，<br>
所以数值解为：<br>![](http://latex.codecogs.com/gif.latex?N%28t&plus;%5CDelta%20t%29%5Capprox%20N%28t%29&plus;%5Cfrac%7BdN%7D%7Bdt%7D%5CDelta%20t)，<br>
代入![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20N%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D%20-%5Cfrac%7BN%7D%7B%5Ctau%20%7D)，<br>
得：<br>![](http://latex.codecogs.com/gif.latex?N%28t&plus;%20%5CDelta%20t%29%5Capprox%20N%28t%29%20-%5Cfrac%7BN%7D%7B%5Ctau%20%7D%5CDelta%20t)。
