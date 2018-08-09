---
title: Kinematics
class_name: EGR598
bibliography: ../../bibliography.bib
csl: ../../ieee.csl
//overlay_text: DRAFT
//subtitle:
---


Vectors {#sec:Vectors}
=======

A $\vec{v}$ defines a magnitude and direction in $n$-dimensional space.

The concept of a vector comes with a lot of baggage. The first thing you
must think about is how many dimensions are you working in? Two or
three-dimensional space is normal, but the concept of a vector extends
to any dimension.

One way to interpret a vector is the *thing* which describes the
difference in position between two points. But what is a point? I would
argue that a point is a vector, whose magnitude and direction are
referenced from a common origin. So it seems that if we use that
definition, a vector is self referencing.

With the idea of Cartesian space comes the idea of axes – such as x,y,z
axes – which represent orthonormal basis vectors. This allows one to
mathematically define a vector with a set of scalar quantities, which
represent the magnitude along the direction of each basis vector. Given
a set of basis vectors $\hat{a}_x$,$\hat{a}_y$, and $\hat{a}_z$, for
example, one can use three scalar quantities $v_x$, $v_y$, and $v_z$ to
create an arbitrary vector $\vec{v}$ with the expression
\begin{align}
\vec{v} = v_x \hat{a}_x + v_y \hat{a}_y + v_z \hat{a}_z. \label{eqn:vector_basisform}
\end{align}

The $\vec{}$ symbol is used to indicate a vector, while the the $\hat{}$ is used to indicate a vector with a magnitude of $1$ in  $\eqref{eqn:vector_basisform}$.

Scalar Multiplication
---------------------

Vectors can be multiplied by scalars in order to change their magnitude
while preserving their direction. The expression $a\vec{v}$ represents a
vector which is $a$ times the magnitude of $\vec{v}$. Scalars may be
positive or negative; negative scalars indicate an opposite orientation
of the vector.

Vector Addition and Subtraction
-------------------------------

Vectors may be be added together in expressions, and are commutative and
associative.
\begin{align}
\vec{u} + \vec{v} &= \vec{v} + \vec{u} \\
\vec{u} + (\vec{v}+\vec{w}) &= (\vec{u}+\vec{v})+\vec{w}
\end{align}

When multiplied by scalars, vector sums are also distributive
\begin{align}
a(\vec{v}+\vec{w}) &= a\vec{v}+a\vec{w}
\end{align}


Dot Product
-----------

The dot product is defined by the expression
\begin{align}
\vec{v} \cdot \vec{w} &\triangleq \left|\vec{v}\right|\left|\vec{w}\right|\cos{\theta},\label{eqn:vector_dot_product}
\end{align}

where $\left|\vec{v}\right|$ indicates the magnitude of vector
$\vec{v}$. The dot product has many uses. It can be used to determine
the magnitude of a vector, as in
\begin{align}
\left|v\right| &= \sqrt{\vec{v} \cdot \vec{v}}. \label{eq:vector_dot_product_magnitude}\end{align}


The result of a dot product is a scalar number. Since scalar algebra is
distributive and commutative, expressions using the dot product are also
distributive and commutative.
\begin{align}
\vec{u} \cdot \vec{v} &= \vec{v} \cdot \vec{u} \\
\vec{u} \cdot \left(\vec{v}+\vec{w}\right) &= \vec{u}\cdot\vec{v} + \vec{u}\cdot\vec{w} \label{eqn:vector_dot_distributive}\end{align}


Cross Product
-------------

The cross product is defined by the expression
\begin{align}
\vec{v} \times \vec{w} &\triangleq \left|\vec{v}\right|\left|\vec{w}\right|\sin{\theta}\hat{u}, \label{eqn:vector_cross_product}\end{align}

where $\hat{u}$ is the unit vector orthogonal to $\vec{v}$ and
$\vec{w}$, according to the right hand rule. Due to this definition, the
cross product of $\vec{w}\times\vec{v}$ will produce a vector equal in
magnitude and opposite direction to $\vec{v}\times\vec{w}$. Thus, the
cross product can be said to be anticommutative.
\begin{align}
\vec{u} \times \vec{v} &= -\vec{v} \times \vec{u}\end{align}
 The
cross product operator can also be distributed.
\begin{align}
\vec{u} \times \left(\vec{v}+\vec{w}\right) &= \vec{u}\times\vec{v} + \vec{u}\times\vec{w}\end{align}


Exercises {#exercises .unnumbered}
---------

1.  Using , write an expression for a vector $a$ whose magnitude along
    $\hat{a}_x$ is 4, whose magnitude along $\hat{a}_y$ is 7, and whose
    magnitude along $\hat{a}_z$ is -3. \[exercise\_1\]

2.  Using , write an expression for a vector $b$ whose magnitude along
    $\hat{a}_x$ is 1, whose magnitude along $\hat{a}_y$ is 5, and whose
    magnitude along $\hat{a}_z$ is -2.\[exercise\_2\]

3.  Using , expand the expression $\vec{a}\cdot\vec{b}$, using the
    results of \[exercise\_3\]

4.  Look up the term orthogonal on google. What is the angle between two
    orthogonal vectors? What is the magnitude of an unit
    vector?\[exercise\_4\]

5.  Assuming $\hat{a}_x$,$\hat{a}_x$, and $\hat{a}_x$ are orthogonal
    unit vectors, and using , supply the following: \[exercise\_5\]

    a)  $\hat{a}_x\cdot\hat{a}_x = ?$

    b)  $\hat{a}_x\cdot\hat{a}_y = ?$

    c)  $\hat{a}_x\cdot\hat{a}_z = ?$

    d)  $\hat{a}_y\cdot\hat{a}_x = ?$

    e)  $\hat{a}_y\cdot\hat{a}_y = ?$

    f)  $\hat{a}_y\cdot\hat{a}_z = ?$

    g)  $\hat{a}_z\cdot\hat{a}_x = ?$

    h)  $\hat{a}_z\cdot\hat{a}_y = ?$

    i)  $\hat{a}_z\cdot\hat{a}_z = ?$

Expanded basis vector forms
---------------------------

If two vectors $\vec{u}$ and $\vec{v}$ can be expanded into component
basis vectors $\hat{a}_x$,$\hat{a}_y$,and $\hat{a}_z$ such that
\begin{align}
\vec{u}&=u_x\hat{a}_x + u_y\hat{a}_y+u_z\hat{a}_z \text{ and}\\
\vec{v}&=v_x\hat{a}_x + v_y\hat{a}_y+v_z\hat{a}_z,\end{align}
 can
then be rewritten as
\begin{align}
\vec{v} \cdot \vec{w} = (u_x\hat{a}_x + u_y\hat{a}_y+u_z\hat{a}_z) \cdot (v_x\hat{a}_x + v_y\hat{a}_y+v_z\hat{a}_z)\end{align}

which, using the distributive property equals
\begin{align}
\vec{v} \cdot \vec{w} = &u_x\hat{a}_x \cdot v_x\hat{a}_x + u_x\hat{a}_x \cdot v_y\hat{a}_y + u_x\hat{a}_x \cdot v_z\hat{a}_z  + \\
&u_y\hat{a}_y \cdot v_x\hat{a}_x +u_y\hat{a}_y \cdot v_y\hat{a}_y + u_y\hat{a}_y \cdot v_z\hat{a}_z + \nonumber\\
&u_z\hat{a}_z \cdot v_x\hat{a}_x +u_z\hat{a}_z \cdot v_y\hat{a}_y +u_z\hat{a}_z \cdot v_z\hat{a}_z \nonumber\end{align}

grouping scalars,
\begin{align}
\vec{v} \cdot \vec{w} = &u_x v_x (\hat{a}_x \cdot \hat{a}_x) + u_x v_y (\hat{a}_x \cdot \hat{a}_y) + u_x v_z(\hat{a}_x \cdot \hat{a}_z)  + \label{eqn:dot_product_basis_simplification1} \\
&u_y v_x(\hat{a}_y \cdot \hat{a}_x) +u_y v_y(\hat{a}_y \cdot \hat{a}_y) + u_y v_z(\hat{a}_y \cdot \hat{a}_z) + \nonumber\\
&u_z v_x(\hat{a}_z \cdot \hat{a}_x) +u_z v_y(\hat{a}_z \cdot\hat{a}_y) +u_z v_z(\hat{a}_z \cdot \hat{a}_z) \nonumber\end{align}

using the definition of the dot product, we can see that the dot product
of orthogonal basis unit vectors is equal to 0 while the dot product of
a basis vector with itself is equal to 1. This can be summarized by
\begin{align}
\hat{a}_x\cdot\hat{a}_x &= 1\\
\hat{a}_x\cdot\hat{a}_y &= 0\\
\hat{a}_x\cdot\hat{a}_z &= 0\\
\hat{a}_y\cdot\hat{a}_x &= 0\\
\hat{a}_y\cdot\hat{a}_y &= 1\\
\hat{a}_y\cdot\hat{a}_z &= 0\\
\hat{a}_z\cdot\hat{a}_x &= 0\\
\hat{a}_z\cdot\hat{a}_y &= 0\\
\hat{a}_z\cdot\hat{a}_z &= 1\end{align}
 This simplifies to
\begin{align}
\vec{v} \cdot \vec{w} = u_x v_x +u_y v_y+u_z v_z\end{align}


The expression for the cross product can similarly be simplified. Given
the same $\vec{u}$ and $\vec{v}$, can be rewritten as
\begin{align}
\vec{v} \times \vec{w} = (u_x\hat{a}_x + u_y\hat{a}_y+u_z\hat{a}_z) \times (v_x\hat{a}_x + v_y\hat{a}_y+v_z\hat{a}_z)\end{align}

which, using the distributive property equals
\begin{align}
\vec{v} \times \vec{w} = &u_x\hat{a}_x \times v_x\hat{a}_x + u_x\hat{a}_x \times v_y\hat{a}_y + u_x\hat{a}_x \times v_z\hat{a}_z  + \\
&u_y\hat{a}_y \times v_x\hat{a}_x +u_y\hat{a}_y \times v_y\hat{a}_y + u_y\hat{a}_y \times v_z\hat{a}_z + \nonumber\\
&u_z\hat{a}_z \times v_x\hat{a}_x +u_z\hat{a}_z \times v_y\hat{a}_y +u_z\hat{a}_z \times v_z\hat{a}_z \nonumber\end{align}

grouping scalars,
\begin{align}
\vec{v} \times \vec{w} = &u_x v_x (\hat{a}_x \times \hat{a}_x) + u_x v_y (\hat{a}_x \times \hat{a}_y) + u_x v_z(\hat{a}_x \times \hat{a}_z)  + \label{eqn:cross_product_basis_simplification1}\\
&u_y v_x(\hat{a}_y \times \hat{a}_x) +u_y v_y(\hat{a}_y \times \hat{a}_y) + u_y v_z(\hat{a}_y \times \hat{a}_z) + \nonumber\\
&u_z v_x(\hat{a}_z \times \hat{a}_x) +u_z v_y(\hat{a}_z \times\hat{a}_y) +u_z v_z(\hat{a}_z \times \hat{a}_z) \nonumber\end{align}

using the definition of the cross product, we can see that the cross
product of orthogonal basis unit vectors produces an orthogonal unit
vector to both according to the right hand rule, while the cross product
of a basis vector with itself is equal to the zero vector. This can be
summarized by
\begin{align}
\hat{a}_x\times\hat{a}_x &= \vec{0}\\
\hat{a}_x\times\hat{a}_y &= \hat{a}_z\\
\hat{a}_x\times\hat{a}_z &= -\hat{a}_y\\
\hat{a}_y\times\hat{a}_x &= -\hat{a}_z\\
\hat{a}_y\times\hat{a}_y &= \vec{0}\\
\hat{a}_y\times\hat{a}_z &= \hat{a}_x\\
\hat{a}_z\times\hat{a}_x &= \hat{a}_y\\
\hat{a}_z\times\hat{a}_y &= -\hat{a}_x\\
\hat{a}_z\times\hat{a}_z &= \vec{0}\end{align}
 This simplifies to
\begin{align}
\vec{v} \times \vec{w} = u_x v_y\hat{a}_z - u_x v_z\hat{a}_y - u_y v_x\hat{a}_z + u_y v_z\hat{a}_x + u_z v_x\hat{a}_y - u_z v_y\hat{a}_x\end{align}



# rotations and translations

who knows all about rotations
what is a rotation in 2d
what is a rotation in 3d
how do you make a rotation about a point other than 0,0?  definition of affine. what happens when i moulting everything by two?  gets two times further from origin as well. what if I want to
stretch scale and skew and trapezoid
connection between 2d affine transformations and 3d perspective shift... length is preserved not angles  
take a look at your phone straight on

what is translation, what does it look like

matrix form

two steps or one to rotate translate?

define transformation matrix

simple polygon with plot class
sympy to generate rotation matrix.  
do translate, rotate, translate, symbolically and find the theta and displacement elements in combined matrix  
pick center of polygon and scale

\begin{align}
\rightarrow{v} = x\hat{a}_x +y\hat{a}_y + z\hat{a}_z
\end{align}

\begin{align}
\left[
\begin{array}{ccc}
	cos(q) & sin(q) & 0 \\
	sin(q) & cos(q) & 0 \\
	0 & 0 & 1 \\
\end{array}
\right]
\end{align}


Vector Constraint Equations
===========================

v,w perpendicular {#sec:perpendicular_constraint}
-----------------

Here the intuition is that perpendicular lines have an angle of $\theta$
between them. This means that the expression for dot product or cross
product can be used, as both use $\theta$. The dot product produces a
scalar result, however, while the result of a cross product is a vector,
meaning that all three elements of the vector must equal zero; hence we
pick the dot product expression. Using , we substitute
$\theta = \frac{\pi}{2}$ into the expression, resulting in the
simplified
\begin{align}
\vec{v}\cdot\vec{w}=0.\end{align}
 When broken out into basis vectors
$\hat{a}_x$,$\hat{a}_y$,and $\hat{a}_z$, the expression becomes
\begin{align}
v_x w_x +v_y w_y +v_z w_z = 0\end{align}


v,w parallel {#sec:parallel_constraint}
------------

The intuition here is the same as above, except that we substitute the
expression $\theta = 0$ into , because parallel lines have an angle of
zero between them. This results in
\begin{align}
\vec{v}\cdot\vec{w}=|v||w|.\end{align}
 In expanded form, this looks
like
\begin{align}
v_x w_x +v_y w_y +v_z w_z = \sqrt{(v_x^2+v_y^2+v_z^2)(w_x^2+w_y^2+w_z^2)}
\end{align}


point(p) on line(q,r)
---------------------

using the ideas of , we construct two vectors. The first is a vector
between some point on the line, q, and the point p. The second vector is
a vector of the line itself. For the point p to be on the line, the two
lines must be parallel.
\begin{align}
\text{given }\vec{a} &= \vec{p} - \vec{q} \text{ and}\\
\vec{b} &= \vec{r} - \vec{q},\\
\vec{a}\cdot\vec{b} &= |\vec{a}||\vec{b}|.\end{align}


distance between p and q is l {#sec:length_constraint}
-----------------------------

in this case, we create a vector between points p and q, and use to
retrieve its magnitude.
\begin{align}
|\vec{p} - \vec{q}| = l \label{eqn:length_constraint}\end{align}
 In
expanded form,
\begin{align}
\sqrt{(p_x-q_x)^2 +(p_y-q_y)^2 + (p_z-q_z)^2} = l \label{eqn:length_constraint_expanded}.\end{align}


loop constraints
----------------

A loop is a vector that ends where it began. If you think about generic
mechanisms as branching articulated bodies, sometimes those branches
meet back up at their ends to create closed kinematic chains with
interesting motion. One example is the locomotive engine, which consists
of a crank connected to a piston which slides. Other common devices
include four-bar mechanisms, which can be found in pantographs,
prosthetic knees, and the jaws of some fish.

### Loop Example {#loop-example .unnumbered}

There are four vectors, $\vec{a}$,$\vec{b}$,$\vec{c}$, and $\vec{d}$ for
whom
\begin{align}
\vec{a} + \vec{b} + \vec{c}+ \vec{d} =\vec{0}\end{align}
 in expanded
form, with basis vectors $\hat{n}_x$,$\hat{n}_y$,$\hat{n}_z$
\begin{align}
(a_x +b_x + c_x + d_x)\hat{n}_x
+(a_y +b_y + c_y + d_y)\hat{n}_y
+(a_z +b_z + c_z + d_z)\hat{n}_z  \nonumber \\
= 0\hat{n}_x +0\hat{n}_y +0\hat{n}_z\end{align}
This is a vector
equation, however, and we are more interested in generating a set of
scalar equations. To accomplish this, we may dot the entire expresssion
with a basis vector to convert the vector expression into a scalar
expression. This may be done for each of the three basis vectors. For
$\hat{n}_i$, where $i=(x,y,z)$,
\begin{align}
(\vec{a} + \vec{b} + \vec{c}+ \vec{d})\cdot \hat{n}_i &= \vec{0} \cdot \hat{n}_i\text{, resulting in } \\
a_x +b_x + c_x + d_x &= 0\\
a_y +b_y + c_y + d_y &= 0\\
a_z +b_z + c_z + d_z &= 0\end{align}
 We are left with three scalar
constraint equations


Origami Systems
===============

Using the results of the last section, we can finally start to make a
system for analyzing generic origami structures. You can think of an
idealized origami system as a set of rigid faces which are permitted to
rotate about each other at the fold lines. An ideal origami face is
rigid, *i.e.* any motion in the system occurs between faces, along the
fold lines. Rigidity in the faces preserves face edge lengths, and as
discussed in , the distance between two points can be expressed with .
This allows us to create a system of equations which expresses the
motion of the origami system with regard to those fold lines.

Counting Degrees of Freedom
---------------------------

There is a fairly straightforward way to count the number of degrees of
freedom in an origami design. Here are the steps:

1.  Draw your origami structure(black for outline, red for mountain,
    blue for valley)

2.  Split any polygons with $>3$ sides into triangles by adding green
    lines

3.  Draw vertices where any two lines meet

4.  Number each line as $l_i$. Set $m = $ the total number of all
    lines(black,red,blue,green)

5.  Number each vertex as $v_i$. Set $n = $ the total number of
    vertices.

6.  Count $r$, the number of rigid(green) lines

7.  Determine $f$, the degrees of freedom of your system using
    $f = 3n-m-r-6$

Assembling the constraint equations {#sec:origami_constraint_equations}
-----------------------------------

1.  The first set of equations is generated by directly defining the
    locations of one triangular face. For each vertex $v_i$ on such a
    fixed face,
    \begin{align}
    v_{ix} - x_i  = 0\\
    v_{iy} - y_i =0\\
    v_{iz} - z_i=0,
    \end{align}

    where $x_i$, $y_i$ and $z_i$ are the
    positions of each point in x, y, and z coordinates. Repeated over
    the three vertices, this should produce 9 equations.

2.  For each line $l_i$ that is not on the edge of the fixed face, there
    should be two vertices, $v_j$ and $v_k$ connected to it. Using the
    expanded form of the length constraint , create an equation which
    should look like
    \begin{align}
    v_{jx}v_{kx}+v_{jy}v_{ky}+v_{jz}v_{kz} - \ell_i=0,
    \end{align}

    where $\ell_i$ is the length of line $l_i$.
    This should be done $m-3$ times.

3.  For each green line, there is an additional constraint that the two
    neighboring faces are parallel to each other. let vertices $v_i$ and
    $v_j$ be the two vertices shared by the fixed(green) line, and
    vertices $v_a$ and $v_b$ be the remaining vertices of the two faces.

\begin{align}
    \vec{a}=\vec{v}_a - \vec{v}_i \\
    \vec{b}=\vec{v}_b - \vec{v}_i \\
    \vec{c}=\vec{v}_j - \vec{v}_i \\
    \vec{d}=\vec{c}\times\vec{a}\\
    \vec{e}=\vec{b}\times\vec{c}\end{align}
 Using the parallel
    constraint equation generates an extra equation per rigid line,

\begin{align}
    \vec{d} \cdot \vec{e} - |\vec{d}||\vec{e}| = 0.\end{align}
 this
    should be done $r$ times.

There should be a total of $c=9+(m-3)+r$ equations derived from the
above three steps. Alternative derivations are possible, but this recipe
is one of the more straightforward.

Creating the Jacobian
---------------------

Each constraint equation from establishes a relationship between one or
more of the variables that determine the vertices’ positions. By taking
the partial derivative of each equation with respect to each of those
variables, we are able to understand how the velocity of one variable
influences the velocity of the other variables. These partial
derivatives can be assembled into a Jacobian matrix, which can be used
to establish motion profiles for an origami mechanism. Let $\mathbf{e} = \left[\begin{matrix}e_1 &\ldots &e_c\end{matrix}\right]^T,$, where $e_i$ is the $i$th constraint equation. $\mathbf{J}$ can
therefore be defined as

\begin{align}
\mathbf{J} = \left[
\begin{matrix}
\frac{\partial \mathbf{e}}{\partial v_{1x}} & \frac{\partial \mathbf{e}}{\partial v_{1y}} & \frac{\partial \mathbf{e}}{\partial v_{1z}} & \ldots & \frac{\partial \mathbf{e}}{\partial v_{nx}} &\frac{\partial \mathbf{e}}{\partial v_{ny}} & \frac{\partial \mathbf{e}}{\partial v_{nz}}\\
\end{matrix}
\right]
\end{align}

##Computing Jacobians

For a given motion path, it is possible to compute the numerical jacobian of a mechanism throughout its motion path.  We assume you are able to compute the path.

From the last section, it is assumed you can compute the kinematic solution to a set of vector-based constraint equations by supplying a set of input positions(or angles), an initial guess, and computing a valid configuration.


<!--### Forward
### Backward-->
### Trapezoidal Method

1. For a given point $p_i$ find the x,y,z location of $p_{i-1}$ and $p_{i+1}$.
1. compute $\Delta{p}_i$ where
\begin{align}
\Delta{p}_i=\left[\begin{array}{c}
\Delta p_{ix}\\
\Delta p_{iy}\\
\Delta p_{iz}\\
\end{array}\right] = \left[\begin{array}{c}
p_{(i+1)x}-p_{(i-1)x}\\
p_{(i+1)y}-p_{(i-1)y}\\
p_{(i+1)z}-p_{(i-1)z}
\end{array}\right]
\end{align}
1. for each point $p_i$, find $\Delta q_i$ for n input(actuator) angles, where
\begin{align}
\Delta{q}_i=\left[\begin{array}{c}
\Delta q_{i1}\\
\vdots\\
\Delta q_{ij}\\
\end{array}\right] = \left[\begin{array}{c}
q_{(i+1)1}-q_{(i-1)1}\\
\vdots\\
q_{(i+1)j}-q_{(i-1)j}
\end{array}\right]_{j=1...n}
\end{align}
1. compute $J_i$
\begin{align}
J_i = \left[\begin{array}{ccc}
\frac{\partial p_{ix}}{\partial q_{i1}} & \cdots & \frac{\partial p_{ix}}{\partial q_{ij}} \\
\frac{\partial p_{iy}}{\partial q_{i2}} & \cdots &\frac{\partial p_{iy}}{\partial q_{ij}}\\
\frac{\partial p_{ix}}{\partial q_{i3}} & \cdots &\frac{\partial p_{iz}}{\partial q_{ij}}\\
\end{array}\right]_{j=1...n}
\approx \left[\begin{array}{ccc}
\frac{\Delta p_{ix}}{\Delta q_{i1}} & \cdots & \frac{\Delta p_{ix}}{\Delta q_{ij}} \\
\frac{\Delta p_{iy}}{\Delta q_{i2}} & \cdots &\frac{\Delta p_{iy}}{\Delta q_{ij}}\\
\frac{\Delta p_{ix}}{\Delta q_{i3}} & \cdots &\frac{\Delta p_{iz}}{\Delta q_{ij}}\\
\end{array}\right]_{j=1...n}
\end{align}

### Compute Joint Torques
The Jacobian helps transform
Virtual power

\begin{align}
P_{in} &= \vec{\tau}\cdot\vec{\omega}=\omega^T\tau \nonumber\\
P_{out} &= \vec{f}\cdot \vec{v} = v^Tf\\
v &= J\omega\\
P_{in}&=P_{out}\\
\omega^T\tau &= v^Tf\\
&= (J\omega)^Tf\\
&= \omega^TJ^Tf\\
\tau &= J^Tf\label{a}
\end{align}
