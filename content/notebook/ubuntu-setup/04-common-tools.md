---
title: Install Common Tools
weight: 40
tags:
- ubuntu
- linux
---

This assumes you installed a "minimal" version of Ubuntu

## ```apt``` packages first

Update your software first

```bash
sudo apt update
#save this for the end
# sudo apt upgrade -y  
```

Install new packages

```bash
sudo apt install -y \
kdiff3 \
ffmpeg \
qdirstat \
net-tools \
dconf-editor \
openssh-server \
remmina \
usb-creator-gtk \
gmsh \
tmux \
nmap \
p7zip-full \
pdfgrep \
gnome-tweaks \
etherwake \
ethtool \
fonts-roboto* \
httrack \
webhttrack \
meld \
gnome-shell-extensions \
libheif-examples \
autossh \
qrencode \
zbar-tools \
qtqr \
v4l2loopback-dkms \
v4l-utils \
gitg \
htop \
tree \
iperf \
ipe \
darktable \
exfat-fuse exfatprogs \
git-filter-repo \
blueman
```

### Optional

```bash
# sudo apt install -y \
# samba \
# wireguard \
# openresolv \
# sound-juicer \
# libimage-exiftool-perl \
# cifs-utils \
# paper-icon-theme \
# kiwix-tools \
# wkhtmltopdf \
#synaptic \
# kicad # which is better,  apt or flathub?
# solaar # battery drain?
# sudo apt install -y clementine # not my favorite
# fritzing # use flatpak?
```

## Flatpak

If you haven't yet already...

```bash
# install
sudo apt install -y flatpak
#if you want to install from software GUI
sudo apt install -y gnome-software-plugin-flatpak
#add the flathub repo
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## Install flatpaks

```bash
flatpak install -y flathub \
com.github.tchx84.Flatseal \
org.inkscape.Inkscape \
org.gimp.GIMP \
org.mozilla.firefox \
org.kicad.KiCad \
org.audacityteam.Audacity \
org.videolan.VLC \
com.bitwarden.desktop \
org.signal.Signal \
org.shotcut.Shotcut \
com.github.micahflee.torbrowser-launcher \
com.obsproject.Studio \
org.libreoffice.LibreOffice \
org.gnome.Rhythmbox3 \
org.raspberrypi.rpi-imager \
com.jetpackduba.Gitnuro \
com.github.xournalpp.xournalpp \
com.mattermost.Desktop \
org.fritzing.Fritzing \
com.rafaelmardojai.Blanket
# org.gpodder.gpodder \
# org.synfig.SynfigStudio
# net.xm1math.Texmaker\
# com.authy.Authy \
#us.zoom.Zoom \ #currently doesn't work with links or signon or sharing screen
#flatpak install flathub io.github.webcamoid.Webcamoid  #virtual camera driver not working
#flatpak install flathub org.darktable.Darktable  # font issue
```

optional

```bash
# flatpak install -y flathub \
# org.gnome.Cheese \
# org.kiwix.desktop \
# md.obsidian.Obsidian \
flatpak install flathub org.openscad.OpenSCAD
flatpak install flathub net.meshlab.MeshLab
flatpak install flathub org.blender.Blender
flatpak install flathub com.slack.Slack
```

close and reopen terminal

### Install snaps

```bash
sudo snap install mqtt-explorer
sudo snap install hugo --channel=extended
# sudo snap install superproductivity # no longer matches android appa
```

### Remove Firefox AGAIN

```bash
sudo snap remove firefox
```

### Flatseal config

* add whole filesystem to mozilla
* add user files to thunderbird
* add user space to fritzing
* turn off wayland for fritzing
* turn onn x11 fallback for fritzing


### Zoom

<https://zoom.us/download#client_4meeting>

### Ubuntu Mainline

```bash
sudo add-apt-repository ppa:cappelikan/ppa
sudo apt update && sudo apt install mainline
```

## Packages with options or multiple setup lines

### Thunderbird

```bash
flatpak install flathub org.mozilla.Thunderbird -y
```

move configuration from backup to ~/.var/app/org.mozilla.Thunderbird/.thunderbird/

turn off threading: <https://support.mozilla.org/en-US/questions/1426449>

### Pandoc

* <https://github.com/jgm/pandoc/releases/latest>
* <https://pandoc.org/installing.html>

dependencies

```bash
sudo apt install -y librsvg2-bin
```


### Anytype

<https://download.anytype.io/>

### Other tutorials

- [world clocks](/notebook/multiple-clocks/)
- [git clients](/notebook/install-git-clients/)
- [vscode]((/notebook/vscode-setup/))
- [docker](/notebook/docker/install-docker/)

### Latex

#### Full Install

```bash
sudo apt install -y texlive-full
```

<!--
#### Necessary Packages
This is a big install so plan it for when you can let it go a while

```bash
sudo apt install texlive-science texlive-xetex texlive-latex-recommended texlive-lang-english texlive-fonts-recommended texlive-base texlive-fonts-extra
```
-->

### Arduino

```bash
cd ~/Downloads
#sudo apt install -y arduino #outdated
python3 -mwebbrowser "https://www.arduino.cc/en/software"
```

To download version 1.8.19...

```bash
wget https://downloads.arduino.cc/arduino-1.8.19-linux64.tar.xz
tar -xvf arduino-1.8.19-linux64.tar.xz
cd arduino-1.8.19
sudo bash install.sh
```
you need to modify .bashrc to point python3 to python because we use anaconda

```bash
echo "alias python=python3" >> ~/.bashrc
```


### Cisco VPN for ASU

1. Go to <https://sslvpn.asu.edu/> and install the linux client
1. Extract installer image.  Locate the download file anyconnect-linux64-#.#.#####-core-vpn-webdeploy-k9.sh.
1. Open Terminal and issue the command:

    ```bash
    sudo bash anyconnect-linux*.sh
    ```

1. add to path

    ```bash
    echo "export PATH=\$PATH:/opt/cisco/secureclient/bin" >> ~/.bashrc
    source ~/.bashrc 
    ```

1. to run from command line, run ```vpn connect``` or ```vpn disconnect```

### Virtualbox

```bash
sudo apt install -y virtualbox virtualbox-ext-pack virtualbox-guest-additions-iso virtualbox-guest-utils
sudo usermod -a -G vboxusers $USER
sudo modprobe vboxdrv
```

to reinstall:

```bash
sudo apt reinstall virtualbox-dkms virtualbox-ext-pack virtualbox-guest-additions-iso virtualbox-guest-utils virtualbox-qt virtualbox
sudo modprobe vboxdrv
```

### Common Windows Fonts

Derived from [here](https://askubuntu.com/questions/651441/how-to-install-arial-font-and-other-windows-fonts-in-ubuntu):

```bash
sudo apt install -y ttf-mscorefonts-installer
sudo fc-cache -f
```


### VSCode

</notebook/vscode-setup/>

#### old

Find help [here](https://code.visualstudio.com/docs/setup/linux)

Download from [here](https://code.visualstudio.com/Download)

```bash
cd ~/Downloads
sudo dpkg -i code_1.72.2-1665614327_amd64.deb 
sudo apt install -yf
```

install python, c/c++, html css, jupyter


### Mosquitto

```bash
sudo apt install mosquitto mosquitto_clients
```

--------------------------------

## Optional


### Webcamoid

```bash
mkdir ~/apps
cd Downloads
wget "https://github.com/webcamoid/webcamoid/releases/download/9.0.0/webcamoid-portable-linux-9.0.0-x86_64.AppImage"
mv webcamoid-portable-linux-9.0.0-x86_64.AppImage cd ~/apps
cd ~/apps
chmod +x webcamoid-portable-linux-9.0.0-x86_64.AppImage
./webcamoid-portable-linux-9.0.0-x86_64.AppImage
```

### Cura

```bash
flatpak install flathub com.ultimaker.cura
```


<!--
script to download 64-bit generic 

```bash
mkdir ~/apps
cd ~/apps && \
url="https://www.mendeley.com/download-reference-manager/linux" && \
xpath="/html/body/div[2]/section[1]/div[1]/a" && \
html=$(wget -q -O - "$url") && \
dl_url=$(echo $html | xmllint --html --xpath "string($xpath/@href)" - 2>/dev/null | xargs)  && \
wget "$dl_url" && \
chmod +x mendeley*.AppImage
```
-->



<!--
#### Mendeley Desktop on Ubuntu 21 and older

```
cd ~/Downloads
sudo dpkg -i mendeleydesktop*.deb
sudo apt-get install -yf
```
-->

<!--
### Tor Browser

Old method:

```bash
#sudo add-apt-repository ppa:micahflee/ppa # this repository is deprecated
sudo apt update 
sudo apt install torbrowser-launcher
```
-->


### FreeCad

```bash
wget https://github.com/FreeCAD/FreeCAD/releases/download/0.20.2/FreeCAD_0.20.2-2022-12-27-conda-Linux-x86_64-py310.AppImage
```

---

## Deprecated



### Mendeley Reference Manager

go to [mendeley](https://www.mendeley.com/download-mendeley-desktop-legacy#download), download 64-bit generic version, unzip and move to ~/apps

```bash
mkdir ~/apps
cd ~/apps
wget https://www.mendeley.com/autoupdates/installer/Linux-x64/stable-incoming -O mendeley-desktop.tar.bz2
tar -xvjf mendeley-desktop.tar.bz2 
rm mendeley-desktop.tar.bz2 
```

### Vocal

<https://flathub.org/apps/details/com.github.needleandthread.vocal>

```
flatpak install flathub com.github.needleandthread.vocal
flatpak run com.github.needleandthread.vocal
```

### Ruby and Jekyll Toolchain

Trying to move away from ruby and jekyll...too hard

```bash
sudo apt-get update 
sudo apt install -y ruby git  build-essential ruby-dev pandoc-citeproc
sudo gem install bundler jekyll
```

### Screen

```bash
sudo apt install -y screen
```



### Numix Theme

```
sudo apt update
sudo add-apt-repository ppa:numix/ppa
sudo apt install -y gnome-tweaks numix-gtk-theme numix-icon-theme numix-icon-theme-circle
```

open tweak tool and set icons and theme to numix




### Chromium

You need to add some permissions to get chromium working with microphones...

[reference](https://askubuntu.com/questions/1148074/i-can-not-use-the-microphone-on-websites-using-chromium)

```bash
sudo snap install chromium
snap connections chromium  # to list existing permissions
sudo snap connect chromium:audio-record :audio-record  # to enable
```

### GitKraken

```bash
cd ~/Downloads
wget https://release.axocdn.com/linux-standalone/gitkraken-amd64.deb
sudo dpkg -i gitkraken-amd64.deb
```
