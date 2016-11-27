# Exercise_10

## Abstract
In this essay, we will discuss the Kepler' Laws of planetary motion and precession of the erihelion of Mercury and use Python to simulate the orbit of Mercury.<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/002VTACjgy6U69Bogp644%26690.jpg)
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/9f4702003af33a8730dab0acc45c10385243b554.jpg)
## Background
### Kepler's Laws of planetary motion
In astronomy, Kepler's laws of planetary motion are three scientific laws describing the motion of planets around the Sun.<br>
1.The orbit of a planet is an ellipse with the Sun at one of the two foci.<br>
2.A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.<br>
![Kepler-second-law(extracted from wikipedia)](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/Kepler-second-law.gif)<br>
3.The square of the orbital period of a planet is proportional to the cube of the semi-major axis of its orbit.<br>
### Precession of the Perihelion of Mercury
Discrepancies between the observed perihelion precession rate of the planet Mercury and that predicted by classical mechanics were prominent among the forms of experimental evidence leading to the acceptance of Einstein's Theory of Relativity (in particular, his General Theory of Relativity), which accurately predicted the anomalies. Deviating from Newton's law, Einstein's theory of gravitation predicts an extra term, which accurately gives the observed excess turning rate of 43″ every 100 years.<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/Apsidendrehung.png)
The force law predicted by general relativity is<br>
![](http://latex.codecogs.com/gif.latex?F_G%5Capprox%20%5Cfrac%7BGM_SM_M%7D%7Br%5E2%7D%5Cleft%20%28%201&plus;%5Cfrac%7B%5Calpha%20%7D%7Br%5E2%7D%20%5Cright%20%29) ,<br>
where ![](http://latex.codecogs.com/gif.latex?M_M) is the mass of Mercury and ![](http://latex.codecogs.com/gif.latex?%5Calpha%20%5Capprox%201.1%5Ctimes%2010%5E%7B-8%7DAU%5E2) .

## Problem
problem 4.10. Calculate the precession of the perihelion of Mercury, following the approach described in this section.

## Main Body
* First, we don't consider the effects of general relativity, and then we plot the orbit of Mercury(t=4T):<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o1.png)<br>
* Second, we consider the effects of general relativity. The result obtained using the force law with α=0.01 is shown in the following picture(t=4T):<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o2.png)<br>
  Then, we expand time and we will obtain this result when t=20T:<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o3b.png)<br>
  When t=80T:<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o4.png)<br>
* If we make α=0.0008, we will obtain such results:<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o11.jpg)<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o12.jpg)<br>
* We also need plot the picture of orbit orientation versus time:<br>
  ![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/o5.png)<br>

## Code
[code](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_10/Exercise_10.py)

## Conclusion
Finished the problem 4.10 successfully.

## Acknowledge
Wikipedia, Google.
