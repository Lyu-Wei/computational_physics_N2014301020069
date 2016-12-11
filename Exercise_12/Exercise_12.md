# Exercise_12

## Abstract
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y02.png)<br>
In this essay, we will discuss how to solve the capacitor problem (we can also call it the problem about electric potential near two metal plates) by relaxition method.<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y01.jpg)<br>

## Background
* Laplace's Equation<br>
In order to find the distribution of the electric field of the capacitor, we need to solve for the Laplace's equation. In mathematics, Laplace's equation is a second-order partial differential equation named after Pierre-Simon Laplace who first studied its properties. This is often written as:<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20z%5E2%7D%3D0)<br>

* Relaxition Method<br><br>
In numerical mathematics, relaxation methods are iterative methods for solving systems of equations, including nonlinear systems.<br>
Relaxation methods were developed for solving large sparse linear systems, which arose as finite-difference discretizations of differential equations. They are also used for the solution of linear equations for linear least-squares problems and also for systems of linear inequalities, such as those arising in linear programming. They have also been developed for solving nonlinear systems of equations.<br>
Relaxation methods are important especially in the solution of linear systems used to model elliptic partial differential equations, such as Laplace's equation and its generalization, Poisson's equation. These equations describe boundary-value problems, in which the solution-function's values are specified on boundary of a domain; the problem is to compute a solution also on its interior. Relaxation methods are used to solve the linear equations resulting from a discretization of the differential equation, for example by finite differences.<br>
These iterative methods of relaxation should not be confused with "relaxations" in mathematical optimization, which approximate a difficult problem by a simpler problem, whose "relaxed" solution provides information about the solution of the original problem.<br>

* Jacobi Method<br>
In numerical linear algebra, the Jacobi method (or Jacobi iterative method) is an algorithm for determining the solutions of a diagonally dominant system of linear equations. Each diagonal element is solved for, and an approximate value is plugged in. The process is then iterated until it converges. This algorithm is a stripped-down version of the Jacobi transformation method of matrix diagonalization. The method is named after Carl Gustav Jacob Jacobi.<br>

* SOR<br>
In numerical linear algebra, the method of successive over-relaxation (SOR) is a variant of the Gauss–Seidel method for solving a linear system of equations, resulting in faster convergence. A similar method can be used for any slowly converging iterative process.<br>
It was devised simultaneously by David M. Young, Jr. and by Stanley P. Frankel in 1950 for the purpose of automatically solving linear systems on digital computers. Over-relaxation methods had been used before the work of Young and Frankel. An example is the method of Lewis Fry Richardson, and the methods developed by R. V. Southwell. However, these methods were designed for computation by human calculators, and they required some expertise to ensure convergence to the solution which made them inapplicable for programming on digital computers. These aspects are discussed in the thesis of David M. Young, Jr.<br>

## Problem
* Problem 5.3.<br>
Use the symmetry of the capacitor problem (Figure 5.6) to write a program that obtain the result by calculating the potential in only one quadrant of the x-y plane.<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y0.png)<br>

* Problem 5.7.<br>
Write two programs to solve the capacitor problem of Figure 5.6 and 5.7,one using the Jacobi method and one using the SOR algorithm. For a fixed accuracy (as set by the convergence test)compare the number of iterations, ![](http://latex.codecogs.com/gif.latex?N_%7Biter%7D),that each algorithm requires as a function of the member of grid elements, L. Show that for the Jacobi method ![](http://latex.codecogs.com/gif.latex?N_%7Biter%7D%5Csim%20L%5E2),while with SOR ![](http://latex.codecogs.com/gif.latex?N_%7Biter%7D%5Csim%20L).<br>

## Main Body
* Voltage Near the Capacitor<br>
First, we can solve the capacitor problem using numerical method and draw a picture to dscribe voltage near the capacitor:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y1.png)<br>
Then we can change it as 3d picture:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y2.png)<br>
We also can put color on the picture:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y3.png)<br>
And this is electric field near the capacitor:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y4.png)<br>

* Comparation between Jacobi Method and SOR<br>
From the picture we can see SOR is better than the Jacobi Method:<br>
![](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/y5.png)<br>

## Code
[code](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/Exercise_12%2B.py)<br>
[code](https://github.com/Lyu-Wei/computational_physics_N2014301020069/blob/master/Exercise_12/Exercise_12.py)<br>

## Conclusion
Finished problem 5.3. and 5.7. successfully.

## Appreciation
Wikipedia & the official website of matplotlib
