---
title: Install and Setup ```git```
---

## Git

Git is the command line program for interacting with a git repository

```bash
sudo apt install -y git kdiff3
git config --global user.email "danaukes@gmail.com"
git config --global user.name "Dan Aukes"
git config --global pull.rebase false
```

## Git Extensions

Git Extensions is a useful gui that has been ported over to ubuntu.  It barely still works but provides continuity with windows, so I still use it

This assumes you have already installed git and kdiff3

from <https://github.com/gitextensions/gitextensions/wiki/How-To%3A-run-Git-Extensions-on-Linux>:

```
sudo apt install -y mono-complete
cd ~/Downloads
wget https://github.com/gitextensions/gitextensions/releases/download/v2.51.05/GitExtensions-2.51.05-Mono.zip
unzip GitExtensions-2.51.05-Mono.zip
rm GitExtensions/Plugins/Bitbucket.dll
chmod +x GitExtensions/GitExtensions.exe
mv GitExtensions ~/
#sudo cp ~/GitExtensions/git-extensions-logo-final-256.ico /usr/share/icons
echo "export PATH=\$PATH:$(realpath ~)/GitExtensions" >> ~/.bashrc
source ~/.bashrc
```

The run GitExtensions.exe and set up
