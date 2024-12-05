---
title: Setting up Bitwarden
weight: 99
tags:
  - security
params:
  published: false
summary: " "
---

## Introduction

derived from [this link](https://askubuntu.com/questions/902672/registering-appimage-files-as-a-desktop-app)

## Steps

### Download

```bash
python -mwebbrowser "https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=appimage"
```
### Icon

download this file:

![Icon](/images/bw.png)

```bash
cd Downloads
wget https://danaukes.com/images/bw.png
sudo mv bw.png /usr/share/pixmaps
```

### Create an "appimage" folder

```bash
cd ~/Downloads
chmod +x Bitwarden*.AppImage 
mkdir ~/apps
mv Bitwarden*.AppImage ~/apps
```

### make a gnome icon

Make sure to replace ```Bitwarden-1.28.3-x86_64.AppImage``` with the correct filename

```bash
cat <<EOT >> bitwarden.desktop
[Desktop Entry]
Type=Application
Name=Bitwarden
Comment=Bitwarden
Icon=bw
Exec=/home/danaukes/apps/Bitwarden-1.28.3-x86_64.AppImage
Terminal=false
Categories=Bitwarden;
EOT

mv bitwarden.desktop ~/.local/share/applications
```

And you're good to go!

### Install Browser plugins

go here: <https://bitwarden.com/download/>

Install for your browser.


## External References

* <https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html>
* <https://askubuntu.com/questions/902672/registering-appimage-files-as-a-desktop-app>