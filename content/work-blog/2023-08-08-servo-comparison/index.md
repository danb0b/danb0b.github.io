---
title: Servo Comparison
date: 2023-08-12
summary: ""
---

<!-- One of the issues with low cost RC servos is their vastly different characteristics.   -->

When I'm developing a course or camp, I often don't have time to do in-depth research on parts or to pre-order multiple rounds of test parts in order to properly research what I need.  But RC servo motors -- to a robotics professor like me -- are one of the cornerstones to teaching half of the sensing & actuation loop so often required of a robotic or embedded system. If the servo doesn't work right, the class stalls out and the students get frustrated!  So, over the years, I've realized I have to find a solution to the following question

> How do I find the cheapest _functional_ RC servos that work with most available sources of power?

This is harder than it might seem.  Even the cheapest RC servo motors are incredibly complex systems, if you think about it.  They include a (plastic) housing, a (plastic) transmission usually composed of multiple gear stages, a motor, feedback, and often a microcontroller or circuit-based control scheme to provide feedback.  And the cheapest servos are only a couple dollars a piece!  So a lot can go wrong.

## Mechanical Issues

* **Stripped gears, splines, or screw threads.**  The plastic in these servos is so cheap that even the smallest over-torque scenario can strip elements of the transmission.
* **Backlash in the transmission.**  Many of the cheapest rc servos forego proper bearings, using the housing itself or small brass bushings instead.  This can warp or
wear quickly when operated above a cheap servo's minimal torque limits, causing the servo to inherit some backlash ("play" or "slop").
* **Poor feedback:**  The potentiometers in these small servos are not very sensitive, and don't provide a lot of position precision.  Sending a command outside of the allowed frequency range can also jam the shaft or cause a mechanical / electrical failure.  I've even seen shafts start to rotate continuously when the commands were outside of the allowable range.

## Electrical issues

* **Over-Voltage:**  Cheap RC servos are not electrically robust, and so operating them outside of their ratings is going to break some of them.  One common mistake is using too high of a voltage.  This can cause either instant death or cause the motor to heat up, melting a lead or coil.
* **Miswiring:**  These servos are also intolerant to reverse voltage situations, because they don't include basic protections built into more complex (expensive) servos.  Plugging in the wrong pins to power and ground is a quick way to destroy a little servo.
* **Overheating:**  Even if rated for 6V, it is sometimes best to use less voltage than that.  Running a servo near stall, or in situations where they're jerking under load will cause little servos to heat up quickly.  Without a metal casing or proper heat sinks, the motors just keep getting hotter until they short and die.

Of course, you can avoid all of these issues simply by paying more for a higher-quality part.  This is what we do in research.  But think about the challenges of teaching a course...each dollar you spend on parts gets multiplied many times over.  A simple robot, consisting of 4 $5 servos, will cost the course 600 dollars for a 30 person class.  Upgrading to a 10 dollar motor with bearings and metal gears costs 600 dollars more!  This is not sustainable in a college setting, let alone a K-12 classroom, even if you utilize project teams to reduce the number of systems.

But, if you do happen to find a servo that avoids the worst of these issues, one of the most pernicious things I've found that crops up, even with a fairly robust, low-cost servo happens as you start to scale up the number of servos in a system, with an issue that relates to stall-torque.

## The Stall Torque Issue

Stall torque, as you may know, is the highest amount of current a motor can draw during normal operation, when the motor is not moving, or stalled.  This is not a special case -- in robotics applications, your motors may be at rest much of the time.  So whenever you are starting a motor from rest, you will observe a short period wher the motor is using the highest amount of power.  This is related directly to the motor's coil resistance and the voltage it is driven at through Ohm's law, or $V=IR$.  Once the motor starts moving, it generates velocity-dependent back-EMF through its coil windings that lowers the amount of current drawn through the coil.  Unfortunately, though, as said before, in many robotics applications actuators are slow-moving or even stopped.  This is exacerbated when  motors are used in a synchronous fashion throughout a system, for example in a legged robot.  Often times, in order to complete a standing, walking, or running gait, multiple motors will be moving in phase with each other, starting from rest at the same time, in different parts of the robot.  This means that the worst case, startup from rest, potentially multiplies the current/power needs from a single actuator many times over.  You always would like to be able to supply power to your system,  even in the worst case, so this impacts your power bottom line by increasing your _current_ needs.

So lets say you have a servo that nominally draws 100 mA while moving at top speed.  You may find that, based on its coil resistance and nominal driving voltage, that it could draw 500-1000 mA in order to start moving!  Considering the current available from AA or AAA batteries, computers' USB ports, 5V chargers, or single-cell lithium ion batteries, you can probably only "afford" to power one or two servos at a time, in the worst-case condition that they start and stop at roughly the same time.

> Again, you could solve the problem in a "real" system by simply buying a beefy power supply or bigger battery.  But power is expensive, both money-wise, and mass-wise.  So it is in our best interest to find a different way...

What happens when you do draw too much power?  In a typical microcontroller-driven application, you "pull down" the voltage from its nominal level, causing it to dip briefly.  For example, if using an ESP32 development board powered by a small battery, and the board needs (let's say) at least 3.8V in order to supply the microcontroller with the required 3.3V to operate.  If you start up several servos simultaneously and pull down the voltage below 3.8V, you could damage your power source, or at the very least pull down the output voltage below the ESP32 dev board's minimum threshold, causing a "brownout".  Why is this a big deal?  It resets your microcontroller, putting it into an unexpected state.  It can also interrupt the PWM signal being sent to the servos, causing the servo to jiggle or jump.  Jumping servos also act like a motor starting from rest, causing another brownout and another reset sequence.  This can become an endless loop, with your microcontroller continually resetting itself, never recovering.

What are some mitigations?  You can add a big capacitor in parallel, to average out the transient peaks.  But that only eliminates short-term peaks.  What about when your power draw over 50-100ms continues to exceed your power supply's available budget?   Another good solution is to power the servo directly from a high capacity lithium ion battery; these have a relatively high current availability (unlike the smaller currents available through chip-basd regulated supplies, small batteries, or USB cables from your computer or a small charger).  But that increased capacity comes at a high cost to the classroom, which we've already said we'd like to avoid.

But, for small, low-power robotics projects, we often don't need that kind of power.  The rest of this article describes my search for motors that didn't need serious mitigation.

## Test Conditions

I tried a number of strategies to find the nominal and worst-case performance of the servos I was testing.  Here are some of them.

### Power

* I tried using USB power from my computer, as well as a 3A, 5V USB charger I found on amazon.  These are both good starting points because they replicate what students will be using when debugging, as well as the cheapest non-computer power source.
* I tested servos with rechargeable AA and AAA lithium ion batteries, as well as some alkaline batteries (Energizer or similar)  Typically, the servos perfomed worse with these batteries than with the wall charger.  I assume their ability to supply peak current is limited and causes more brownouts.
* I tried using one or more 1000uF / 4700uF Electrolytic capacitors across the power rails to smooth out the peaks.  A tantalum capacitor would have probably worked better with fast transient peaks though.
* I used an oscilloscope to verify dips on the vin line, though not across every combination of power, servo, and command, so I can't share those details.

### Servo test conditions

* I ordered 4x of each servo I extensively tested, and tested 1x, 2x, and 4x of each.  
* I played around with the timing of servo startup to reduce instantaneous current requirements, in order to test how multiple servos might work during normal operation.
* I also pushed the limits of the servos to match worst-case conditions.  This was done by commanding large jumps in position, more frequently, and simultaneously across multiple servos

### Code

I used the following code to test 1, 2, and 4 servos.  I set ```l1```, ```l2``` , ```l3```, and ```l4``` to 0 to synchronize their motion so they all moved simultaneously, or to 0, 0.25, 0.5, and 0.75 duty cycle, respectivly, to distribute their motion throughout a cycle. To play with frequency and amplitude I increased ```f``` to 1 or 2 Hz to increase the frequency of cycling.  I increased ```A``` to move from a smooth, sinusoidal motion to a sharper transition (note the use of output limits to protect the servo when increasing A.)

```python
#import all the libraries
# from machine import Pin
# from machine import PWM
import math
import time
from machine import Pin
from machine import PWM

# define constants
# This is the servo's driving frequency, which equals 20ms (1/f=t).
servo_frequency = 50
# This PWM value corresponds to the servo's smallest angle (0)
range_low = 28
# This PWM value corresponds to the servo's largest angle (180)
range_high = 122

# save the initial time in nanoseconds as t0
t0 = time.time_ns()

def angle_to_pwm(degrees):
    '''
    this function converts a desired angle to
    its corresponding PWM value, using the range_low 
    and range_high constants defined inline
    '''
    # compute output scaling
    output_range = range_high-range_low
    # compute input scaling
    input_range = 180-0
    # divide the desired angle by the input scaling, multiply
    #by the output scaling, and add the range_low value as an offset.
    output_pwm = ((degrees/input_range)*output_range)+range_low

    if output_pwm < range_low:
        output_pwm = range_low

    if output_pwm > range_high:
        output_pwm = range_high
        
    # return the computed value as an integer
    return int(output_pwm)

def get_seconds_float():
    '''
    This function accesses the internal time_ns() function and
    converts it to a floating point value in seconds
    '''
    # get current time, t in nanoseconds
    t = time.time_ns()
    # subtract from t0 to obtain the time since the program began
    dt = t-t0
    # convert to a float firsty, and then convert from nanoseconds
    # to seconds by multiplying by 10^9
    dt = float(dt)/1e9
    # return the change in time.
    return dt

f = .5
A = 90
b = 90

l1 = 0
l2 = .25
l3 = .5
l4 = .75

# create a new PWM instance and call it servo1
servo1 = PWM(Pin(13), servo_frequency)
servo2 = PWM(Pin(12), servo_frequency)
servo3 = PWM(Pin(14), servo_frequency)
servo4 = PWM(Pin(27), servo_frequency)

# here is our main loop
while True:
    # time.sleep is not as necessary...can be commented
    # out except if you want to print values out.
    #time.sleep(.01)
    
    # get the current time in (floating-point) seconds
    t = get_seconds_float()

    # compute the desired angle for servo 1
    y1 = A*(math.sin((2*(f*t-l1))*math.pi)) + b
    y2 = A*(math.sin((2*(f*t-l2))*math.pi)) + b
    y3 = A*(math.sin((2*(f*t-l3))*math.pi)) + b
    y4 = A*(math.sin((2*(f*t-l4))*math.pi)) + b

    # print out the desired angle.  Not essential, can be commented out
    print(y1)

    # set servo 1 pwm value according to the desired angle
    servo1.duty(angle_to_pwm(y1))
    servo2.duty(angle_to_pwm(y2))
    servo3.duty(angle_to_pwm(y3))
    servo4.duty(angle_to_pwm(y4))
```

## Results

| Body Style | link                                                                                         | Lowest price per unit | Needed Cap | Brownout at x2 | Brownout at x4 | Notes                                                                       |
| ---------- | -------------------------------------------------------------------------------------------------------- | --------------------- | ---------- | -------------- | -------------- | --------------------------------------------------------------------------- |
| **SG90**   | **[link](https://www.amazon.com/gp/product/B0BJQ2QTHG/ref=ox_sc_act_title_2?smid=A2QTZX14X1D97I&psc=1)** | **1.686875**          | **n**      | **n**          | **n**          | The best one I tested.  Didn’t require a capacitor                          |
| SG90       | [link](https://www.amazon.com/gp/product/B09Y55C21K/ref=ox_sc_act_title_3?smid=A10MX0RD2LYNQR&psc=1)     | 1.888                 | n          | n              | n              | Seemed like a good choice. I broke one easily by mis-wiring it              |
| SG90       | [link](https://www.amazon.com/gp/product/B08KCTQQM8/ref=ox_sc_act_title_6?smid=A2JLTKYCWT3GQ2&psc=1)     | 1.87375               | y          | n              | n              | This servo had some mechanical issues and required a capacitor              |
| MG90S      | [link](https://www.amazon.com/gp/product/B07L6FZVT1/ref=ox_sc_act_title_5?smid=A2QTZX14X1D97I&psc=1)     | 3.1225                | y          | n              | y              | It seemed that 1-2 worked okay, but you could not use four at the same time |
| SG92R      | [link](https://www.adafruit.com/product/169)                                                             | 5.36                  | y          | y              | y              | High stall current caused brownouts, even with 2-3 motors attached.         |
| PS-1171MG  | [link](https://www.amazon.com/gp/product/B07PMBF45T/ref=ox_sc_act_title_7?smid=AOLMYPIAI5LNM&psc=1)      | 10.79                 | ?          | ?              | ?              | too expensive                                                               |
| PDI-1181MG | [link](https://www.amazon.com/gp/product/B07QPM6D5J/ref=ox_sc_act_title_8?smid=AOLMYPIAI5LNM&psc=1)      | 11.99                 | ?          | ?              | ?              | too expensive                                                               |
| ES08A II   | [link](https://www.amazon.com/gp/product/B081YXX77X/ref=ox_sc_act_title_1?smid=A32A7V0ESA8D26&psc=1)     | 10.99                 | ?          | ?              | ?              | too expensive                                                               |

There was a wide range in behavior between seemingly similar servos.  The Adafruit servos have always given me problems with stall current, which was the impetus for my search in the first place.  They jiggled and jerked when I connected anything over 2 servos at the same time.
Some of the other cheap brands I found on Amazon worked under load, at relatively high command frequency, with four servos attached to my computer's USB port or 3A USB charger, all without browning out the microcontroller.  Others needed a capacitor once I got up to 4x connected at the same time under simultaneous commands.
The metal gear servos I purchased, though of seeming higher quality and being slightly more expensive, could not be used 4x at a time without dropping system voltage too low.  Using 2x simultaneously seemed to be the limit.

## Conclusions

I'm writing this mostly from memory about 2 months after running my tests, so I have already forgotton some of the finer details of the procedure, and every permutation I tested.  This writeup is based upon those recollections, so take everything with a grain of salt.
One unfortunate thing I found as writing this up now two months later, however, was that many of the product descriptions, branding, and images on Amazon _have already changed_, and some parts are _already out of stock_.
**Thus, this article is already out of date if you're just looking for my top pick.**

So instead of drawing any direct conclusions about which RC servo to purchase for your class, here are my concluding thoughts:

* Pre-testing the cheapest of the cheap servos is required if you're trying to save money for a big purchase.  Buy more than one of the same servo, and test the number that you expect your students to use simultaneously.
* Use code like that shared above to test best case and worse case conditions.  If you're asking your students to use these, you need to ensure at the very least that they will work under the most basic conditions.
* Test many servo brands before committing.
* Many of the servos you'll find on Amazon are the same, but with different branding / stickers.
* If you're buying from Amazon or similar, buy everything you need all at once, to ensure you get parts from the same product run and source.
* Don't assume your next purchase will meet the same specs.
* Buy extra parts, because you will experience many initial or early failures, and your students will destroy more than you expect due to generally low-quality.
* Consider the cost of your power solution when selecting RC servos.  USB chargers are a cheap option but keep you tethered to a PC or the wall.  Typical AA batteries are heavy and cannot supply high amounts of peak current.
* Consider step-up regulators with a single-cell lithium ion battery.  These seemed like a nice option that kept cost and mass lower, but this solution can add $30 dollars or more to a single system.
