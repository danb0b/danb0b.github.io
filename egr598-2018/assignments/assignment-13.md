---
title: INDIVIDUAL Assignment 13
subtitle: RC Servos & Pro Trinket
class_name: EGR598
bibliography: ../bibliography.bib
csl: ../ieee.csl
---

## Overview

Your assignment is to connect to and program a microcontroller connected to an RC servo.

## Steps

1. Follow the instructions in lecture 19, the adafruit tutorial on blackboard, and/or the website for the adafruit pro trinket in order to set up your computer for downloading programs using the USB bootloader.
1. Load the servo--> sweep demo and save to a new file.  Edit the attach command to work with an address on the pro trinket (like "A0").  Test this code with your servo.  You can use this code as a starting point. (Then make sure you plug your servo's signal plug into pin "A0" as well.)
1. Create a program which approximates a sine wave to your servo. Your program should contain four variables which determine how your servo moves:  amplitude, offset, frequency, and time_division.
    * The amplitude variable should reflect a percentage of the servo's total range from 0 to 1.  1 meaning the servo hits its (mechanical) positive and negative travel limits, 0 meaning a DC signal.  Eliminate any dead zones in your amplitude variable by shifting and scaling your 0-1 range to match the limits that your pwm signal can actually move the servo, if necessary.  
    * if the amplitude is zero, a zero offset should reflect a DC signal where the output of your servo rests halfway between positive and negative limits of your motor. an offset of .5 should make your servo reach it maximum, and an offset of -.5 should make your servo reach its minimum limit.
    * your frequency variable should be used in conjunction with the time_division variable to assert a sleep command which divides up time in your sine wave to approximate the sine wave.  The frequency should be supplied in Hz and the time_division variable determines the number of approximate segments your sine wave is divided into within a single cycle.
    <!--* **optional:** learn how interrupts work in order to update your pwm command with a timer based interrupts instead of a sleep command.-->

## Discussion

1. What is the maximum and minimum command(value range you send from the pro trinket) that produces a response in your motor?  What is the maximum range in degrees that your motor is able to achieve?  
1. What is the maximum frequency you can command at an amplitude of 1 before you notice the amplitude decreasing?
1. What value of time_division at this .5 Hz produces a smooth motor output?
1. create a video(or 8 short **labeled** videos) demonstrating how you can change these three values to generate different sine-wave sweeps.  Show the following cases.

    | case | amplitude | offset | frequency | divisions |
    |-----:|:---------:|:------:|:---------:|:---------:|
    |    1 |     0     |   .5   |     4     |    100     |
    |    2 |     0     |  -.5   |     4     |    100     |
    |    3 |    .1     |   .4   |     4     |    100     |
    |    4 |    .1     |  -.4   |     4     |    100     |
    |    5 |      1     |   0    |    4     |    100     |
    |    6 |      1     |   0    |    1     |    100     |
    |    7 |      1     |   0    |    .5     |    100     |
    |    8 |    1     |   0    |    .5     |    20     |

1. Briefly comment about the limitations of this servo in the context of each of these tests.  
<!--
1. **optional** demonstrate a sawtooth wave generator as well
-->



## Submission Info
Submit your arduino code, writeup, and video demonstration to blackboard in a single zip file.

## Links

* Adafruit pro trinket website: <https://www.adafruit.com/product/2000>
* pro trinket tutorial: <https://learn.adafruit.com/introducing-pro-trinket>
* arduino IDE setup for adafruit products <https://learn.adafruit.com/adafruit-arduino-ide-setup/overview>
