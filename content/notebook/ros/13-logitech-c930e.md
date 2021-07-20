---
---

# Using a USB webcam (with virtualbox)

## Introduction

Making a usb webcam work in Linux AND virtualbox is not as easy as it sounds.  These instructions were validated for the C930 Webcam by Logitech.  Some steps need to change to make other cameras work.  For this tutorial to work, the camera should be "UVC compliant"

You need to follow slightly different steps if you want to provide access to a built-in camera on your computer.  This is possible but some of the USB-specific instructions will not work, as it won't be necessarily recognized as a usb device using libusb

## Instructions

1. Make sure you have installed the virtualbox extension pack: <https://www.virtualbox.org/wiki/Downloads>
1. check virtualbox usb settings to ensure usb is set at 3.0 to get high speed working.
1. make sure usb filter is set for usb webcam.
1. make sure your user is part of vboxusers group, per this suggestion (you may have already done this in a previous tutorial): [reference](https://askubuntu.com/questions/4875/how-can-i-use-my-webcam-with-ubuntu-running-in-virtualbox)

    1. check if your vboxusers displays in this command :

        ```
        groups
        ```
    
    1. add yourself
    
        ```bash
        sudo usermod -a -G vboxusers $(whoami)
        ```

    1. Logout & login again , check if your vboxusers displays in this command :

        ```
        groups
        ```

1. install uvc stuff.

    ```bash
    sudo apt update
    sudo apt install -y guvcview cheese v4l-utils
    # sudo apt install uvccapture uvcdynctrl 
    ```

1. try guvcview or cheese to see if you can see video output(may need to install):

    ```bash
    # cheese # only need to try one command
    guvcview
    ```

1. install ros package:

    ```bash
    sudo apt update
    sudo apt install ros-melodic-libuvc-camera
    #ros-melodic-uvc-camera #deprecated
    ```

1. add yourself to video group
      
      ```bash
      sudo usermod -a -G video $(whoami)
      ```

1. Logout & login again , check if your vboxusers displays in this command

    ```
    groups
    ```
      
1. copy rules from idealab_ros_tools to rules folder (according to this [ref](http://wiki.ros.org/libuvc_camera))

    ```bash
    cd ~/code_idealab_ros/src
    sudo cp 99-uvc-c930.rules /etc/udev/rules.d/
    sudo cp 99-uvc-vboxcam.rules /etc/udev/rules.d/
    sudo udevadm control --reload-rules && udevadm trigger
    ```

1. if that doesn't work just 

    ```bash
    sudo chmod 777 /dev/bus/usb/001/001  
    ```

    where 001 and 002 is the bus and id of the desired usb camera, respectively, which was acquired from the lsusb command.

1. optional step: you can view/edit parameters directly from bash according to [this](https://www.kurokesu.com/main/2016/01/16/manual-usb-camera-settings-in-linux/)

    ```bash
    v4l2-ctl --list-devices
    v4l2-ctl -d /dev/video0 --list-ctrls
    ```

    this results...
    
    ```
                         brightness 0x00980900 (int)    : min=0 max=255 step=1 default=128 value=128
                           contrast 0x00980901 (int)    : min=0 max=255 step=1 default=128 value=128
                         saturation 0x00980902 (int)    : min=0 max=255 step=1 default=128 value=128
     white_balance_temperature_auto 0x0098090c (bool)   : default=1 value=1
                               gain 0x00980913 (int)    : min=0 max=255 step=1 default=0 value=0
               power_line_frequency 0x00980918 (menu)   : min=0 max=2 default=2 value=2
          white_balance_temperature 0x0098091a (int)    : min=2000 max=7500 step=1 default=4000 value=4000 flags=inactive
                          sharpness 0x0098091b (int)    : min=0 max=255 step=1 default=128 value=128
             backlight_compensation 0x0098091c (int)    : min=0 max=1 step=1 default=0 value=0
                      exposure_auto 0x009a0901 (menu)   : min=0 max=3 default=3 value=3
                  exposure_absolute 0x009a0902 (int)    : min=3 max=2047 step=1 default=250 value=250 flags=inactive
             exposure_auto_priority 0x009a0903 (bool)   : default=0 value=1
                       pan_absolute 0x009a0908 (int)    : min=-36000 max=36000 step=3600 default=0 value=0
                      tilt_absolute 0x009a0909 (int)    : min=-36000 max=36000 step=3600 default=0 value=0
                     focus_absolute 0x009a090a (int)    : min=0 max=255 step=5 default=0 value=0 flags=inactive
                         focus_auto 0x009a090c (bool)   : default=1 value=1
                      zoom_absolute 0x009a090d (int)    : min=100 max=400 step=1 default=100 value=100
                          led1_mode 0x0a046d05 (menu)   : min=0 max=3 default=0 value=3
                     led1_frequency 0x0a046d06 (int)    : min=0 max=255 step=1 default=0 value=0
    ```

1. (optional) other [steps](http://wiki.ros.org/libuvc_camera#Running_the_driver) which might be required

1. Finally, get it working in ros:

    1. in the first window:

        ```bash
        roscore
        ```

    1. in window #2:

        ```bash
        rosrun libuvc_camera camera_node
        ```

    1. in another window (ctrl+shift+t)

        ```bash
        rosrun rqt_image_view rqt_image_view
        ```
        
## References

* <https://www.virtualbox.org/wiki/Downloads>
* <https://www.kurokesu.com/main/2016/01/16/manual-usb-camera-settings-in-linux/>
* <http://wiki.ros.org/libuvc_camera>
* <https://askubuntu.com/questions/4875/how-can-i-use-my-webcam-with-ubuntu-running-in-virtualbox>
* <https://msadowski.github.io/ros-web-tutorial-pt2-cameras/>

## Other helpful commands

```
# list usb devices with verbose option
lsusb -v
# list usb devices
lsusb
# list usb messages
dmesg 
```