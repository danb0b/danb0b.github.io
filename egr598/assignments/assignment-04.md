---
title: Individual Assignment 4
subtitle: Python and Biomechanics
class_name: EGR598
bibliography: ../bibliography.bib
csl: ../ieee.csl
---

## Due: Tuesday, January 23, Before Class, on Blackboard

# Part I
## Assignment Overview

The goal here is to verify you have python installed correctly.  

## Steps
1. Follow the instuctions on blackboard for installing the anaconda distribution of python.
1. Download the windows build for [ffmpeg](https://www.ffmpeg.org/), a common video encoder.  Move it into a new root-level folder called "c:/binaries" or something like that
1. Add that new folder to your system path
    * here's a [tutorial](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)
1. Open up jupyter notebook.  in the command prompt, type
```
jupyter notebook
```
if installed correctly, a browser window should eventually pop open
1. learn how to navigate
1. create a new python 3 notebook.
1. In the first code window enter:  
```
from matplotlib import animation, rc
from IPython.display import HTML
import shapely
import idealab_tools
import foldable_robotics
import pynamics
import pynamics_examples.pendulum_2_ways
```
1. Run that code by hitting shift+enter.  Some information should pop out, along with a blank plot.  There should be a new code window below the first.  In this window, enter:
```
HTML(pynamics_examples.pendulum_2_ways.points_output.anim.to_html5_video())
```
1. run it.  What do you see?
1.  Finally, enter and run this last snippet
```
from foldable_robotics.laminate import Laminate
from foldable_robotics.layer import Layer
import shapely.geometry as sg
box = sg.box(-2,-1,2,1)
box = Layer(box)
circle =sg.Point((0,0))
circle = Layer(circle)<<1.5
lam = Laminate(box,circle)
lam.plot()
```
1. Save your results as a pdf and submit.

## Hints and Ideas

* If you already have Python, it may not be what you need.  We need the most up-to-date version with specific packages installed

---

# Part II
## Assignment Overview
The goal of this part is to encourage you to get "bio-inspired".  

## Steps
1. Read this whole assignment first
1. Find three candidate biological templates (animal, subsystem, action or motion) and the biomechanics papers associated with each.  Search in google scholar using keywords such as "morphology", "mechanics", "biomechanics", "ground reaction forces", etc. along with different animals or motions you are interested in.  
    1. List all the research paper references you can find, in IEEE/MLA/Harvard format.  
    1. If there are many, identify the top 3 citations
    1. It is not critical to have 3 references, but if I search for it, I should not find more than you.
1. For each template, search for existing bio-inspired robots based on the same animal, subsystem, and motion, eg "robots that mimic bonobos' leg systems  for jumping purposes".  
    1. List all the research paper references you can find, in IEEE/MLA/Harvard format.  
    1. If there are many, identify the top 3 citations
    1. It is not critical to have 3 references, but if I search for it, I should not find more than you.
1. Look through these references and identify any opportunities for further research.  What has not been done already?
1. Select one of these templates and find as much information as you can about the parameters associated with this system and motion. Some ideas:
    * body mass, for as many different body parts as possible
    * important materials and their properties
    * kinematics of skeleton / exoskeleton
    * forces and torques
    * motion plots
<!--1. Identify two materials which are integral.  Find  material properties which are critical to the success of this motion (density, tensile strength, modulus of elasticity are some, please think of more for your specific motion)-->
1.  Try to synthesize some information.   For example, if you know ground reaction forces from your paper, and some masses, try to find peak accelerations.  If you know forces and velocities, try to find the power usage.  If you know maximum jump height and mass, find energy required for a jump.  Your template should have some critical information which must be synthesized.
1.  Write this up and submit a pdf.

## Hints and Ideas
* It will be useful to start using a program like Mendeley to collect and organize references.
* Be creative in your search terms. Use [@Dickinson2000] to find good starting points for references and keywords.
* Start writing down search keywords from class.

## Bibliography
