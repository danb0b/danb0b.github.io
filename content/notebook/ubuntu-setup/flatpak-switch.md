---
title: Switching to Flatpak
tags:
  - ubuntu
  - linux
  - flatpak
---


```bash
# install
sudo apt install flatpak
#if you want to install from software GUI
sudo apt install gnome-software-plugin-flatpak
#add the flathub repo
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```
 
## Inkscape

```bash
sudo apt remove Inkscape -y
flatpak install flathub org.inkscape.Inkscape -y
```

## Kdiff

```bash
sudo apt remove kdiff3 -y
flatpak install flathub org.kde.kdiff3 -y
```

## firefox

```bash
sudo snap remove firefox -y
flatpak install flathub org.mozilla.firefox -y
flatpak run org.mozilla.firefox
```