# Exercise_06

## 摘要

## 背景介绍
* 抛体运动方程及其数值解法已经在上一次作业（[Exercise_05](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_05.md)）的背景介绍中给出。<br>
* 阻力<br>
  阻力的值有下面这一方程给出：<br>
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_%7B2%7Dv%5E%7B%7D2)，<br> 
  其中![](http://latex.codecogs.com/gif.latex?v%3D%5Csqrt%7Bv_%7Bx%7D%5E%7B2%7D&plus;v_%7By%7D%5E%7B2%7D%7D) 。<br>
  将阻力在坐标系中分解有：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20F_%7Bdrag%2Cx%7D%3DF_%7Bdrag%7Dcos%5Ctheta%20%3DF_%7Bdrag%7D%28v_x/v%29%3D-B_2vv_x%20%5C%5C%20F_%7Bdrag%2Cy%7D%3DF_%7Bdrag%7Dsin%5Ctheta%20%3DF_%7Bdrag%7D%28v_y/v%29%3D-B_2vv_y)。<br>
  运用欧拉方法有：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t)。<br>
* 海拔对空气密度的影响<br>
  在绝热模型中：<br>
  ![](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%5Crho%20_0%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%20%7D)，<br>
  其中![](http://latex.codecogs.com/gif.latex?a%5Capprox%206.5%5Ctimes%2010%5E%7B-3%7DK/m%2C%5Calpha%20%5Capprox%202.5)，![](http://latex.codecogs.com/gif.latex?T_%7B0%7D)是海平面的开尔文温度（![](http://latex.codecogs.com/gif.latex?%5Capprox%20300K)）。<br>
  受海拔影响空气的阻力为：<br>
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E%7B*%7D%3D%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7DF_%7Bdrag%7D%28y%3D0%29)。<br>
  所以有：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20x_%7Bi&plus;1%7D%3Dx_i&plus;v_%7Bx%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7D%5Cfrac%7BB_2vv_%7Bx%2Ci%7D%7D%7Bm%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20y_%7Bi&plus;1%7D%3Dy_i&plus;v_%7By%2Ci%7D%5CDelta%20t%20%5C%5C%20%5C%5C%20v_%7By%2Ci&plus;1%7D%3Dv_%7By%2Ci%7D-g%5CDelta%20t-%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_0%7D%5Cfrac%7BB_2vv_%7By%2Ci%7D%7D%7Bm%7D%5CDelta%20t)。<br>
* 海拔对重力加速度的影响<br>
  ![](http://latex.codecogs.com/gif.latex?g%3Dg_0%28%5Cfrac%7BR%7D%7BR&plus;y%7D%29%5E2)<br>
* 风的影响
  考虑风的影响后阻力在x轴和y轴上的分力为：<br>
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20F_%7Bdrag%2Cx%7D%3D-B_%7B2%7D%7C%5Cvec%7Bv%7D-%5Cvec%7Bv_%7Bwind%7D%7D%7C%28v_%7Bx%7D-v_%7Bwind%7D%29%20%5C%5C%5C%5C%20F_%7Bdrag%2Cy%7D%3D-B_%7B2%7D%7C%5Cvec%7Bv%7D-%5Cvec%7Bv_%7Bwind%7D%7D%7Cv_%7By%7D)。
