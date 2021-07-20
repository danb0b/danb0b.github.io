---
---

## Introduction

This tutorial describes how to install and run a Novint falcon in an Ubuntu virtual machine.  This tutorial goes through how to do it from scratch.  

Note: the libnifalcon repository is now forked [here](https://github.com/idealabasu/libnifalcon).  Furthermore, the [idealab_ros_tools](https://github.com/idealabasu/code_idealab_ros) repository now has the current working copy of the ros_falcon package in it.  the original ros_falcon package has been forked and is now [here ](https://github.com/idealabasu/ros_falcon)


## Instructions

1. Go to the usb settings and add the falcon filter to virtualbox ('Future Technology Devices International, Ltd FALCON HAPTIC [0400]')

1. open up virtualbox and check to see if it is found 

		```bash
		dmesg | grep FALCON
		```	

1. install libusb

		```bash
		sudo apt install libusb
		```

1. clone repository

		```bash
		cd ~/
		git clone https://github.com/idealabasu/libnifalcon
		cd ~/libnifalcon
		```

1. follow instructions

		```bash
		cd ~/libnifalcon
		mkdir build
		cd build
		cmake -G "Unix Makefiles" ..
		make
		sudo make install
		```


1. add device udev file from within the idealab_ros_tools repository

		```
		#the default one doesn't seem to work
		#sudo cp ~/libnifalcon/linux/40-novint-falcon-udev.rules /etc/udef/rules.d/
		sudo cp ~/code_idealab_ros/src/ros_falcon/udev/99-udev-novint.rules /etc/udef/rules.d/
		sudo chmod 644 99-udev-novint.rules
		sudo udevadm control --reload-rules && udevadm trigger
		```

1. run ```findfalcons``` several times until you see it

1. add joy package

		```bash
		sudo apt install ros-melodic-joy
		```

1. clone the ros falcon repository (optional, it is now located in the code_idealab_ros repository now)

		```bash
		cd ~/
		git clone https://github.com/idealabasu/ros_falcon.git
		```

1. copy the folder into the src folder in your workspace (also unnecessary now, it is already there)

1. Run node and view results

	1. in a new terminal:

			```
			roscore
			```

	1. run falcon node
	
			```bash
			roscd ros_falcon
			# cd nodes
			#chmod +x joy2cmd_vel.py
			rosrun ros_falcon driver
			```

	1. in a second terminal:

			```
			rostopic echo /falconPos
			```