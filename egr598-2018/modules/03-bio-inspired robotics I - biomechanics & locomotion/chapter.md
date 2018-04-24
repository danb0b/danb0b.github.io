---
title: EGR598
subtitle: Biomechanics and Bio-inspired Robots
class_name: EGR598
bibliography: ../../bibliography.bib
csl: ../../ieee.csl
//overlay_text: DRAFT
//font_size: 8pt
---

## Existing Biomechanics Literature

Starting Points:

* On being the right size "A rat is killed, a man is broken, a horse splashes." [@Haldane1964]
* Gravity and life on the ground.[@Vogel2006]
* How Animals Move: An Integrative View[@Dickinson2000]
* Froude number [@Alexander2009]

### People
* Dickenson - Animal Locomotion
* Biewener - Muscles
* McMahon, Herr - Human Running
* Lauder  - fish
* Maciver  - knifefish
* Full - Crabs, Cockroaches, Geckos, etc.
* Autumn - Geckos, Gecko Adhesives
* Goldman - Turtles, Granular Locomotion, Ants, etc.

### Cost of Transport

![cost of transport[@Alexander2005], reprinted from [@Full1989]](figures/cot-alexander-2005.png){width="65%"}  

![peak bone stress[@Biewener1990]](figures/biewener-peak-bone-stress-1990.png){width="65%"}  

![muscle mechanical advantage[@Biewener1990]](figures/biewener-1990-table1.png){width="65%"}  

![safety factors[@Biewener1990]](figures/biewener-1990-table1-2.png){width="65%"}  

\small

| Type of Animal | Animal       |  Subsystem  |            Action             | Reference/Link                                          |
|:---------------|:-------------|:-----------:|:-----------------------------:|:--------------------------------------------------------|
| Mammals        | Humans       |    Legs     |   Bipedal Walking & Running   |                                                         |
| Mammals        | Lemurs       |    Legs     |            Jumping            | Leaping Kinematics[@Demes1996]                          |
| Mammals        | Lemurs       |    Legs     |            Jumping            | External forces during takeoff and landing.[@Demes2005] |
| Mammals        | Orangutangs  |    Legs     |            Jumping            | Cost of Locomotion w/ branches [@Thorpe2007a]           |
| Mammals        | Cheetah      |    Legs     |            Running            |                                                         |
| Mammals        | Cheetah      |    Legs     |            Running            |                                                         |
| Birds          | -            |    Wings    |        Flapping Flight        |                                                         |
| Birds          | -            |    Legs     |            Running            |                                                         |
| Birds          | -            | Wings, Legs |     Wing-Assisted Running     |                                                         |
| Birds          | -            |    Legs     |           Climbing            |                                                         |
| Birds          | Woodpecker   | Legs, Beak  |        Impact Drilling        |                                                         |
| Fish           | -            | Whole Body  |      Undulatory Swimming      |                                                         |
| Fish           | Shark        | Whole Body  |           Swimming            |                                                         |
| Fish           | Rays, Skates |    Wings    |      Undulatory Flapping      | [@Fish2016],[@Cacucciolo2014]                           |
| Reptiles       | -            | Whole Body  | Undulatory Swimming (in sand) | [@Maladen2009]                                          |
| Reptiles       | Gecko        |    Legs     |           Climbing            | [@Autumn2006]                                           |
\normalsize


![jumping forces[@Demes1999]](figures/demes-1999.png){width="65%"}  
![peak forces across other animals[@Demes1999]](figures/demes-1999-2.png){width="65%"}  

<!--
### Kinematics of Animals
### Swimming
### Flapping
### Primates
### Grasping
### Climbing
### Terrestrial Animals
### Human Walking
### Swimming
-->

* Terrestrial vs Swimming [@Biewener1999]
* Comparisons between muscles during locomotion [@Biewener2000]

![muscle comparison[@Biewener2000]](figures/biewener-2000-1.png){width="65%"}

## Other Biological References

### Properties of Biological Materials

It's useful to know the range of material properties that biological systems can achieve.  Soft materials include muscle, cartiledge, tendon.  Strong Materials form the structural elements of biological systems, like skeletons, shells, teeth,

\tiny

| Material                | Chemistry         | Use                                | Modulus(MPa) | Strength(MPa) |
|:------------------------|:------------------|:------------------------------------------------------------------|
| Muscle                  |                   | Power Generation & Storage         |              |               |
| Cartilege               | collagen          | Connection                         |              |               |
| Tendon                  |                   | Power Transmission, Energy Storage |              |               |
| Bone                    | heterogeneous     | Structural                         |              |               |
| Egg Shell               | Calcium Carbonate | Structural                         |              |               |
| Nails and Hooves        | Alpha-keratin     | Protective                         |              |               |
| Exoskeleton (Arthropod) | Chitin            | Structural, Protective             |              |               |
| Tooth                   |                   | Structural                         |              |               |

\normalsize

<!--Shell (Mollusk) | Calcium Carbonate, glycoprotiens, polysaccharides(chitin) | Structural ||-->

### Mechanics of Muscle

![typical muscle curve[@Biewener1999]](figures/biewener-1999-1.png){width="65%"}

## Modeling Efforts

* 1. Maganaris, C. N. & Paul, J. P. human tendon mechanical properties. In Vivo (Brooklyn). 307–313 (1999).[@Maganaris1999]
* "A physiologically based criterion of muscle force prediction in locomotion."[@Crowninshield1981]
* Nice survey on modeling four-bar linkages in biology, with an introduction to four-bar linkages at the beginning [@Muller1996]
* Four-bar mechanisms in fish [@Westneat1990],[@Alfaro2004],[@Westneat2004]
* OpenSim^[<https://simtk.org/projects/opensim>]
* A good paper on a modeling effort [@Hutchinson2004]

## Existing Robotic Platforms

\tiny

| Type of Animal | Animal       |     Subsystem     |             Action             |       Robot Name        | Reference/Link | Image |
|:---------------|:-------------|:-----------------:|:------------------------------:|:-----------------------:|:---------------|:------|
| Mammals        | Humans       |       Legs        |   Bipedal Walking & Running    |          ATLAS          |                |       |
| Mammals        | Humans       |       Legs        |   Bipedal Walking & Running    |           ...           | ...            |       |
| Mammals        | Humans       |       Hands       |    Grasping & Manipulation     |           ...           | ...            |       |
| Mammals        | Cheetah      |       Legs        |            Running             |       MIT Cheetah       |                |       |
| Mammals        | Cheetah      |       Legs        |            Running             | Boston Dynamics Cheetah |                |       |
| Mammals        | Cheetah      |       Legs        |            Running             |       CheetahCub        |                |       |
| -              | -            |       Legs        |            Jumping             |       Penn Jerboa       |                |       |
| -              | -            |       Legs        |            Jumping             |            -            |                |       |
| Birds          | -            |       Wings       |        Flapping Flight         |    RAVEN I, II, etc.    |                |       |
| Birds          | Cassowary    |       Legs        |        Bipedal Walking         |     Cassie, ATRIAS      |                |       |
| Arthropods     | Fly/Bee      |       Wings       |      Flapping-wing Flight      |         RoboBee         |                |       |
| Arthropods     | Mayfly       |       Wings       |      Flapping-wing Flight      |                         |                |       |
| Arthropods     | Butteryfly   |       Wings       |      Flapping-wing Flight      |                         |                |       |
| Arthropods     | Cockroach    |       Legs        |            Running             |          RHex           |                |       |
| Arthropods     | Cockroach    |       Legs        |            Running             |          DASH           |                |       |
| Arthropods     | Cockroach    |       Legs        |            Running             |          ROACH          |                |       |
| Reptiles       | Gecko        |       Legs        |            Climbing            |        Stickybot        |                |       |
| Reptiles       | Turtle       |                   |                                |                         |                |       |
| Reptiles       | Jesus Lizard |                   |                                |                         |                |       |
| Fish           | Rays, Skates | Wings, Whole Body | Flapping (undulatory swimming) |                         |                |       |
| Fish           | -            |    Whole Body     |      Undulatory Swimming       |                         |                |       |
| Fish           | Knifefish    |       Fins        |            Swimming            |                         |                |       |
| Cephalopod     | Octopus      |       Arms        |           Locomotion           |                         |                |       |

\normalsize


## Unexplored Potential Platforms

\small

| Type of Animal | Animal     | Subsystem      | Action                   |
|:---------------|:-----------|:---------------|:-------------------------|
| Arthropods     | Crab       |                | |                        |
| Birds          | Woodpecker | Leg,Beak       | Impact Drilling|         |
| Birds          | Roadrunner | Leg, Body Mass | Running|                 |
| Birds          | -          | Wings, Legs    | Wing-Assisted Running || |

\normalsize

## Bibliography
