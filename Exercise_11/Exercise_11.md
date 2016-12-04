# Exercise_11

## Abstract
In this essay, we will discuss chaotic tumbling of Hyperion and use Python to simulate the orbit of Hyperion.

## Background
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/PIA17193-SaturnMoon-Hyperion-20150531.jpg)<br>
Hyperion, also known as Saturn VII (7), is a moon of Saturn discovered by William Cranch Bond, George Phillips Bond and William Lassell in 1848. It is distinguished by its irregular shape, its chaotic rotation, and its unexplained sponge-like appearance. It was the first non-round moon to be discovered.<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/hyperion_21_45_200.jpg)<br>
yperion is unique among the large moons in that it is very irregularly shaped, has a fairly eccentric orbit, and is near a much larger moon, Titan. These factors combine to restrict the set of conditions under which a stable rotation is possible. The 3:4 orbital resonance between Titan and Hyperion may also make a chaotic rotation more likely. The fact that its rotation is not locked probably accounts for the relative uniformity of Hyperion's surface, in contrast to many of Saturn's other moons, which have contrasting trailing and leading hemispheres.<br>
The differential equation of Hyperion's orbit is<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/p1.png)<br>

## Problem
* problem 4.19<br>
Study the behavior of our model for Hyperion for dofferent initial conditions. Estimate the Lyapunov exponent from calculations of Δθ, such as those shown in Figure 4.19. Examine how this exponent varies as a function of the eccentricity of the orbit.<br>

* problem 4.20<br>
Our results for the divergence of the two trajectories θ₁(t) and θ₂(t) in the chaotic regime, shown on the right in Figure 4.19,are complicated by the way we dealt with the angle θ. In Figure 4.19 we followed the practice employed in Chapter3 and restricted θ to the range -π to +π, since angles outside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then "reset" (by adding or substracting 2π), this shows up in the results for Δθ as a discontinuous (and distracting) jump. Repeat the calculation of Δθ as in Figure 4.19, but do not restrict the value of θ. This should remove the large (Δθ~2π) jumps in Δθ in Figure 4.19, but the smaller and more frequent dips will remain. What is the origin of these dips?<br>

## Main Body
* The conditions that the orbit of Hyperion is circular and elleptical<br>
When the orbit is circular orbit, we can plot the θ-t, ω-t and ω-θ relations:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/ll1.jpg)<br>
From the figure, we can see that there is no chaotic when orbit is circular.<br>
When the orbit is elleptical, chaotic tumbling happens:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/ll2.jpg)<br>

* The effect from different initial velocities<br>
When the initial velocity is 7 HU/Hyperion-year, the condition of Hyperion is shown as:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/ll3.jpg)<br>
When the initial welocity is 10 HU/Hyperion-year:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/ll4.jpg)<br>
We can know Hyperion will leave out Saturn when the initial velocity is too high.<br>

* The effect from different initial angle<br>
When the initial angle is π/2 and initial velocity is 5 HU/Hyperion-year, there is no chaotic tumbling happens in Hyperion:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/ll5.jpg)<br>
In the same angle, chaotic tumbling will happen when initial velocity is 7 HU/Hyperion-year:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/ll6.jpg)<br>

* Δθ and Lyapunov exponent<br>
We can plot the Δθ-t when the orbit is circular and elleptiacl:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/l19.png)<br>
We also can see the Lyapunov exponent will raise as the eccentrocity of orbit raises:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/l20.png)<br>

* Delate the restrain of angle range<br>
If we don't have the restrain that the difference of angles remains 0-2π (problem 4.20), we can draw the picture of Δθ-t as:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/l21.png)<br>

## Code
[code](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_11/Exercise_11.py)

## Conclusion
Finished problem 4.19 and 4.20.

## Acknowledge
Thank wikipedia and Google.
