---
---
## Webcam Tutorial

[Original Reference](https://msadowski.github.io/ros-web-tutorial-pt2-cameras/)

### Configure the camera

1. check camera availability

    ```bash
    ls /dev/video*
    ```

1. Get detailed information of the camera

    ```bash
    udevadm info --name=/dev/video1 --attribute-walk
    ```

1. looking at parent device ‘/devices/pci0000:00/0000:00:14.0/usb1/1-1’: as those are our camera parameters. 

    ```bash
    ATTRS{idProduct}=="9320"
    ATTRS{idVendor}=="05a3"
    ```

1. Creating a file /etc/udev/rules.d/99-uvc.rules with lines below: (change numbers based on the camera informations)

    ```bash
    SUBSYSTEMS=="usb", ENV{DEVTYPE}=="usb_device", ATTRS{idVendor}=="05a3", ATTRS{idProduct}=="9320", MODE="0666"
    ```

1. reload the Udev rules:

    ```bash
    sudo udevadm control --reload-rules
    ```

### Set up ROS nodelets

1. Install library

    ```bash
    sudo apt-get install ros-melodic-libuvc-camera
    ```
1. Set up the ROS package (firstly make sure catkin is installed)

    ```bash
    cd ~/catkin_ws/src
    catkin_create_pkg my_camera -s libuvc_camera
    mkdir ~/catkin_ws/src/my_camera/launch
    ```

1.  Create a file named elp.launch with contents below:  
(modify the ‘vendor’ value and ‘product’ value based on the configuration shown before,as well as the image size information, usually the default setting below will work)

    ```xml
    <launch>

      <node pkg="nodelet" type="nodelet" name="nodelet_manager" args="manager" output="screen"/>

      <node pkg="nodelet" type="nodelet" name="libuvc_camera" args="load libuvc_camera/driver /nodelet_manager" output="screen">
        <param name="frame_id" value="elp_camera" />
        <!-- Parameters used to find the camera -->
        <param name="vendor" value="0x5986"/>
        <param name="product" value="0x2115"/>

        <!-- Image size and type -->
        <param name="width" value="1280"/>
        <param name="height" value="720"/>
        <param name="video_mode" value="mjpeg"/>
        <param name="frame_rate" value="30"/>

        <!-- <param name="camera_info_url" value="file://$(find my_camera)/config/elp.yaml"/> -->
      </node>
    </launch>
    ```

### Testing

1. Open a new terminal, run lines below:

    ```bash
    sudo -s
    source /home/yuhao/catkin_ws/devel/setup.bash
    roslaunch my_camera elp.launch
    ```

1. Open a new terminal, launch rqt_image_view to check the received image feed

    ```bash
    rosrun rqt_image_view rqt_image_view
    ```
