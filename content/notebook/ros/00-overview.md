---
---

## Introduction

The purpose of this project is to document our implementation of ROS and teach lab members how to use it for a number of purposes specific to the activities of a robotics lab like the IDEAlab.

In contrast with its name, ROS is not an operating system.  It is a way to have vast, disparate sources of data come together in networked way in order to perform tasks important to robotics, such as simulation, sensing, control, learning, and teleoperation.  It coordinates the transfer of information from one place to another in a way that is scalable

## Integration

The IDEAlab has a number of disparate pieces of hardware, each of which is controlled using a mix of standardized and proprietary protocols.  It is important to be able to access that data in a standardized way so that we can run experiments more efficiently

Each device typically has an API or protocol that we can use to communicate with it, but these protocols are not standardized (nor should they be).  In the past, when creating experimental data collection setups, we would write individual Matlab or Python-based scripts to communicate with the specific devices we needed. This led to non-standardized code with situation-specific instructions making it difficult to reuse the code for new purposes, limiting sharing. Secondly, as multiple devices were often integrated together within some sort of while loop, communication from multiple sources at different rates led to common problems with buffering and asynchronous communication, leading to poor performance.  Through ROS, we have more control over each devices communication rate in a way that is non-blocking and variable depending on need.

## High Level Overview

There are a variety of terms used for the parts of ROS, and while there are good tutorials out there, it is nice to see a quick summary of terms in one place.

| Item        | Description                                                                                                                            |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| Master      | the computer that coordinates communication sent over ROS                                                                              |
| Node        | A node is a program compiled to interact with ros topics.  Nodes can be run on different PC's and communicate over communication layer |
| Service     | Like a node, except that services respond to requests rather than publish at their own discretion                                      |
| Message     | particular data type that gets passed between nodes                                                                                    |
| Topic       | A category of messages that a node can subscribe to                                                                                    |
| Package     | collections of nodes, messages, and data types that work together as a project.  They are written in python and/or C++                 |
| launch file | a method for starting up a number of ros nodes, services and topics. synchronizes the startup of ros stuff                             |
| publish     | how to send data over ROS                                                                                                              |
| subscribe   | how to select and receive data published over ROS                                                                                      |

## Devices

Some examples of the types of devices we need to communicate with include:

* Ethernet-based data from standalone robotic systems
    * UR-5 and UR-5e
    * Wifi-based microcontrollers suh as the Photon.
    * ATI LAN-based sensors
* Camera data from USB webcams or ethernet-accessible computers like the Raspberry Pi.
* Ethernet-based motion tracking systems like Optitrack.
* USB-based devices connected to a local or remote computer
    * Novint Falcon
    * Thorlabs Linear Stage
    * Serial over USB data to/from microcontrollers connected to a computer, for custom sensing
        * Accelerometer Data from I2C based chips
        * Current data from current sensing chips
        * Analog data from I/O pins
    * Dynamixel Servos
    * Load Cells
* PCI-card-based devices with drivers available only in Windows, like NI hardware
* etc...

The variety of these devices, their connection to a computer, and their specific constraints, is the reason we have chosen ROS for our integration effort.  We have determined that ROS can satisfy those needs while remaining relatively accessible to students in terms of the learning curve and complexity.

## ROS Capabilities

ROS is capable of performing a number of tasks critical for robotics research

### Data Collection

Once routed into ROS, it is important to select which pieces of data to gather, process and publish.  Our needs at this point are mostly related to collection, processing, filtering, and recording that data.  Future work will relate to closing the loop with control.

### Data Processing

Data can be processed within the ROS environment.  One standard way to do that would be to have a separate node -- a program that runs within its own process -- subscribing to a stream of data, doing something with it, and then publishing a derivative of that work.  Examples include

* taking camera data from two cameras and to combine it into a 3d image.
* filtering noisy sensor data
* compressing an image
* extracting raw load cell data and converting it into a resultant force and location.

### Recording

Data can also be recorded using ROS, by subscribing to different topics and logging everything as it comes in into a "bag" file.  This functionality also permits replaying the same data as it came in, for subsequent processing later

### Viewing and Interacting

ROS also has the capability to view and interact with different kinds of data

* text data can be printed to a terminal or viewed in a GUI
* image data can be subscribed to and viewed using a native viewer
* Custom nodes can be composed in Python or C++ that permit one to display and control pieces of data from one interface.

## Versions

This tutorial is set up assuming Ubuntu 18 and ROS Melodic.  Things will change, but for ROS 1 and Ubuntu, this can serve as a rough roadmap even in other versions.  Some instructions may change over time and this will be updated to reflect that as needed.

