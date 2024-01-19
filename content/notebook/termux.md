---
title: Handy Termux Commands
tags:
  - android
  - bash
  - termux
  - linux
---
 
```bash
pkg install openssl openssh gnupg iproute2
pkg install nmap # port scanning
pkg install dnsutils # dig
pkg install termux-tools
termux-setup-storage

pkg install python3 git
pkg install cmake
pip install matplotlib
pkg update
pkg install tsu # is this necessary?
pkg install nmap
pkg install texlive-bin
#pkg install texlive-full 
pkg upgrade
termux-change-repo
termux-install-tl
tlmgr update --all

```


https://wiki.termux.com/wiki/Internal_and_external_storage

```bash
ip a
```


https://www.modmy.com/how-modify-hosts-file-your-android-device
./adb pull /system/etc/hosts ./

