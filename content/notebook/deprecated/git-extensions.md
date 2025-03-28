---
title: Git Extensions Setup
tags:
- git
summary: " "
---


## Git Extensions

Git Extensions is a useful gui that has been ported over to ubuntu using mono.  It barely still works but provides continuity with windows, so I still use it

This assumes you have already installed git and kdiff3

from <https://github.com/gitextensions/gitextensions/wiki/How-To%3A-run-Git-Extensions-on-Linux>:

```bash
sudo apt install -y mono-complete
cd ~/Downloads
wget https://github.com/gitextensions/gitextensions/releases/download/v2.51.05/GitExtensions-2.51.05-Mono.zip
unzip GitExtensions-2.51.05-Mono.zip
rm GitExtensions/Plugins/Bitbucket.dll
chmod +x GitExtensions/GitExtensions.exe
mkdir ~/apps
mv GitExtensions ~/apps
echo "export PATH=\$PATH:$(realpath ~)/GitExtensions" >> ~/.bashrc
source ~/.bashrc
```

download this file:

![Icon](/images/git-extensions.png)

```bash
cd Downloads
wget https://danaukes.com/images/git-extensions.png
sudo mv git-extensions.png /usr/share/pixmaps
```

```bash
cat <<EOT >> git-extensions.desktop
[Desktop Entry]
Type=Application
Name=GitExtensions
Comment=GitExtensions
Icon=git-extensions
Exec=/home/danaukes/apps/GitExtensions/GitExtensions.exe
Terminal=false
Categories=Git;
EOT

mv git-extensions.desktop ~/.local/share/applications
```

Then run GitExtensions.exe and set up
