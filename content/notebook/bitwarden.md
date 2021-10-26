---
title: Setting up Bitwarden
---

## Introduction

## Download

```bash
cd Downloads
python -mwebbrowser "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=appimage"
```
## Icon

download this file:

![Icon](/images/bw.png)

```bash
sudo mv bw.png /usr/share/pixmaps
```

## Create an "appimage" folder

```bash
mkdir ~/appimage
mv Bitwarden*.AppImage ~/appimage
```

## make a gnome icon
```bash
[Desktop Entry]
Type=Application
Name=Bitwarden
Comment=Bitwarden
Icon=bw
Exec=/home/danaukes/appimage/Bitwarden-1.28.3-x86_64.AppImage
Terminal=false
Categories=Bitwarden;
EOT

mv bitwarden.desktop ~/.local/share/applications
```

And you're good to go!
