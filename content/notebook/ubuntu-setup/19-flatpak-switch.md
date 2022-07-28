---
title: Switching to Flatpak
tags:
  - ubuntu
  - linux
  - flatpak
weight: 19
---


```bash
# install
sudo apt install flatpak
#if you want to install from software GUI
sudo apt install gnome-software-plugin-flatpak
#add the flathub repo
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## Also

```
flatpak update
```

## Inkscape

```bash
sudo apt remove Inkscape -y
flatpak install flathub org.inkscape.Inkscape -y
```


## firefox

```bash
sudo snap remove firefox -y
flatpak install flathub org.mozilla.firefox -y
flatpak run org.mozilla.firefox
```

## Kicad

```bash
sudo apt remove kicad
flatpak install flathub org.kicad.KiCad
```

## Audacity

```bash
sudo apt remove audacity
flatpak install flathub org.audacityteam.Audacity
```

## Webcamoid

Note: Cannot currently install the virtual cam output due to missing libraries

```bash
sudo apt remove webcamoid
flatpak install flathub io.github.webcamoid.Webcamoid
```

## VLC

```bash
sudo apt remove vlc
flatpak install flathub org.videolan.VLC
```

## Bitwarden

```bash
flatpak install flathub com.bitwarden.desktop
```

## Slack

```bash
flatpak install flathub com.slack.Slack
```

## Zoom

```bash
sudo apt remove zoom
flatpak install flathub us.zoom.Zoom
```

## Cheese
```bash
sudo apt remove cheese
flatpak install flathub org.gnome.Cheese
```

## LibreOffice

```bash
sudo apt remove libreoffice*
sudo apt autoremove
flatpak install flathub org.libreoffice.LibreOffice
```

## Darktable

```bash
flatpak install flathub org.darktable.Darktable
```

## Gimp

```bash
sudo apt remove gimp
flatpak install flathub org.gimp.GIMP
```

## Gpodder

```bash
flatpak install flathub org.gpodder.gpodder
```

--------------------

# Not Recommended

## Kdiff

didn't seem to work...

```bash
sudo apt remove kdiff3 -y
flatpak install flathub org.kde.kdiff3 -y
```
