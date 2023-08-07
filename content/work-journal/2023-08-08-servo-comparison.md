---
title: Servo Comparison
draft: true
---

One of the issues with low cost RC servos is their vastly different characteristics.  When I'm developing a course or camp, I often don't have time to do in-depth research on parts or to pre-order multiple rounds of test parts in order to properly research what Ineed.

However, RC servo motors -- to a robotics professor like me -- are one of the cornerstones to teaching half of the sensing & actuation loop so often required of a robotic or embedded system.
If the servo doesn't work right, there is a learning gap.  So, over the years, as I've hit the challenge of 
"how do you find cheap (and I mean _cheap_) rc servos that can survive for a week or even a semester, that behave nicely when you try to use 4-6 of them off the same low power microcontroller?"

Tis is harder than it might seem.  RC servo motors are incredibly complex systems, if you think about it.  They include a housing, a transmission usually composed of multiple gear stages, a motor, feedback, and often a microcontroller or circuit-based control scheme to provide feedback.  And the cheapest servos are only a couple dollars a piece!

Typical mechanical issues:

* stripped gears, splines, or screw threads.  The plastic in these servos is so cheap that even the smallest over-torque scenario can strip elements of the transmission.
* slop in the transmission.  Many of the cheapest rc servos forego proper bearings, using the housing itself or small brass bushings instead.  This can warp or 
wear quickly when operated above a cheap servo's minimal torque limits, causing the servo to inherit some mechanical X, or slop.

Electrical issues:

* over-voltage
* miswiring
* overheating

If you find a servo that avoids the worst of these issues, One of the most pernicious issues that 
* current issues
