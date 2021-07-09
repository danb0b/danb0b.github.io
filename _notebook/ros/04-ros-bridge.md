---
---

## Introduction

This section describes installing RosBridge, which is useful for communicating to devices which do not have ROS installed (like windows machines with custom drivers)

## Installing, Running, and Using RosBridge

from [here](https://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge) and [here](https://roslibpy.readthedocs.io/en/latest/examples.html)

<!--
```bash
#sudo apt install ros-melodic-rosbridge-library ros-melodic-rosbridge-msgs ros-melodic-rosbridge-server ros-melodic-rosbridge-suite
```
-->
1. Install necessary prerequisites on the ROS machine
    ```bash
    #Install rosbridge on guest machine
    sudo apt install ros-melodic-rosbridge-suite

    #Install roslibpy client for rosbridge on guest machine
    pip3 install service_identity roslibpy

    #launch rosbridge server
    roslaunch rosbridge_server rosbridge_websocket.launch

    #open up your favorite python editor
    spyder3
    ```

1. start roscore on the guest:

    ```bash
    roscore
    ```

1. Run an existing talker in ROS.  in a new terminal window:
    ```bash
    cd ~/catkin_ws
    source ./devel/setup.bash

    #In the last tutorial we made a publisher called "talker". Let's run it:
    #rosrun beginner_tutorials talker      (C++)
    rosrun beginner_tutorials talker.py  # (Python) 
    ```

## Non-ROS machine setup


1. install roslibpy (required if you did not do this in the prior step)

    ```
    pip install service_identity roslibpy
    ```
    
1. create a file called listener.py, substituting the ip address of the ROS Master for <IPADDRESS>.  Paste in the following:

    ```python
    # -*- coding: utf-8 -*-
    """
    Created on Fri Mar 27 08:33:41 2020

    @author: danaukes
    """

    from __future__ import print_function
    import roslibpy

    client = roslibpy.Ros(host='<IPADDRESS>', port=9090)
    client.run()

    listener = roslibpy.Topic(client, '/chatter', 'std_msgs/String')
    listener.subscribe(lambda message: print('Heard talking: ' + message['data']))

    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.terminate()
    except Exception as e:
        print(e)
        client.terminate()
    ```

1. Run from the editor(f5) or, in a new terminal window, navigate to the location of 'listener.py' and type:

    ```
    python3 listener.py
    ```

1. Now, create a file called talker.py, substituting the ip address of the machine for <IPADDRESS> if on the host machine, or 'localhost' if in the guest machine.  Paste in the following:

    ```python
    # -*- coding: utf-8 -*-
    """
    Created on Fri Mar 27 08:36:13 2020

    @author: danaukes
    """

    import time

    import roslibpy

    client = roslibpy.Ros(host='<IPADDRESS>', port=9090)
    client.run()

    talker = roslibpy.Topic(client, '/dancustom', 'std_msgs/String')

    while client.is_connected:
        talker.publish(roslibpy.Message({'data': 'Hello World!'}))
        print('Sending message...')
        time.sleep(1)

    talker.unadvertise()

    client.terminate()
    ```

1. on the guest machine, start a new terminal window, and type

    ```bash
    rostopic echo /dancustom
    ```

