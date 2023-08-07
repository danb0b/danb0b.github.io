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

Stall torque, as you may know, is the highest amount of current a motor can draw during normal operation, when the motor is not moving, or stalled.  This is not a special case -- in robotics applications, your motors may be at rest much of the time.  So whenever you are starting a motor from rest, you will observe a short perio
d wher the motor is using the highest amount of power.  This is related directly to the motors coil resistance and the voltage it is driven ata through Ohm's law, or $V=IR$.  Once the motor starts moving, it generates velocity-dependent back-emf through its coil windings that lowers the amount of current being drawn.  Unfortunately, many robotics applications its actuators are slow-moving or
 even stopped.  This is exacerbated when  motors are used in a synchronous fashion across a system, for example in a legged robot.  Often times, in order to complete a standing, walking, or running gait, two motors will be starting from rest at the same time in different parts of the robot.  This means that the worst case -- this sttartup from rest -- multiplies the current/power needs of a single actuator many times over, potentially.  You always would like to be able to supply power to your system,  even in the worst case, so this impacts your power bottom line by increasing your _current_ needs.

So lets say you have a servo that nominally draws 100 mA while moving at top speed.  You may find that, based on its coil resistance and nominal driving voltage, that it could draw 500-1000 mA in order to start moving!  Considering the current available from AA or AAA batteries, computers' USB ports, 5V chargers, or single-cell lithium ion batteries, you can probably only "afford" to power one or two servos at a time, in the worst-case condition that they start and stop at roughly the same time, sometimes.

Again, you could solve the problem in a "real" system by simply buying a beefy power supply or bigger battery.  But power is expensive, both money-wise, and mass-wise.  So it is in our best interest to find a different way...

What happens when you do draw too much power?  In a typical microcontrollera-driven application, you "pull down" the voltage too much.  For example, if using an ESP32 development board powered by your USB port on your computer (with a 1-2A limit), it needs (let's say) 3.8V in order to supply the microcontroller with the required 3.3V for it to operate.  If you start up several servos simultaneously and pull down the current, you can 1) damage your USB port (not as likely), or at the very least pull down the output voltage below the ESP32 dev board's minimum threshold, causing a "brownout".  Why is this a big deal?  It resets your microcontroller, putting it in an unexpected state.  It can also interrupt the PWM signal being sent to the servos, causing the servo to jiggle or jump.  Jumping servos also act like a start from rest, causing another brownout and another reset sequence.  This can become an endless loop with your microcontroller
 in
