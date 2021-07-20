---
---
1. install uvc stuff.

    ```bash
    sudo apt update
    sudo apt install -y libuvc-dev guvcview cheese v4l-utils
    # sudo apt install uvccapture uvcdynctrl 
    ```

1. try guvcview or cheese to see if you can see video output(may need to install):

    ```bash
    # cheese # only need to try one command
    guvcview
    ```

1. (optional, seems already done, perhaps by previous step) add yourself to video group
      
      ```bash
      sudo usermod -a -G video $(whoami)
      ```

      1. Logout & login again , check if your vboxusers displays in this command

      ```
      groups
      ```

      
1. (optional, seems already done, perhaps by previous step)  copy rules from idealab_ros_tools to rules folder (according to this [ref](http://wiki.ros.org/libuvc_camera))

```bash
cd ~/code_idealab_ros/src
sudo cp 99-uvc-c930.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && udevadm trigger
sudo reboot
```

1. get workspace prepared with dependencies:

    ```
    cd ~

    git clone https://github.com/ros-drivers/libuvc_ros
    cd libuvc_ros
    cp -r libuvc_camera ~/code_idealab_ros/src
    cp -r libuvc_ros ~/code_idealab_ros/src

    cd ~

    git clone https://github.com/ros/nodelet_core
    cd nodelet_core
    cp -r nodelet ~/code_idealab_ros/src
    cp -r nodelet_core ~/code_idealab_ros/src

    git clone https://github.com/ros/bond_core
    cd bond_core
    cp -r * ~/code_idealab_ros/src

    cd ~

    cd code_idealab_ros/
    catkin_make
    ```

1. identify desired video device:

```
v4l2-ctl --list-devices
```

1. start roscore on master uri

1. run node

```
rosrun libuvc_camera camera_node
```