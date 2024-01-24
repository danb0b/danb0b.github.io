---
title: Installing ROS2 on a Raspberry Pi Zero 2W
tags:
- ros2
- ubuntu
- linux
---

## Flashing

Make sure you 

* add your ssh key during flashing 
* setup wifi
* define a hostname

## Installing

It's important to disable automatic updates as you should initiate it according to your own availability.  Otherwise, it will start updating the first time you get an internet connection.  To prevent that, uninstall the "unattended-upgrades" package.

```bash
sudo apt remove unattended-upgrades
```

if you get a message like:

```bash
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2131 (uWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2131 (unattended-upgr)   
```

```bash
sudo killall unattended-upgr
```

It's always a good idea to perform headless updates in a way that won't break if you lose your wireless connction.  for this I use tmux

```bash
sudo apt update
sudo apt install tmux
tmux
```

inside the tmux window:

update and upgrade

```bash
sudo apt update && sudo apt upgrade -y
exit
```

```bash
sudo reboot now
```

Install packages

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Install ros2.  this follows the humble instructions

```bash
locale
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade
```

now for installing ros, we want the minimum required set.  therefore we are going to install the base package and a couple packages on top as needed, rather than the full desktop

```bash
sudo apt install ros-humble-ros-base
# not sure which one of these I actually did, but pretty sure I did the cpp version.
#sudo apt install ros-humble-examples-rclpy-minimal-subscriber ros-humble-examples-rclpy-minimal-publisher 
sudo apt install ros-humble-examples-rclcpp-minimal-subscriber ros-humble-examples-rclcpp-minimal-publisher 
source /opt/ros/humble/setup.bash
sudo apt-get install python3-rosdep
sudo rosdep init
rosdep update
sudo apt install ros-humble-rmw-cyclonedds-cpp
```

```bash
ros2 run demo_nodes_cpp talker
sudo apt install ros-humble-demo-nodes-cpp
ros2 run demo_nodes_cpp talker
```

install ifconfig to find your ip address

```bash
sudo apt install net-tools
ifconfig
```

create a cyclonedds config file for your local network

```bash
cat <<EOT >> ~/cyclonedds_local.xml
<CycloneDDS>
    <Domain>
        <General>
            <DontRoute>true</DontRoute>        
            <AllowMulticast>false</AllowMulticast>
            <EnableMulticastLoopback>true</EnableMulticastLoopback>
        </General>
        <Discovery>
          <ParticipantIndex>auto</ParticipantIndex>
          <Peers>
            <Peer Address="<the local ip address of the rpi2w>"/>
            <Peer Address="<the local ip address of other machine>"/>
            <Peer Address="<...>"/>
          </Peers>
    </Discovery>
    </Domain>
</CycloneDDS>
EOT
sudo mv ~/cyclonedds_local.xml /etc/
sudo cp /etc/cyclonedds_local.xml /etc/cyclonedds.xml
```

create a cyclonedds config file for your tailscale network network:

```bash
tailscale status
```

this will tell you about your tailscale ip addresses.

```bash
cat <<EOT >> ~/cyclonedds_ts.xml
<CycloneDDS>
    <Domain>
        <General>
            <DontRoute>true</DontRoute>        
            <AllowMulticast>false</AllowMulticast>
            <EnableMulticastLoopback>true</EnableMulticastLoopback>
        </General>
        <Discovery>
          <ParticipantIndex>auto</ParticipantIndex>
          <Peers>
            <Peer Address="<the tailscale ip address of the rpi2w>"/>
            <Peer Address="<the tailscale ip address of other machine>"/>
            <Peer Address="<...>"/>
          </Peers>
    </Discovery>
    </Domain>
</CycloneDDS>
EOT
sudo mv ~/cyclonedds_ts.xml /etc/
```

setup .bashrc

```bash
echo "export CYCLONEDDS_URI=/etc/cyclonedds.xml" >> ~/.bashrc
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
echo "export ROS_DOMAIN_ID=0" >> ~/.bashrc
echo "export ROS_LOCALHOST_ONLY=0" >> ~/.bashrc
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc 
source ~/.bashrc
sudo reboot now
```

```bash
ros2 run demo_nodes_cpp listener
ros2 run demo_nodes_cpp talker
```

now try replacing the local ip addresses with tailscale ip addresses

```bash
sudo cp /etc/cyclonedds_ts.xml /etc/cyclonedds.xml
sudo reboot now
ros2 run demo_nodes_cpp listener
ros2 run demo_nodes_cpp listener
```

<!-- 
sudo apt install ros-humble-desktop
sudo apt install ros-humble-desktop
sudo apt search ros-humble*demo*
sudo apt search ros-humble*
sudo apt search ros-humble-de*
sudo apt search ros-humble-de
sudo apt search ros-humble-demo
sudo apt search ros-humble-exampl
sudo apt install ros-humble-desktop -->
