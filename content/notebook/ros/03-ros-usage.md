---
---

## Navigating the Ros Filesystem (optional)

From [here](https://wiki.ros.org/ROS/Tutorials/NavigatingTheFilesystem)

```bash
#sudo apt-get install ros-<distro>-ros-tutorials
sudo apt-get install ros-melodic-ros-tutorials
#rospack find [package_name]
rospack find roscpp
#roscd [locationname[/subdir]]
roscd roscpp
#print the working directory using the Unix command
pwd
#To see what is in your ROS_PACKAGE_PATH, type:
echo $ROS_PACKAGE_PATH

#roscd can also move to a subdirectory of a package or stack.  Try:
roscd roscpp/cmake
pwd

#roscd log will take you to the folder where ROS stores log files. Note that if you have not run any ROS programs yet, this will yield an error saying that it does not yet exist.
#If you have run some ROS program before, try:
roscd log

#rosls is part of the rosbash suite. It allows you to ls directly in a package by name rather than by absolute path.
#rosls [locationname[/subdir]]
rosls roscpp_tutorials
```

## Create A Package

From [here](https://wiki.ros.org/ROS/Tutorials/CreatingPackage)

```bash
# You should have created this in the Creating a Workspace Tutorial
cd ~/catkin_ws/src
# catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
catkin_create_pkg beginner_tutorials std_msgs rospy roscpp

#Now you need to build the packages in the catkin workspace:
cd ~/catkin_ws
catkin_make

#To add the workspace to your ROS environment you need to source the generated setup file:
. ~/catkin_ws/devel/setup.bash

#first-order dependencies can now be reviewed with the rospack tool.
rospack depends1 beginner_tutorials 

#dependencies for a package are stored in the package.xml file:
roscd beginner_tutorials
cat package.xml

#In many cases, a dependency will also have its own dependencies. For instance, rospy has other dependencies.
rospack depends1 rospy

#rospack can recursively determine all nested dependencies.
rospack depends beginner_tutorials
```

open up package.xml and check whether there is an exec_depend tag for each of the dependencies in package.xml as in [the tutorial](https://wiki.ros.org/ROS/Tutorials/CreatingPackage#ROS.2BAC8-Tutorials.2BAC8-catkin.2BAC8-CreatingPackage.Final_package.xml)

```xml
  <buildtool_depend>catkin</buildtool_depend>

  <build_depend>roscpp</build_depend>
  <build_depend>rospy</build_depend>
  <build_depend>std_msgs</build_depend>

  <exec_depend>roscpp</exec_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>std_msgs</exec_depend>
```

## Build a ROS Package

from [here](https://wiki.ros.org/ROS/Tutorials/BuildingPackages)

```bash
#source your environment setup file if you have not already
# source /opt/ros/%YOUR_ROS_DISTRO%/setup.bash
# this has been added to bashrc so is not necessary
source /opt/ros/melodic/setup.bash
# In a catkin workspace
#catkin_make [make_targets] [-DCMAKE_VARIABLES=...]
#catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
#catkin_make
#catkin_make install #optional

#If your source code is in a different place, say my_src then you would call catkin_make like this:
# In a catkin workspace
#catkin_make --source my_src
#catkin_make install --source my_src  # (optionally)

cd ~/catkin_ws/
ls src
catkin_make
```


## Running ROS

From [here](https://wiki.ros.org/ROS/Tutorials/UnderstandingNodes)

1. In Terminal 1 (ctrl+alt+t)

    ```bash
    roscore
    ```

1. Open up a new terminal tab (ctrl+shift+t)

    ```bash
    rosnode list
    rosnode info /rosout
    ```

1. Open up a new terminal tab (ctrl+shift+t)

    ```bash
    #rosrun [package_name] [node_name]
    rosrun turtlesim turtlesim_node
    ```

1. In terminal 2(ctrl+pg_up):

    ```bash
    rosnode list
    ```

1. In terminal 3(ctrl+pg_dn):
    1. ctrl+c
    1. 
        ```rosrun turtlesim turtlesim_node __name:=my_turtle```

1. In terminal 2(ctrl+pg_up):

    ```bash
    rosnode list
    ```

## Understanding Topics

See the [tutorial](https://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)

```bash
#run ros
roscore
```
in a new terminal
```bash
rosrun turtlesim turtlesim_node
```
in a new terminal:
```bash
rosrun turtlesim turtle_teleop_key
```
in a new terminal:
```bash
rosrun rqt_graph rqt_graph
```
in a new terminal:
```bash
# list all commands within rostopic
rostopic -h

#how to subscribe to and print a topic
#rostopic echo [topic]
#rostopic echo [topic]
rostopic echo /turtle1/cmd_vel
```
in a new terminal:
```bash
# list full details
rostopic list -v

# list publishers of
#rostopic list -p [topic]
rostopic list -p /turtle1/cmd_vel

#list subscribers to
#rostopic list -s [topic]
rostopic list -s /turtle1/cmd_vel

# list message type
#rostopic type [topic]
rostopic type /turtle1/cmd_vel
# returns geometry_msgs/Twist

#message type details
#rosmsg show [msg]
rosmsg show geometry_msgs/Twist
```

More details [here](https://wiki.ros.org/ROS/Tutorials/UnderstandingTopics#rostopic_continued)

## Understanding Services and Parameters

See the [tutorial](https://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams)

## RQTConsole and ROSLaunch

From this [tutorial](https://wiki.ros.org/ROS/Tutorials/UsingRqtconsoleRoslaunch)

```bash
#roslaunch starts nodes as defined in a launch file.
#roslaunch [package] [filename.launch]

#you will need to source the environment setup file like you did at the end of the create_a_workspace tutorial:
cd ~/catkin_ws
source devel/setup.bash
roscd beginner_tutorials

#Then let's make a launch directory:
mkdir launch
cd launch

echo "<launch>

  <group ns=\"turtlesim1\">
    <node pkg=\"turtlesim\" name=\"sim\" type=\"turtlesim_node\"/>
  </group>

  <group ns=\"turtlesim2\">
    <node pkg=\"turtlesim\" name=\"sim\" type=\"turtlesim_node\"/>
  </group>

  <node pkg=\"turtlesim\" name=\"mimic\" type=\"mimic\">
    <remap from=\"input\" to=\"turtlesim1/turtle1\"/>
    <remap from=\"output\" to=\"turtlesim2/turtle1\"/>
  </node>

</launch>" >> turtlemimic.launch

roslaunch beginner_tutorials turtlemimic.launch
```
in a new terminal
```bash
rostopic pub /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]'
```
in a new terminal
```bash
#rqt
rqt_graph
```

## Creating a Message and Service

From this [tutorial](https://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)


```bash
cd ~/catkin_ws
source devel/setup.bash
roscd beginner_tutorials

mkdir msg
echo "int64 num
string first_name
string last_name
uint8 age
uint32 score" > msg/Num.msg

nano package.xml
```

add these lines:
```
  <build_depend>message_generation</build_depend>
  <exec_depend>message_runtime</exec_depend>
```

save and exit
```
nano CMakeLists.txt 
```

Add the message_generation dependency to the find_package call which already exists in your CMakeLists.txt so that you can generate messages. You can do this by simply adding message_generation to the list of COMPONENTS such that it looks like this:

```
# Do not just add this to your CMakeLists.txt, modify the existing text to add message_generation before the closing parenthesis
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
```

Also make sure you export the message runtime dependency.

```
catkin_package(
  ...
  CATKIN_DEPENDS message_runtime ...
  ...)
```
Find the following block of code:
```
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )
```
Uncomment it by removing the # symbols and then replace the stand in Message*.msg files with your .msg file, such that it looks like this:
```
add_message_files(
  FILES
  Num.msg
)
```
By adding the .msg files manually, we make sure that CMake knows when it has to reconfigure the project after you add other .msg files.

Now we must ensure the generate_messages() function is called.

For ROS Hydro and later, you need to uncomment these lines:

```
# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )
```
so it looks like:
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

```bash
#rosmsg show [message type]
rosmsg show beginner_tutorials/Num

#Now that we have made some new messages we need to make our package again:

# In your catkin workspace
roscd beginner_tutorials
cd ../..
catkin_make install
cd -
```

## Simple Publisher and Subscriber (Python)

From [here](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)

```bash
cd ~/catkin_ws
source devel/setup.bash
roscd beginner_tutorials
mkdir scripts
cd scripts
wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
chmod +x talker.py
roscd beginner_tutorials/scripts/
wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
chmod +x listener.py
cd ~/catkin_ws
catkin_make
```

## Examining Publisher and Subscriber
From  [here](https://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber)

Make sure that a roscore is up and running:

```bash
roscore
```

```bash
# In your catkin workspace
cd ~/catkin_ws
source ./devel/setup.bash

#In the last tutorial we made a publisher called "talker". Let's run it:
#rosrun beginner_tutorials talker      (C++)
rosrun beginner_tutorials talker.py  # (Python) 
```
In another terminal:
```bash
#rosrun beginner_tutorials listener     (C++)
rosrun beginner_tutorials listener.py  #(Python) 
```


## Recording data (creating a bag file)

1. In Terminal 1:

    ```
    roscore
    ```                                                                                                 
1. In Terminal 2:

    ```
    rosrun turtlesim turtlesim_node
    ```

1. In Terminal 3:

    ```
    rosrun turtlesim turtle_teleop_key
    ```

1. Start Recording.  In Terminal 4:

    ```
    rostopic list -v
    mkdir ~/bagfiles
    cd ~/bagfiles
    rosbag record -a -O test.bag --duration=10s
    #Wait ten seconds

    #Examine your bagfile
    rosbag info test.bag

    #Play back at twice the rate
    #rosbag play -r 2 <your bagfile>
    rosbag play -r 2 test.bag

    rosbag record -O subset.bag --duration /turtle1/cmd_vel /turtle1/pose
    rosbag info subset.bag
    ```

<!--
1. with the ip address:

    ```
    export ROS_IP=192.168.0.17
    ```
-->