---
title: Setting up Bitwarden
---

## Introduction

derived from [this link](https://askubuntu.com/questions/902672/registering-appimage-files-as-a-desktop-app)

## Download

```bash
python -mwebbrowser "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=appimage"
```
## Icon

download this file:

![Icon](/images/bw.png)

```bash
cd Downloads
wget https://danaukes.com/images/bw.png
sudo mv bw.png /usr/share/pixmaps
```

## Create an "appimage" folder

```bash
mkdir ~/appimage
mv Bitwarden*.AppImage ~/appimage
```

## make a gnome icon

Make sure to replace ```Bitwarden-1.28.3-x86_64.AppImage``` with the correct filename

```bash
cat <<EOT >> bitwarden.desktop
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
