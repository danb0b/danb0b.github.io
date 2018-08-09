---
title: Project Requirements
subtitle: Version 2017-01-23
class_name: EGR598
---
The goal for this project is to use all of the things you are learning in foldable robotics in order to create a small, lightweight foldable robot.

A successful project will achieve the following objectives:

## Checkpoints

* bring a ***new*** prototype to each checkpoint presentation.
* summarize your progress up till now, address feedback, discuss next steps.
* demonstrate improvement upon last design.

## Project Objectives
You should use the content introduced in this course.  All of these points must be addressed in presentations, and must be okayed by the professor.

* **bioinspiration:** Develop a robot inspired by the motion of something in the natural world. 
    * Demonstrate knowledge of your animal.  
    * Translate features and attributes from animal template to robot design.
    * Biomimicry is not required
* **kinematics: ** the robot should have a clear, well-thought-out through transmission design facilitated by the concepts taught in this class (and confimed through analysis).
    * Use a kinematic or dynamic work loop to perform locomotion (rather than rely on friction) or single-path motion.
    * Use a kinematic transmission design to transform rotary or linear actuation into a designed motion path.
    * Analyze the kinematics and dynamics of your system.
    * solve constraint equations and plot motion of transmission using a nonlinear solver
    * compute numerical jacobian of transmission to determine gear ratios
    * Use dynamics software to analyze forces and motion of system.
    * Demonstrate knowledge and mastery of layer-based design and manufacturing topics
* **dynamic: ** the robot should feature some element(s) that require analysis of motion as a function of time, mass, inertia, stiffness, damping, etc.  Ideally, your robot bounces, hops, etc, incorporating those factors into its primary motion.
* **laminate manufacturing: ** This robot should be made using the techniques taught in this class.  3d printing, soft robotics, off-the-shelf parts, and metal should take a back seat.
    * May feature 3d printed connectors for convenience, but must primarily create motion through laminate hinge devices.  
    * Must discuss kinematics with Instructor.
    * Use a five-layer laminate design reflecting design practices outlined in class.
    * Automate the workflow from design parameters to cut files.  Hand-drawn dxf's by the end of this project will not be allowed
* **design: **you should incorporate traditional engineering design principles into your process, by factoring in models, design parameters / variables, and try to optimize or design for some goal via a combination of iterative simulation, prototyping, and/or (ideally) optimization.
* **prototyping:** you should iterate your robot often.  I shouldn't see the same robot 3 weeks in a row.
* **sensing: ** you should know the state of your robot via one or more methods, and use that in your analysis.
    * Example sensors include joint angle sensors, encoders, IMU, voltage/current sensors, etc.
    * External sensing is okay provided you have discussed with the instructor.  Examples include force-plate data, load cell data, etc, for the purposes of verifying models and improving the design.
* **experimentation: ** you should confirm the models you use.  This should be discussed and planned with me early, and planned out with your sensor selection, your kinematic design, and your particular dynamics.  
    * Coordinate this activity with your sensor selection.
* **stiffness analysis:** you should analyze one or more of the structures on your device in order to tune its stiffness / compliance for the intended type of locomotion you need.
    * compute the deflection of a 2d laminate beam design using bernoulli-euler bending equations.
    * Designs should be integrated, analyzed, and tuned in your final device

# Grading Rubric

| item                     | value |
|:-------------------------|:------|
| Checkpoint Presentations | 25%   |
| Submissions              | 25%   |
| Final Report             | 25%   |
| Videos                   | 25%   |

# Submission information
Prepare a single folder with your group that contains all of the following content.  Label the folder using your project name.  A dropbox link will be shared with you during finals week for you to put all your content

##Final Report

The final report will be a cleaned-up version of your weekly reports.  

<!--1. Project Title
1. Full name of all group members with program and degree level.
1. An introduction describing your project theme, biological inspiration, and existing robots which have been based on this template.
1. Summarize the development of each iteration and how one informed the next, in the context of the type of robot you developed, the analysis you performed on it, and the sensing you used to collect data on and inform your design process.
1. Manufacturing and assembly instructions, with labeled photos.  This should be mostly pictorial-based and should permit a total novice to make and assemble your device.
-->
## Videos
* **1-minute overview:** This should present your device according to best possible’ representation.  Select your material for impact and clarity. Edit so that your ideas are as legible as possible to the viewer without extraneous information.
* **5-minute extended video: ** Show the stages of development, both conceptual and physical, ending with your final device. Keep your narrative concise (that is, don’t show too many iterations), but emphasize how each iteration of your design informed your understanding of the final version.  Include
    * Evolution of your design
    * Manufacturing process
    * Sensing & Analysis Results
    * Control Used.

NOTE 1: Primarily we see this as video documentation, but animated rendered material may also be applicable.

NOTE 2: Videos should include a title block in an introductory frame with the project name, and group members, and academic affiliations, as well as the following text:

    EGR598: Foldable Robotics
    Arizona State University
    Fulton Schools of Engineering
    Dan Aukes, Instructor

## Other Files

* **Glamor Shots: ** Publication worthy photos with black or white background and good lighting
* **Manufacturing files** for each iteration
    * CAD designs
    * dxf's
    * python scripts
    * anything else needed to produce the device
* **Microcontroller code** used to run your device.
* **Raw videos and images** collected each week.

## Folder Structure
* final
    * final/design
        * final/design/animations & renderings
        * final/design/python design code
    * final/device
        * final/device/device videos
        * final/device/microcontroller code
        * final/device/photos
    * final/documentation
    * final/final_videos
    * final/glamour_shots
* checkpoint_1
    * checkpoint_1/design
        * checkpoint_1/design/animations & renderings
        * checkpoint_1/design/python_design_code
    * checkpoint_1/device
        * checkpoint_1/device/device_videos
        * checkpoint_1/device/microcontroller_code
        * checkpoint_1/device/photos
    * checkpoint_1/presentation
* checkpoint_2...checkpoint_n
