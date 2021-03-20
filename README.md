##Projectile Motion


 <a href="https://www.codecogs.com/eqnedit.php?latex=\tan&space;(\Theta&space;)x&space;-&space;\frac{g}{2V_{0}^{2}cos^{2}(\Theta&space;)}x^{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\tan&space;(\Theta&space;)x&space;-&space;\frac{g}{2V_{0}^{2}cos^{2}(\Theta&space;)}x^{2}" title="\tan (\Theta )x - \frac{g}{2V_{0}^{2}cos^{2}(\Theta )}x^{2}" /></a>

g >=0

90> Angle >0

Velocity >=0


##Momentum

For two uniform masses (m_a & m_b) travelling at velocities (v_a & v_b) in a one dimensional resistance free environment we can find a solution for both masses in a collision:

 v_a=[m_a*u_a + m_b*u_b + m_b*C_R*(u_b-u_a)]/[m_a+m_b]

and

 v_b=[m_a*u_a + m_b*u_b + m_a*C_R*(u_a-u_b)]/[m_a+m_b]


0< Masses

-10<= Velocities <=10

0<= Coefficient of restitution <=1


##Simple Harmonic Motion



In mechanics and physics, simple harmonic motion is a type of periodic motion where the restoring

 force is directly proportional to the displacement and acts in the direction opposite to that of

 displacement.

Simple harmonic motion can serve as a mathematical model for a variety of motions, such as the

 oscillation of a spring. In addition, other phenomena can be approximated by simple harmonic

 motion, including the motion of a simple pendulum as well as molecular vibration. Simple harmonic

 motion is typified by the motion of a mass on a spring when it is subject to the linear elastic

 restoring force given by Hooke's Law. The motion is sinusoidal in time and demonstrates a single

 resonant frequency. For simple harmonic motion to be an accurate model for a pendulum, the net force

 on the object at the end of the pendulum must be proportional to the displacement. This will be a good

 approximation when the angle of swing is small.

(source-wikipedia.org)



To represent this motion. I used the equation:



 y=Asin(wt)=Asin([(k/m)^1/2]t)



This gave me the displacement for a object in simple harmonic motion and the program lets the user

vary the three variables in the equation to create different movements.

1<= Mass <=10

0.1<= Spring constant <=5

100<= Amplitude <=280

##Orbits

The orbital mechanics of a satellite orbiting around another body are incredibly complex. After many
 weeks of research I was unable to produce an accurate equation allowing me to plot the path of an orbit
 within my abilities.My search brought me to Kepplers equation and many differential computational
 methods of solving it, the equation related mean anomaly, eccentric anomaly and eccentricity but I was
 unable to fully understand this relationship and I had to settle on a less accurate method;



The equation of an ellipse can be written as,

 r=a*(1-e**2)/(1+e*cos(theta))

However this equation when programmed as a animation does not show the satellite as moving faster when nearer
 to the larger planet and slower when further away. To fix this I tried to relate the distance between the
 orbiting bodies to the time that should be waited between each iteration. But through my best efforts I
 was unable to produce a smooth and non-glitchy simulation. The module is patchy and should be ignored for
 those who seek acccuracy.I will hope to finish it one day in the future.

0<= Eccentricity <1

10<= Semi-major axis <=300

0< Speed <=32
