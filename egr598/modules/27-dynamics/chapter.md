---
title: EGR598
subtitle: Dynamics
class_name: EGR598
bibliography: ../../bibliography.bib
csl: ../../ieee.csl
//overlay_text: DRAFT
//font_size: 8pt
---


## Lesson 1: Golden Rule

$$
\frac{\prepost{N}{}{d\vec{v}}{}{}}{dt} = \frac{\prepost{A}{}{d\vec{v}}{}{}}{dt} + \prepost{N}{}{\vec{w}}{A}{} \times \vec{v}
$$

![double pendulum](figures/double_pendulum.png){height="2in"}

------------

## Lesson 2: Rotation Matrices

![rotation between frames](figures/rotation_matrix.png){height="2in"}

$$
\begin{array}{c|c c c}
  \prepost{N}{}{\textbf{R}}{A}{}& \hat{a}_x &\hat{a}_y & \hat{a}_z\\
  \hline
  \hat{n}_x &\cos q&-\sin q &0 \\
  \hat{n}_y &\sin q& \cos q &0 \\
  \hat{n}_z &0&0&1
 \end{array}
$$

Multiple rotations:

$$
\prepost{N}{}{\textbf{R}}{B}{} = \prepost{N}{}{\textbf{R}}{A}{} \prepost{A}{}{\textbf{R}}{B}{}
$$

------------

## Lesson 3: Golden Rule, Continued
![body moving through space](figures/body_in_space.png){height="2in"}

find the cartesian velocity of point q

$$\begin{aligned}
\vec{r}_1 &= x_1 \hat{n}_x + y_1 \hat{n}_y + z_1 \hat{n}_z \\
\vec{r}_2 &= x_2 \hat{n}_x + y_2 \hat{n}_y + z_2 \hat{n}_z \\
\prepost{N}{}{\vec{\omega}}{A}{} &= \omega_x \hat{n}_x + \omega_y \hat{n}_y + \omega_z \hat{n}_z
\end{aligned}$$



$$
\begin{array}{c|c c c}
  \prepost{N}{}{R}{A}{} & \hat{a}_x & \hat{a}_y & \hat{a}_z \\
  \hline
  \hat{n}_x &r_{11}&  r_{12}&r_{13} \\
  \hat{n}_y &r_{21}& r_{22} &r_{23} \\
  \hat{n}_z &r_{31}&r_{32}&r_{33}
 \end{array}
$$

------------

## Lesson 4: Four Bar Kinematics
write the constraint equations in several methods


![four bar mechanism](figures/fourbar.png){height="2in"}

## Lesson 5: Particles

* No Inertia, No Angular Momentum, no Angular Velocity
* Just mass at a point

------------

## Lesson 6: Kane's method

![pendulum](figures/pendulum.png){height="2in"}

$$\begin{aligned}
\vec{r} &= -l\hat{a}_y \\
\vec{v} &= \frac{\prepost{N}{}{ d\vec{r}}{}{}}{dt} = \frac{\prepost{A}{}{ d\vec{r}}{}{}}{dt} + \prepost{N}{}{\vec{\omega}}{A}{} \times \vec{r}\\
\vec{v} &= \frac{\prepost{N}{}{ d\vec{r}}{}{}}{dt} = \dot{\theta}\hat{a}_z \times -l\hat{a}_y \\
\vec{v} &= \frac{\prepost{N}{}{ d\vec{r}}{}{}}{dt}= l\dot{\theta}\hat{a}_x \\
\vec{a} &= \frac{\prepost{N}{}{ d\vec{v}}{}{}}{dt} = \frac{\prepost{N}{}{d^2\vec{r}}{}{}}{dt^2}\\
\vec{a} &=  \frac{\prepost{A}{}{d\vec{v}}{}{}}{dt} + \prepost{N}{}{\vec{\omega}}{A}{} \times \vec{v} \\
\vec{a} &= l\ddot{\theta}\hat{a}_x  + \dot{\theta}\hat{a}_z \times l\dot{\theta}\hat{a}_x \\
\vec{a} &= l\ddot{\theta}\hat{a}_x  + l\dot{\theta}^2\hat{a}_y
\end{aligned}$$

Frame A

* $\prepost{N}{}{\vec{\omega}}{A}{} = \dot{\theta} \hat{n}_z= \dot{\theta} \hat{a}_z$

Speed variables

* $\dot{\theta}$

All the forces in the system

* Two tension forces, one at point $p$ one at point $o$
* One gravity force

Partial Velocities

* partial velocity of particle
* $v_{p1} = v$
* partial velocity of f1, f2,f3
* $v_{f1} = 0$
* $v_{f2} = v$
* $v_{f3} = v$

Generalized effective force of a particle
$$
\prepost{N}{}{F}{Q}{u_r} = \frac{\partial{^N\vec{v}^Q}}{\partial u_r} \cdot  \left(m^Q* \prepost{N}{}{\vec{a}}{Q}{}\right)
$$

Kane's Equation for a system of particles and masses for speed variable $u_r$, $m$ forces, $n$ moments, $o$ particles, and $p$ bodies
$$
\sum_{i=1}^{m}{\vec{f}_i} \cdot \frac{\partial\vec{v}_{\vec{f}_i}}{\partial u_r} + \sum_{j=1}^{n}{\vec{\tau}_j} \cdot \frac{\partial\vec{\omega}_{\vec{\tau}_j}}{\partial u_r} = \sum_{k=1}^{o}\frac{\partial\vec{v}_{k}}{ \partial u_r} \cdot m_{k}\vec{a}_{k} +    \sum_{l=1}^{p}\left( \frac{\partial\vec{v}_{l}}{\partial u_r} \cdot m_{l}\vec{a}_{l} +
\frac{\partial\vec{\omega}_{l}}{\partial u_r} \cdot \left( \overrightarrow{I}_{l}\cdot\vec{\alpha}_l
+ \vec{\omega}_l \times \overrightarrow{I}_{l}\cdot\vec{\omega}_l
\right) \right)
$$

----------------

## Lesson 7: Springy Mass

now $l$ from the last problem is a spring

### Output
![Figure_1.png](figures/Figure_1.png){width="50%"}

### Code

```{python}
# -*- coding: utf-8 -*-
"""
Written by Daniel M. Aukes
Email: danaukes<at>gmail.com
Please see LICENSE for full license.
"""

import pynamics
pynamics.script_mode = False

from pynamics.frame import Frame
from pynamics.variable_types import Differentiable,Constant
from pynamics.system import System
from pynamics.body import Body
from pynamics.dyadic import Dyadic
from pynamics.output import Output
from pynamics.particle import Particle

#import sympy
import numpy
import scipy.integrate
import matplotlib.pyplot as plt
plt.ion()
from sympy import pi
system = System()

lA = Constant(1,'lA',system)

mA = Constant(1,'mA',system)

g = Constant(9.81,'g',system)
#b = Constant(1e0,'b',system)
k = Constant(3e2,'k',system)

Ixx_A = Constant(1,'Ixx_A',system)
Iyy_A = Constant(1,'Iyy_A',system)
Izz_A = Constant(.3,'Izz_A',system)


tinitial = 0
tfinal = 10
tstep = .001
t = numpy.r_[tinitial:tfinal:tstep]

preload1 = Constant(0*pi/180,'preload1',system)

q,q_d,q_dd = Differentiable('q',system)
x,x_d,x_dd = Differentiable('x',system)

initialvalues = {}
initialvalues[q]=30*pi/180
initialvalues[q_d]=0*pi/180
initialvalues[x]=1
initialvalues[x_d]=0

statevariables = system.get_state_variables()
ini = [initialvalues[item] for item in statevariables]

N = Frame('N')
A = Frame('A')

system.set_newtonian(N)
A.rotate_fixed_axis_directed(N,[0,0,1],q,system)

pNA=0*N.x
pAB=pNA-x*A.y
vNA=pNA.time_derivative(N,system)
vAB=pAB.time_derivative(N,system)
aAB = vAB.time_derivative(N,system)

#ParticleA = Particle(pAB,mA,'ParticleA',system)
IA = Dyadic.build(A,Ixx_A,Iyy_A,Izz_A)
BodyA = Body('BodyA',A,pAB,mA,IA,system)

stretch = x-lA
direction = -A.y
#system.addforce(-b*vAB,vAB)
system.addforce(-k*stretch*A.y,vNA)
system.addforce(k*stretch*A.y,vAB)
#system.add_springforce(k*stretch*A.y,vAB)
#system.addforce(b*x_d*A.y,vAB)
system.addforcegravity(-g*N.y)

x1 = BodyA.pCM.dot(N.x)
y1 = BodyA.pCM.dot(N.y)

pynamics.tic()
print('solving dynamics...')
f,ma = system.getdynamics()
print('creating second order function...')
func = system.state_space_post_invert(f,ma)
print('integrating...')
#from pynamics.integrator import RK4,DoPri
#integrator = RK4(func,ini,t)
#integrator = DoPri(func,ini,t)
#states = integrator.run()
states=scipy.integrate.odeint(func,ini,t,rtol=1e-12,atol=1e-12,hmin=1e-14, args=({'constants':system.constant_values},))

pynamics.toc()
print('calculating outputs..')

KE = system.get_KE()
PE = system.getPEGravity(pNA) - system.getPESprings() - 1/2* k*(stretch)**2

output = Output([x1,y1,q,KE-PE],system)
y = output.calc(states)
pynamics.toc()

plt.figure(1)
plt.plot(y[:,0],y[:,1])
plt.axis('equal')

plt.figure(2)
plt.plot(y[:,3])

#plt.figure(3)
#plt.plot(t,y[:,0])
#plt.show()
```

----------------

## Lesson 6: Cart Pendulum

```{python}
# -*- coding: utf-8 -*-

import pynamics
from pynamics.frame import Frame
from pynamics.variable_types import Differentiable,Constant
from pynamics.system import System
from pynamics.body import Body
from pynamics.dyadic import Dyadic
from pynamics.output import Output
from pynamics.particle import Particle

#import sympy
import numpy
import scipy.integrate
import matplotlib.pyplot as plt
plt.ion()
from sympy import pi
system = System()

l = Constant(.5,'l',system)
xO = Constant(1.0, 'xO',system)

M = Constant(10,'M',system)
m = Constant(2,'m',system)


I_xx = Constant(9,'I_xx',system)
I_yy = Constant(9,'I_yy',system)
I_zz = Constant(9,'I_zz',system)

g = Constant(9.81,'g',system)
b = Constant(1e2,'b',system)
k = Constant(1e4,'k',system)

tinitial = 0
tfinal = 10
tstep = .01
t = numpy.r_[tinitial:tfinal:tstep]

x,x_d,x_dd = Differentiable('x',system)
q,q_d,q_dd = Differentiable('q',system)

initialvalues = {}
initialvalues[x]=0.0
initialvalues[x_d]=0

initialvalues[q]=30*pi/180
initialvalues[q_d]=0*pi/180


statevariables = system.get_state_variables()
ini = [initialvalues[item] for item in statevariables]

N = Frame('N')
A = Frame('A')

system.set_newtonian(N)
A.rotate_fixed_axis_directed(N,[0,0,1],q,system)

p1 = x*N.x
p2 = p1 - l*A.y
v1 = p1.time_derivative(N,system)
v2 = p2.time_derivative(N, system)

I = Dyadic.build(A,I_xx,I_yy,I_zz)

BodyA = Body('BodyA',A,p2,m,I,system)
ParticleO = Particle(p1,M,'ParticleO',system)


stretch = x-xO
system.add_spring_force1(k,(stretch)*N.x,v1)
system.addforce(-b*v1,v1)
system.addforcegravity(-g*N.y)

eq = []

eq_d= [system.derivative(item) for item in eq]
eq_dd= [system.derivative(item) for item in eq_d]

pynamics.tic()
print('solving dynamics...')
f,ma = system.getdynamics()
print('creating second order function...')
#func1 = system.state_space_pre_invert(f,ma,constants = system.constant_values)
func1 = system.state_space_post_invert(f,ma,eq_dd,constants = system.constant_values)
print('integrating...')
states=scipy.integrate.odeint(func1,ini,t,rtol=1e-3,atol=1e-3,args=({'constants':{},'alpha':1e2,'beta':1e1},))
pynamics.toc()
print('calculating outputs..')

# =============================================================================
KE = system.get_KE()
PE = system.getPEGravity(0*N.x) - system.getPESprings()
energy = Output([KE-PE])
energy.calc(states)
energy.plot_time()
# =============================================================================
points = [p1,p2]
points = [item2 for item in points for item2 in [item.dot(N.x),item.dot(N.y)]]
points = Output(points)
y = points.calc(states)
y = y.reshape((-1,2,2))

plt.figure()
plt.plot(y[:,1,0],y[:,1,1])
plt.axis('equal')

states2= Output([x,q])
states2.calc(states)

plt.figure()
plt.plot(states[:,0])
plt.figure()
plt.plot(states[:,1])
```
