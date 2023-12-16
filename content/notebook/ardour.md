---
title: Compiling Ardour
tags:
- ubuntu
- audio
- ardour
---

## Intro

The steps for building ardour are not complete [on their website](https://ardour.org/building_linux.html).  Here are a couple helpful things for automating it more.




## Install Prerequisites


```bash
sudo apt install -y libboost-dev
sudo apt install -y pkg-config
sudo apt install -y alsa
sudo apt install -y alsa-base
sudo apt install -y alsa-utils
sudo apt install -y libasound2-dev
sudo apt install -y libglib2.0-dev
sudo apt install -y libglibmm-2.4-dev 
sudo apt install -y libsndfile1-dev
sudo apt install -y libcurl4
sudo apt install -y libcurl4-openssl-dev
sudo apt install -y libarchive-dev
sudo apt install -y liblo-dev
sudo apt install -y libtaglib-ocaml-dev
sudo apt install -y libtagc0-dev 
sudo apt install -y libvamp-sdk2v5 
sudo apt install -y libvamp-hostsdk3v5
sudo apt install -y vamp-plugin-sdk
sudo apt install -y librubberband-dev 
sudo apt install -y libfftw3-dev
sudo apt install -y libaubio-dev
sudo apt install -y libxml2-dev 
sudo apt install -y libpangomm-1.4-dev
sudo apt install -y lv2-dev
sudo apt install -y libserd-dev 
sudo apt install -y libsord-dev 
sudo apt install -y libsratom-dev 
sudo apt install -y liblilv-dev 
sudo apt install -y libgtkmm-2.4-dev
sudo apt install -y libusb-1.0-0-dev
sudo apt install -y libsuil-dev
sudo apt install -y libcppunit-dev 
sudo apt install -y liblrdf0-dev 
sudo apt install -y libwebsockets-dev 
sudo apt install -y libcwiid-dev
sudo apt install -y libpulse-dev
sudo apt install -y libjack-dev 
sudo apt install -y libdbus-1-dev
sudo apt install -y libudev-dev
sudo apt install -y libclang-dev
sudo apt install -y clang-15
sudo apt install -y lib64readline8
sudo apt install -y lib64readline-dev 
sudo apt install -y libreadline-dev 
sudo apt install -y librubberband-dev
sudo apt install -y libclang-dev
sudo apt install -y clang-15
sudo apt install -y libclang-15-dev
sudo apt install -y clang
sudo apt install -y clang-14 clang-13 clang-12
sudo apt install -y libclang-14-dev libclang-13-dev libclang-12-dev
```

## Clone Repository 

git clone https://github.com/Ardour/ardour.git

cd ardour

```bash
./waf configure
./waf
./waf install
./waf clean
```