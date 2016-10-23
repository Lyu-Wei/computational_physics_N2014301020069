# Exercise_06

## 摘要
   在上一次作业的基础上，本次作业考虑了空气阻力、不同海拔空气密度的变化（绝热模型）、不同海拔重力加速度的变化和迎面风阻对炮弹轨迹的影响。本次所完成的系统实现了对任一距离目标的打击，并且引入了炮弹初速、角度和风阻误差，可以模拟打击n次再对模拟落点进行分析。

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
  ![](http://latex.codecogs.com/gif.latex?%5C%5C%20F_%7Bdrag%2Cx%7D%3D-B_%7B2%7D%7C%5Cvec%7Bv%7D-%5Cvec%7Bv_%7Bwind%7D%7D%7C%28v_%7Bx%7D-v_%7Bwind%7D%29%20%5C%5C%5C%5C%20F_%7Bdrag%2Cy%7D%3D-B_%7B2%7D%7C%5Cvec%7Bv%7D-%5Cvec%7Bv_%7Bwind%7D%7D%7Cv_%7By%7D)。<br>
* 误差引入<br>
  误差的引入可使用随机数实现。<br>
  模拟结果的方差由下面公式算出：<br>
  ![](http://latex.codecogs.com/gif.latex?s%5E%7B2%7D%3D%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-%5Cbar%7Bx%7D%29%5E%7B2%7D%5Capprox%20%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_%7Bi%7D-x_%7Btarget%7D%29%5E%7B2%7D)
  
## 题目
   作业L2 2.10题进一步升级，发展“超级辅助精确打击系统”（考虑炮弹初始发射的时候发射角度误差正负2度，速度有5%的误差，迎面风阻误差10%，以炮弹落点与打击目标距离差平方均值最小为优胜）
   
## 正文
* 对任意指定目标设计的轨迹<br>
  确定了目标距离后，程序将对炮弹发射角从0到90度间隔0.1度进行扫描，选出落点与目标距离最小的角度。该步程序中考虑了空气阻力、不同海拔空气密度的变化（绝热模型）、不同海拔重力加速度的变化和迎面风阻对炮弹轨迹的影响，引入这些影响因素的方法在背景介绍中给出。<br>
  该步程序如下：<br>
```
```
  在炮弹初速度为2公里每秒，风速为10公里每小时，打击距离100公里的目标结果如下图：<br>
  ![]()<br>
* 引入误差<br>
  现在我们考虑炮弹初始发射的时候发射角度误差正负2度，速度有5%的误差，迎面风阻误差10%。将由均匀分布随机数产生的误差项加在初速度、风阻和上一步我们计算所得的最佳角度上，模拟n次打击实验，画出炮弹轨迹图和落点距离图，计算出炮弹落点与打击目标距离差平方均值。<br>
  该步程序如下：<br>
```
```
  模拟100次结果如下图：<br>
  ![]()  ![]()<br>
  
  
## 程序代码
   [完整代码链接]()
   
## 结论
   通过此次作业，我学会了如何在物理计算模拟中考虑误差的影响，并由误差分析系统的性能。
   
## 致谢
   感谢蔡浩老师提供了课件。
