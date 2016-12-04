# Exercise_11

## Abstract
In this essay, we will discuss chaotic tumbling of Hyperion and use Python to simulate the orbit of Hyperion.

## Background
![]()
Hyperion, also known as Saturn VII (7), is a moon of Saturn discovered by William Cranch Bond, George Phillips Bond and William Lassell in 1848. It is distinguished by its irregular shape, its chaotic rotation, and its unexplained sponge-like appearance. It was the first non-round moon to be discovered.
yperion is unique among the large moons in that it is very irregularly shaped, has a fairly eccentric orbit, and is near a much larger moon, Titan. These factors combine to restrict the set of conditions under which a stable rotation is possible. The 3:4 orbital resonance between Titan and Hyperion may also make a chaotic rotation more likely. The fact that its rotation is not locked probably accounts for the relative uniformity of Hyperion's surface, in contrast to many of Saturn's other moons, which have contrasting trailing and leading hemispheres.
The differential equation of Hyperion's orbit is
![]()

## Problem
* problem 4.19
Study the behavior of our model for Hyperion for dofferent initial conditions. Estimate the Lyapunov exponent from calculations of Δθ, such as those shown in Figure 4.19. Examine how this exponent varies as a function of the eccentricity of the orbit.

* problem 4.20
Our results for the divergence of the two trajectories θ₁(t) and θ₂(t) in the chaotic regime, shown on the right in Figure 4.19,are complicated by the way we dealt with the angle θ. In Figure 4.19 we followed the practice employed in Chapter3 and restricted θ to the range -π to +π, since angles outside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then "reset" (by adding or substracting 2π), this shows up in the results for Δθ as a discontinuous (and distracting) jump. Repeat the calculation of Δθ as in Figure 4.19, but do not restrict the value of θ. This should remove the large (Δθ~2π) jumps in Δθ in Figure 4.19, but the smaller and more frequent dips will remain. What is the origin of these dips?

## Main Body




## Code

## Conclusion

## Acknowledge

