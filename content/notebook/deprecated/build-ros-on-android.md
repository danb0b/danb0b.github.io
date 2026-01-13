---
title: Building ROS2 on Android
tags:
- ROS2
- android
- termux
---

<https://github.com/termux/proot-distro>

```bash
termux-setup-storage
pkg install proot-distro
proot-distro login ubuntu --termux-home
```

Install ROS

<https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html>

```bash
apt install -y software-properties-common
add-apt-repository universe
apt update && apt install -y curl
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt install -y \
  python3-flake8-docstrings \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools
sudo apt install -y \
   python3-flake8-blind-except \
   python3-flake8-builtins \
   python3-flake8-class-newline \
   python3-flake8-comprehensions \
   python3-flake8-deprecated \
   python3-flake8-import-order \
   python3-flake8-quotes \
   python3-pytest-repeat \
   python3-pytest-rerunfailures  
mkdir -p ~/ros2_humble/src
cd ~/ros2_humble
vcs import --input https://raw.githubusercontent.com/ros2/ros2/humble/ros2.repos src   
sudo apt upgrade
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -y --skip-keys "fastcdr rti-connext-dds-6.0.1 urdfdom_headers"
cd ~/ros2_humble/
colcon build --symlink-install
```

But that may not work.  The following links gave me some hints (most helpful to least)

* <https://answers.ros.org/question/304300/compilling-ros2-on-rasperry-pi/>
* <https://answers.ros.org/question/379624/building-ros2-dashing-base-from-source/>
* <https://robotics.stackexchange.com/questions/101962/ros2-colcon-build>
* <https://robotics.stackexchange.com/questions/88848/can-not-compile-ros-2-cmake-error-installexport-given-unknown-export-has-li>

I was not able to compile without not building ros-visualization.  Not needed anyways.

```bash
cd ros-visualization
touch COLCON_IGNORE
cd ../
```

Then it would crash termux without warning.  I reduced the number of processors and told colcon to build sequentially

```bash
export MAKEFLAGS="-j1"
colcon build --symlink-install --parallel-workers 1 --executor sequential
```

And then wait two weeks.  Not kidding.

The following  might be needed to be compatible with other ROS2 implementations.

```bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

## Storage

This installation takes about 14 Gb, including proot, ubuntu, ROS dependencies, etc.

## Where I'm stuck

after  doing:

```bash
. ~/ros2_humble/install/local_setup.bash
ros2 run demo_nodes_cpp talker
```

I get

```bash
getifaddrs: Permission denied
```

<https://www.reddit.com/r/termux/comments/143y69f/patching_getifaddrs_permission_denied/>


This seems like a ROS2 problem to patch, rather than a termux or proot issue.  proot/termux just doesn't support this functionality...

## Future Work


How can I route android sensor data to this?  I will need to check out this website...

<https://wiki.termux.com/wiki/Termux-sensor>

## External Resources

* <https://answers.ros.org/question/304300/compilling-ros2-on-rasperry-pi/>
* <https://answers.ros.org/question/379624/building-ros2-dashing-base-from-source/>
* <https://robotics.stackexchange.com/questions/88848/can-not-compile-ros-2-cmake-error-installexport-given-unknown-export-has-li>
* <https://docs.ros.org/en/humble/Installation/DDS-Implementations/Working-with-Eclipse-CycloneDDS.html>
* <https://robotics.stackexchange.com/questions/101962/ros2-colcon-build>
* <https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html>
* <https://github.com/termux/proot-distro>
