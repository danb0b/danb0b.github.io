---
title: GROUP Assignment 5
subtitle: Back of the Envelope Calculations
class_name: EGR598
bibliography: ../bibliography.bib
csl: ../ieee.csl
---

## Due: Thursday, January 25, Before Class, on Blackboard

## Assignment Overview

The goal of this assignment is to get you thinking about the scale of your robot, and your ability to replicate the efficiencies of biological muscle.

## Steps

1. Using the results from Tuesday's assignment (or at least the same methods), please find the answer to as many of these questions as possible, for your team's animal / subsystem / motion(gait).
    * What is the animal / subsytem / motion(gait) pair you are studying?
    * List the biomechanics references you have already found
    * List other bio-inspired robots based on the same platform
    * List the typical body mass, for as many different body parts as possible
    * Find other values
        * speed of the animal while walking / running
        * if running, does the animal leave the ground?
        * typical stride length
        * maximum height off the ground in a stride

1. What is the total energy used to complete a single locomotion cycle?  What is the power required?  How did you calculate this?
1. How much respiration energy / power is used?  If you can't find it, are there references for a similar animal you could scale?  Can you find a reference that tells you how to scale respiration energy across different size animals?
1. Find the ground reaction forces involved with completing a typical locomotion cycle.  
    * A figure from literature (with the appropriate references) of the animal during a locomotion cycle typical of the one you are studying will suffice.  Make sure you include the units
1. Supply a figure from literature of the animal's skeleton, exoskeleton, shell, rigid structure.  How many moving parts are there in the biological system?
1. Draw the simplest representation of the system you can. How many rigid bodies are there?  How many can be approximated as massless(1/10 of the total mass or less)?  Where are the springs?  Where is the (main) motor?
1. Draw free body diagrams for those bodies.
1. Based on mass  a knowledge of the duration and magnitude of the ground/world reaction forces involved in a single stride, what forces/torques would be required at the motor to add enough energy to the system at the ground?  What power?
1. Look online for a motor and battery which can supply that power.  Motor efficiencies may be as high as 95%, but let's assume you find a cheap motor near 50-60% efficiency.  How much does it weigh?  What are the mechanical watts/kg for motor/battery vs animal?  Which one is more efficient?  What about after you factor in your structure weight?
1. Discuss whether/how you will need to scale your robot up or down, or how you can mitigate the differences.

## Links
* https://en.wikipedia.org/wiki/Kleiber%27s_law
* http://biomch-l.isbweb.org/archive/index.php/t-24548.html

[@Bennett1985],[@Kramer2011],[@DeLong2010],[@Makarieva2008],[@Hanna2011],[@Taylor1982],[@Weir1949]

## Bibliography
