---
title: Setting up OptiTrack
tags:
  - ROS
  - ubuntu
  - linux
  - optitrack
---

## Links

* <http://wiki.ros.org/mocap_optitrack>

## Install

```
sudo apt install ros-melodic-mocap-optitrack
```

## Create a rigid body and ensure it is being transmitted from Motiv

![](image1.jpg)

![](image2.jpg)

## Edit mocap.yaml                                           

```
roscd mocap_optitrack/config
nano mocap.yaml
```

```
#
# Definition of all trackable objects
# Identifier corresponds to Trackable ID set in Tracking Tools
#
rigid_bodies:
    '1':
        pose: Robot_1/pose
        pose2d: Robot_1/ground_pose
        odom: Robot_1/Odom
        tf: tf
        child_frame_id: Robot_1/base_link
        parent_frame_id: world
#    '2':
#        pose: Robot_2/pose
#        pose2d: Robot_2/ground_pose
#        odom: Robot_2/Odom
#        tf: tf
#        child_frame_id: Robot_2/base_link
#        parent_frame_id: world
optitrack_config:
        multicast_address: 224.0.0.1
        command_port: 1510
        data_port: 1511
        enable_optitrack: true
```

## Launch mocap

```
roslaunch mocap.launch
```

## Subscribe to the pose topic

```
rostopic echo /mocap_node/Robot_1/pose 
```
