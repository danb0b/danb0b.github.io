---
title: Demonstrating Unicast in ROS2 on virtual machines over a local network using CycloneDDS
weight: 20
tags:
- virtualbox
- linux
- ubuntu
- ros2
- cyclonedds
- unicast
summary: " "
---

Switching from ROS2's multicast default to unicast can be a bit tricky, especially if you're testing.  I came up with a way to get it working between to virtualbox virtual machine clones and wanted to share my strategy.

> This tutorial assumes you have set up two clones of the same virtual machine according to [this tutorial](/notebook/ros2/installing-ros2-on-a-vm/).  If you would like to follow along, please complete that tutorial first.

## Instructions

> Follow these instructions for both virtual machine clones.

Start both the original and clone vms and obtain the ip addresses:

vm 1:

```bash
ip a
```

vm2:

```bash
ip a
```

Then install cyclone dds, which is not the default DDS middlewaer for humble.

```bash
sudo apt install -y ros-humble-rmw-cyclonedds-cpp
```

Then create a cyclonedds configuration file.  Replace ```192.168.xxx.yyy``` and ```192.168.xxx.zzz``` with the two ip addresses for each of your vm clones.

```bash
cat <<EOT | sudo tee /etc/cyclonedds_pc.xml
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
            <Peer Address="192.168.xxx.yyy"/>
            <Peer Address="192.168.xxx.zzz"/>
          </Peers>
    </Discovery>
    </Domain>
</CycloneDDS>
EOT
```

Then modify .bashrc and source it.

```bash
echo "export CYCLONEDDS_URI=/etc/cyclonedds_pc.xml" >> ~/.bashrc
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
source ~/.bashrc
```

Close the terminal windows in each vm and opened new ones in each vm and ran:

vm1:

```bash
ros2 run demo_nodes_cpp talker
```

vm2:

```bash
ros2 run demo_nodes_cpp listener
```

## Behavior

It seems that if you change the cyclone config xml file, those changes will not be seen until terminal windows on both machines are re-opened, or better yet, all machines are rebooted.  it seems once the computers are linked, ros retains a memory of what it has connected to in the past.

It also seems that it is sufficient for either one or the other xml file to reflect the other machine's ip address, regardless of which one is publishing and which one is subscribing.  

>I'm not sure if what I described is _intended_ behavior
