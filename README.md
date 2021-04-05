# Dynamics of Spheres

## NOTE: CODE REQUIRES HIGH DEGREE OF REFACTORING

Simulations of the dynamics of idealised spheres in four different generalised contexts. Initially created with A-Level students as the target end-users, to help them visualise complex topics taught in class. Built using Python and Tkinter.


# Theory

## Projectile Motion

The parabolic equation for the trajectory of a projectile in a uniform gravitational field with no resistance. Angle of projection (<a href="https://www.codecogs.com/eqnedit.php?latex=\Theta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Theta" title="\Theta" /></a>), gravitational constant (g), initial velocity (<a href="https://www.codecogs.com/eqnedit.php?latex=V_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V_{0}" title="V_{0}" /></a>);

<a href="https://www.codecogs.com/eqnedit.php?latex=y=\tan&space;(\Theta&space;)x&space;-&space;\frac{g}{2V_{0}^{2}cos^{2}(\Theta&space;)}x^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y=\tan&space;(\Theta&space;)x&space;-&space;\frac{g}{2V_{0}^{2}cos^{2}(\Theta&space;)}x^{2}" title="y=\tan (\Theta )x - \frac{g}{2V_{0}^{2}cos^{2}(\Theta )}x^{2}" /></a>

where this program's boundary conditions for user input are defined as;

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;\leq&space;g" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;\leq&space;g" title="0 \leq g" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;\leq&space;\Theta&space;\leq&space;90" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;\leq&space;\Theta&space;\leq&space;90" title="0 \leq \Theta \leq 90" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;\leq&space;V_{0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;\leq&space;V_{0}" title="0 \leq V_{0}" /></a>


## Momentum

For two uniform masses (<a href="https://www.codecogs.com/eqnedit.php?latex=m_{a},&space;m_{b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m_{a},&space;m_{b}" title="m_{a}, m_{b}" /></a>) travelling at velocities (<a href="https://www.codecogs.com/eqnedit.php?latex=u_{a},&space;u_{b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u_{a},&space;u_{b}" title="u_{a}, u_{b}" /></a>) in a one dimensional resistance-free environment we find a solution for the final velocities of both masses in a collision with coefficient of restitution (<a href="https://www.codecogs.com/eqnedit.php?latex=C_{R}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C_{R}" title="C_{R}" /></a>):

<a href="https://www.codecogs.com/eqnedit.php?latex=v_{a}&space;=&space;\frac{m_{a}u_{a}&plus;m_{b}u_{b}&plus;m_{b}C_{R}(u_{b}-u_{a})}{m_{a}&plus;m_{b}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_{a}&space;=&space;\frac{m_{a}u_{a}&plus;m_{b}u_{b}&plus;m_{b}C_{R}(u_{b}-u_{a})}{m_{a}&plus;m_{b}}" title="v_{a} = \frac{m_{a}u_{a}+m_{b}u_{b}+m_{b}C_{R}(u_{b}-u_{a})}{m_{a}+m_{b}}" /></a>

and  

<a href="https://www.codecogs.com/eqnedit.php?latex=v_{b}&space;=&space;\frac{m_{a}u_{a}&plus;m_{b}u_{b}&plus;m_{a}C_{R}(u_{a}-u_{b})}{m_{a}&plus;m_{b}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_{b}&space;=&space;\frac{m_{a}u_{a}&plus;m_{b}u_{b}&plus;m_{a}C_{R}(u_{a}-u_{b})}{m_{a}&plus;m_{b}}" title="v_{b} = \frac{m_{a}u_{a}+m_{b}u_{b}+m_{a}C_{R}(u_{a}-u_{b})}{m_{a}+m_{b}}" /></a>

where this program's boundary conditions for user input are defined as;

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;\leq&space;m_{a},&space;m_{b}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;\leq&space;m_{a},&space;m_{b}" title="0 \leq m_{a}, m_{b}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=-10&space;\leq&space;u_{a},&space;u_{b}&space;\leq&space;10" target="_blank"><img src="https://latex.codecogs.com/gif.latex?-10&space;\leq&space;u_{a},&space;u_{b}&space;\leq&space;10" title="-10 \leq u_{a}, u_{b} \leq 10" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;\leq&space;C_{R}&space;\leq&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;\leq&space;C_{R}&space;\leq&space;1" title="0 \leq C_{R} \leq 1" /></a>


## Simple Harmonic Motion


We assume a restoring force that is directly proportional to the displacement (y) and acts in the direction opposite to that of the displacement. Spring constant (k), mass (m), time (t).

<a href="https://www.codecogs.com/eqnedit.php?latex=y&space;=&space;Asin(wt)&space;=&space;Asin((\frac{k}{m})^{\frac{1}{2}}t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;=&space;Asin(wt)&space;=&space;Asin((\frac{k}{m})^{\frac{1}{2}}t)" title="y = Asin(wt) = Asin((\frac{k}{m})^{\frac{1}{2}}t)" /></a>

where this program's boundary conditions for user input are defined as;

<a href="https://www.codecogs.com/eqnedit.php?latex=1&space;\leq&space;m&space;\leq&space;10" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1&space;\leq&space;m&space;\leq&space;10" title="1 \leq m \leq 10" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=0.1&space;\leq&space;k&space;\leq&space;5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0.1&space;\leq&space;k&space;\leq&space;5" title="0.1 \leq k \leq 5" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=100&space;\leq&space;A&space;\leq&space;280" target="_blank"><img src="https://latex.codecogs.com/gif.latex?100&space;\leq&space;A&space;\leq&space;280" title="100 \leq A \leq 280" /></a>

## Orbits

The equation of an ellipse with eccentricity (e) can be described;

<a href="https://www.codecogs.com/eqnedit.php?latex=r(\Theta)&space;=&space;\frac{a(1-e^{2})}{1&plus;cos(\Theta&space;)e}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r(\Theta)&space;=&space;\frac{a(1-e^{2})}{1&plus;cos(\Theta&space;)e}" title="r(\Theta) = \frac{a(1-e^{2})}{1+cos(\Theta )e}" /></a>

(This equation when programmed as an animation fails to accurately describe a satellite's motion. To fix this I crudely tried to relate the distance between the orbiting bodies to the time that should be waited between each iteration. The module is patchy and should be ignored for those who seek acccuracy.)

where this program's boundary conditions for user input are defined as;

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;\leq&space;e&space;<&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;\leq&space;e&space;<&space;1" title="0 \leq e < 1" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=10&space;\leq&space;a&space;\leq&space;300" target="_blank"><img src="https://latex.codecogs.com/gif.latex?10&space;\leq&space;a&space;\leq&space;300" title="10 \leq a \leq 300" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=0&space;<&space;Animation&space;Speed&space;\leq&space;32" target="_blank"><img src="https://latex.codecogs.com/gif.latex?0&space;<&space;Animation&space;Speed&space;\leq&space;32" title="0 < Animation Speed \leq 32" /></a>
