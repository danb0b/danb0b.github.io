---
title: Installing GrapheneOS on a Pixel 4a
tags:
  - android
  - grapheneos
  - ubuntu
  - security
---



Instructions derived from <https://grapheneos.org/install/cli>

## Download Developer Tools

```bash
sudo apt install -y android-sdk-platform-tools-common
sudo apt install -y signify-openbsd
echo "alias signify=signify-openbsd" >> ~/.bashrc
sudo apt remove adb 
mkdir ~/adb
cd ~/adb
sudo apt install -y libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r33.0.3-linux.zip
echo 'ab885c20f1a9cb528eb145b9208f53540efa3d26258ac3ce4363570a0846f8f7  platform-tools_r33.0.3-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r33.0.3-linux.zip
echo "export PATH=\$PATH:/home/danaukes/adb/platform-tools" >> ~/.bashrc
which fastboot
fastboot --version
```

## Download graphene

go to <https://grapheneos.org/releases#bramble-stable>

```bash
wget https://releases.grapheneos.org/bramble-factory-2022071300.zip.sig
wget https://releases.grapheneos.org/bramble-factory-2022071300.zip
```

## Prep Phone

1. Turn on developer mode
1. go to settings --> "about phone"
1. press "build number" until developer mode is enabled
1. exit out of settings so that the new menu can load
1. go back to settings --> system --> developer options
1. enable "OEM unlocking"
1. restart phone in bootloader mode by restarting and holding the "volume down" button until the fastboot screen starts up.

```bash
cd ~/adb
wget https://releases.grapheneos.org/factory.pub
cat factory.pub 
signify-bsd -Cqp factory.pub -x bramble-factory-2022071300.zip.sig  && echo verified
bsdtar xvf bramble-factory-2022071300.zip
cd bramble-factory-2022071300/
fastboot flashing unlock
./flash-all.sh 
fastboot flashing lock
```

## Next Steps

* <https://f-droid.org/>
* <https://auroraoss.com/>

## VPN Issue

1. After installing tailscale, turn off blocking in vpn settings

<https://github.com/GrapheneOS/os-issue-tracker/issues/183>


## To return to the original

* <https://developers.google.com/android/images>
* <https://developers.google.com/android/ota>
* [factory image](https://dl.google.com/dl/android/aosp/bramble-sq3a.220705.003.a1-factory-87426cb6.zip)
* [ota image](https://dl.google.com/dl/android/aosp/bramble-ota-sq3a.220705.003.a1-1fefa3a0.zip)

## other resources

* [platform-tools website](https://developer.android.com/studio/releases/platform-tools.html)