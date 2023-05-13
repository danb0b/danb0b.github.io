---
title: Arduino IDE setup
---

```bash
sudo apt install fuse3 libfuse2 libfuse3-3
```

## board libraries

- <https://dl.espressif.com/dl/package_esp32_index.json>
- <https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCM9.04/master/arduino/opencm_release/package_opencm9.04_index.json>


library manager
dynamixel2arduino

## Board manager

ESP32
OpenCM9.04

## Solving the Compiler error in linux

After installing I get the error:

> ...arm-none-eabi-g++: No such file or directory

Thanks to [this post](https://forum.arduino.cc/t/arduino-1-5-6-r2-for-64-bit-linux-includes-32-bit-gcc/216075) I was able to solve the problem.


```bash
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install libc6:i386
```