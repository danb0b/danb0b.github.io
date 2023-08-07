---
title: Servo Comparison
draft: true
---

One of the issues with low cost RC servos is their vastly different characteristics.  When I'm developing a course or camp, I often don't have time to do in-depth research on parts or to pre-order multiple rounds of test parts in order to properly research what Ineed.

However, RC servo motors -- to a robotics professor like me -- are one of the cornerstones to teaching half of the sensing & actuation loop so often required of a robotic or embedded system.
If the servo doesn't work right, there is a learning gap.  So, over the years, as I've hit the challenge of 
"how do you find cheap (and I mean _cheap_) rc servos that can survive for a week or even a semester, that behave nicely when you try to use 4-6 of them off the same low power microcontroller?"

Tis is harder than it might seem.  Even the cheapest RC servo motors are incredibly complex systems, if you think about it.  They include a (plastic) housing, a (plastic) transmission usually composed of multiple gear stages, a motor, feedback, and often a microcontroller or circuit-based control scheme to provide feedback.  And the cheapest servos are only a couple dollars a piece!

Typical mechanical issues:

* stripped gears, splines, or screw threads.  The plastic in these servos is so cheap that even the smallest over-torque scenario can strip elements of the transmission.
* slop in the transmission.  Many of the cheapest rc servos forego proper bearings, using the housing itself or small brass bushings instead.  This can warp or 
wear quickly when operated above a cheap servo's minimal torque limits, causing the servo to inherit some mechanical X, or slop.

Electrical issues:

* over-voltage
* miswiring
* overheating

Of course, you can avoid all of these issues simply by paying more for a higher-quality part.  This is what we do in research.  But think about the challenges of teaching a course...each dollar you spend on parts gets multiplied many times over.  A simple robot, consisting of 4 servos, will cost the course 4 \* 30 \* $5 = $600 for a 30 person class.  Upgrading to a $10 motor with bearings and metal gears costs $600 more!  This is not sustainable in a college setting, let alone a K-12 classroom, even if you utilize project teams to reduce the number of systems.

But, if you do happen to find a servo that avoids the worst of these issues, One of the most pernicious things I've found that crops up, even with a fairly robust, low-cost servo happens as you start to scale up the number of servos, and this relates to the stall-torque.

Stall torque, as you may know, is the highest amount of current a motor can draw during normal operation, when the motor is not moving, or stalled.  This is not a special case -- in robotics applications, your motors may be at rest much of the time.  So when ever
* current issues
