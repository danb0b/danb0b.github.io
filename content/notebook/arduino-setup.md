---
title: Arduino IDE setup for Dynamixel, ESP32, and other IDEAlab devices
tags:
- arduino
- dynamixel
- opencm
- ESP32
- idealab
summary: " "
---

```bash
sudo apt install -y fuse3 libfuse2 libfuse3-3
```

## board libraries

- <https://dl.espressif.com/dl/package_esp32_index.json>
- <https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCM9.04/master/arduino/opencm_release/package_opencm9.04_index.json>

library manager
dynamixel2arduino
simplefoc

## Board manager

ESP32
OpenCM9.04

## Solving the Compiler error in linux

After installing I get the error:

```bash
fork/exec /home/danaukes/.arduino15/packages/OpenCM904/tools/opencm_gcc/5.4.0-2016q2/bin/arm-none-eabi-g++: no such file or directory

Compilation error: fork/exec /home/danaukes/.arduino15/packages/OpenCM904/tools/opencm_gcc/5.4.0-2016q2/bin/arm-none-eabi-g++: no such file or directory
```

This was present in both arduino 1.8 and 2.X ide's.

Thanks to [this post](https://forum.arduino.cc/t/arduino-1-5-6-r2-for-64-bit-linux-includes-32-bit-gcc/216075) I was able to solve the problem.

```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libc6:i386
```

### other refs related to this

- <https://forum.arduino.cc/t/solved-compilation-error-arduino-avrdude-6-3-0-arduino17-is-not-installed/701550>
- <https://support.arduino.cc/hc/en-us/articles/360018444739-Error-file-does-not-exist-no-such-file-or-directory-system-cannot-find-the-file-specified>

## External References

- <https://www.pololu.com/product/2566>
- <https://www.robotis.us/opencm9-04-c-with-onboard-xl-type-connectors/>
- <https://emanual.robotis.com/docs/en/parts/controller/opencm904/>
- <https://emanual.robotis.com/docs/en/dxl/x/xl320/>
- <https://github.com/ROBOTIS-GIT/OpenCM9.04>
