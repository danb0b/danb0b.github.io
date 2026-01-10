---
title: Setup and Use Ente Authenticator
weight: 13
tags:
  - linux
  - ubuntu
  - security
summary: how to install tailscale in linux
---

## Instructions

```bash
flatpak install -y io.ente.auth
```

## Deprecated Instructions

> These instructions are deprecated because I now use the flatpak, and because of this issue: <https://github.com/ente-io/ente/issues/3378>

download from here: <https://github.com/ente-io/ente/releases?q=tag%3Aauth-v4>

```bash
sudo apt install libfuse-dev

app_path="$(find ~/apps/ -iname '*ente*' | head -1)"

chmod +x $app_path

cat << EOL | sudo tee /usr/share/applications/ente.desktop
[Desktop Entry]
Name=Ente Auth
MimeType=
Exec=$app_path
Type=Application
GenericName=Ente Auth
Terminal=false
Icon=passwords-app-symbolic.svg
Comment=Ente Auth
StartupNotify=true;
Categories=System;
EOL

sudo chmod 644 /usr/share/applications/ente.desktop
```
