---
title: identify packages added using apt's log
tags:
- logging
- ubuntu
- apt
summary: " "
---

first step is to  find the first line number where a particular date occurs

```bash
cat /var/log/apt/term.log | grep -n 08-15
```

do that again to find the beginning of the second date range if necessary

```bash
cat /var/log/apt/term.log | grep -n 08-16
```

Then use this technique to select only part of the log and then identify newly added packages

```bash
sed '915,10000000!d' /var/log/apt/term.log | grep -i "selecting previously unselected"
```

this returns something like

```
Selecting previously unselected package libglfw3:amd64.
Selecting previously unselected package libgl1-mesa-glx:amd64.
Selecting previously unselected package libosmesa6:amd64.
Selecting previously unselected package xorg-sgml-doctools.
Selecting previously unselected package x11proto-dev.
Selecting previously unselected package libxau-dev:amd64.
Selecting previously unselected package libxdmcp-dev:amd64.
Selecting previously unselected package xtrans-dev.
Selecting previously unselected package libpthread-stubs0-dev:amd64.
Selecting previously unselected package libxcb1-dev:amd64.
Selecting previously unselected package libx11-dev:amd64.
Selecting previously unselected package libglx-dev:amd64.
Selecting previously unselected package libgl-dev:amd64.
Selecting previously unselected package libegl-dev:amd64.
Selecting previously unselected package libegl1-mesa:amd64.
Selecting previously unselected package libglvnd-core-dev:amd64.
Selecting previously unselected package libgles1:amd64.
Selecting previously unselected package libgles-dev:amd64.
Selecting previously unselected package libopengl-dev:amd64.
Selecting previously unselected package libglvnd-dev:amd64.
Selecting previously unselected package libegl1-mesa-dev:amd64.
Selecting previously unselected package libosmesa6-dev:amd64.
Selecting previously unselected package libglu1-mesa-dev:amd64.
Selecting previously unselected package libglew-dev:amd64
```

by doing a quick find/replace you can then clean up the list and do a ```sudo apt remove```

```bash
sudo apt remove libglfw3:amd64 libgl1-mesa-glx:amd64 libosmesa6:amd64 xorg-sgml-doctools x11proto-dev libxau-dev:amd64 libxdmcp-dev:amd64 xtrans-dev libpthread-stubs0-dev:amd64 libxcb1-dev:amd64 libx11-dev:amd64 libglx-dev:amd64 libgl-dev:amd64 libegl-dev:amd64 libegl1-mesa:amd64 libglvnd-core-dev:amd64 libgles1:amd64 libgles-dev:amd64 libopengl-dev:amd64 libglvnd-dev:amd64 libegl1-mesa-dev:amd64 libosmesa6-dev:amd64 libglu1-mesa-dev:amd64 libglew-dev:amd64
```