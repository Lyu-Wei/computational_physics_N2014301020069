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
本文介绍了运用欧拉法解常微分方程，借助Python编写程序，解决problem 1.5 ——“双元素衰变问题”的过程。

### 背景介绍
* 原子核衰变<br>
对于某一放射性元素集合体，在dt时间内衰变的原子数dN与此时刻母核数N(t)和dt乘积成正比，即：![](http://latex.codecogs.com/gif.latex?%5Cmathrm%7Bd%7D%20N%3D-%5Cfrac%7B1%7D%7B%5Ctau%20%7DN%5Cmathrm%7Bd%7Dt)。
积分运算后可得衰变规律方程：![](http://latex.codecogs.com/gif.latex?N%28t%29%3DN%280%29e%5E%7B-t/%5Ctau%20%7D)
，其中τ为一个时间常数，t=0时刻的放射性核数为N(0)，t时刻放射性核数为N(t)。
