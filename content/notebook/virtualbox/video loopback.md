---
title: Looping Video into Zoom
tags:
  - zoom
  - linux
  - ubuntu
  - fun
weight: 99
---

```bash
sudo apt-get install v4l2loopback-dkms v4l-utils
```
```bash
ls /dev/video*
```
```bash
sudo modprobe v4l2loopback video_nr=9 card_label=“Virtual cam” 
```
```bash
ffmpeg -stream_loop -1 -re -i 2020-10-01-110554.webm -f v4l2 /dev/video9
```
```bash
sudo modprobe -r v4l2loopback
```

## External Links

* <https://yasha.solutions/virtual-webcam-on-linux/>
* <https://theterminallife.com/using-ffmpeg-and-v4l2-loopback-to-play-youtube-videos-as-a-webcam/>
* <https://github.com/umlaeute/v4l2loopback/>
* <https://github.com/webcamoid/akvcam>
