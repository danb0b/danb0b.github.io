---
title: Clone and Setup Custom Workspace
weight: 60
tags:
- ros
- ubuntu
- linux
---

## Steps

1. Install prerequisites

```bash
sudo apt install -y ros-melodic-joy
sudo apt install -y python3-numpy
```

1. Install libnifalcon (instructions in Falcon tutorial)

1. Clone the idealab repository

    ```bash
    mkdir ~/code
    cd ~/code
    git clone https://github.com/idealabasu/code_idealab_ros.git
    ```

1. Compile

    ```bash
    cd ~/code/code_idealab_ros/
    catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
    ```

1. Source your workspace (whenever you clone a new repository/workspace)

    ```bash
    # one time:
    #source devel/setup.bash
    # or permanent:
    echo "source ~/code/code_idealab_ros/devel/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    ```
