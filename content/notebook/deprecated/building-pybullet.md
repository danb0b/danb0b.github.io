---
title: Building PyBullet
tags: 
  - cmake
  - cplusplus
  - ubuntu
  - pybullet
summary: ""
---


```bash
sudo apt  install cmake-curses-gui 
cd ~/Downloads
git clone https://github.com/bulletphysics/bullet3.git
cd bullet3
ccmake .
```

then configure, generate

```bash
make
```

then wait for it to build and then

```bash
sudo make install
```

-------------

## Old

Things I tried that didn't work at fixing my Mesa errors (it was anaconda the whole time!)

```
sudo apt install -y mesa-utils
sudo apt install --reinstall libgl1-mesa-dri

sudo apt install -y libopengl-dev libglx-dev libglfw3-dev
sudo apt install -y freeglut3-dev libglw1-mesa-dev
sudo apt install -y libglm-dev

sudo apt install --reinstall libglw1-mesa libglw1-mesa-dev 
```
