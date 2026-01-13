---
title: Working with topics
tags:
- ROS2
- ubuntu
- bash
- topics
---


```bash
rostopic list
ros2 topic info /myrobot/sensor1
ros2 topic info -v /myrobot/sensor1
ros2 topic echo /myrobot/sensor1
ros2 interface show std_msgs/msg/Int32
ros2 topic pub /myrobot/blink_led std_msgs/msg/Int32 "{data: 1}"
```