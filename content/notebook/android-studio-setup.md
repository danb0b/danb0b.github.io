---
title: android studio
---


sudo apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386

download [android-studio](https://developer.android.com/studio)

----

## Old info

get a message about kvm

```bash
sudo apt-get install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils

sudo adduser $USER kvm
sudo adduser $USER libvirt
#sudo apt install -y qemu-kvm libvirt-clients libvirt-clients-qemu  bridge-utils
#sudo apt install libvirt-daemon-driver-qemu libvirt-daemon-system
```

flatpak install com.google.AndroidStudio 

## Tricks for getting chrome working and eliminating bugs / errors

install:

vip
duo
authy

config.ini

set memory to 2048-->8192 (hw.ramSize)
set heap from 256-->1024
turn off gpu

find the following lines and update as follows

```bash
vm.heapSize = 1024
hw.ramSize = 8192
hw.gpu.enabled = yes
hw.gpu.mode = host
```

turn off vulkan:
https://stackoverflow.com/questions/69134922/google-chrome-browser-in-android-12-emulator-doesnt-load-any-webpages-internet

```bash
cat << EOT | tee advancedFeatures.ini
Vulkan = off
GLDirectMem = on
EOT
```

then move it into your vm's location

```bash
#mv advancedFeatures.ini <final location>
mv advancedFeatures.ini ~/.android/avd/Pixel_6a_API_35.avd # for example
```

delete storage in chrome and uninstall updates.


## External Resources

* https://developer.android.com/studio/run/emulator-acceleration#vm-linux
* https://gist.github.com/ivgiuliani/6882218