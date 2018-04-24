---
title: GROUP Assignment 8
subtitle: Numerical Jacobians
class_name: EGR598
bibliography: ../bibliography.bib
csl: ../ieee.csl
---

## Overview

The purpose of this exercise is to concretely identify the forces and torques involved with at least one mechanism in your system.  

## Procedure

1. Propose an origami-inspired / foldable mechanism.  This does not need to be the entire device, but on the scale of a leg, manipulator, hand, or other biological subsystem.
1.  Make the device in paper.  This should have already been done for your last presentation, but you need an up-to-date model if it has changed.  The paper model should dimensionally match your code.
1. Plot the kinematics of your device using the method you learned in HW7.  You may use an alternate method but see the instructor for an ok if you plan on starting down this road.
1. Select an output point(end-effector). This can / should be a point on your device where forces and/or torques will be transmitted to something else, like the ground, an object, etc.  Plot its motion.
1. If applicable, select a portion of the path corresponding to a known force condition(such as the stance phase of walking).  This depends on your motion and should be explained.
1. Numerically compute the Jacobian of your device by computing the differential output motion over the differential input motion of each / all motors.  If you have a multi-DOF mechanism, compute a subspace of the volume/surface/path the output traces and find the numerical Jacobian of that.
1. Now is a good time to start thinking about the (heavy) parts you will need, specifically motors/servos, batteries, etc.  Select a motor where the stall current, stall torque, no-load speed, free-running current, and mass are available from the manufacturer.  You will be using these values later.
1. Compute a mass budget estimate for your device based on your parts list and multiply by the acceleration due to gravity.  Divide by the number of legs/feet/hands/fins which will be sharing this load.
1. From knowledge of your biological analog, calculate the forces which you expect will be exerted at the end-effector due to accelerations.
1. Using the formula $\tau=J^Tf$, determine required motor torques based on estimated end-effector forces using the Jacobian you calculated.
1. Find motors which can exert required torques, update your mass budget, and then repeat all steps until your device can locomote under its own weight.  Feel free to use any optimization tools at your disposal to accelerate this iterative process.

Detail these steps in your writeup.  This can be done all in a jupyter notebook.  For teams who present next, use this assignment as the basis for your next presentation.
