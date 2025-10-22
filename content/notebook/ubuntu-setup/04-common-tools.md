---
title: Install Common Tools
weight: 40
tags:
- ubuntu
- linux
summary: " "
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
blueman \
librecad \
evince \
wireguard \
handbrake \
nrg2iso \
git-secret
```

### Optional

```bash
# sudo apt install -y \
# samba \
# screen \
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
com.rafaelmardojai.Blanket \
org.famistudio.FamiStudio \
io.dbeaver.DBeaverCommunity
# com.bitwarden.desktop \
# org.gpodder.gpodder \
# org.synfig.SynfigStudio
# net.xm1math.Texmaker\
# com.authy.Authy \
# com.ultimaker.cura \
#us.zoom.Zoom \ #currently doesn't work with links or signon or sharing screen
#flatpak install -y flathub io.github.webcamoid.Webcamoid  #virtual camera driver not working
#flatpak install -y flathub org.darktable.Darktable  # font issue
```

optional

```bash
# flatpak install -y flathub \
# org.gnome.Cheese \
# org.kiwix.desktop \
# md.obsidian.Obsidian \
flatpak install -y flathub org.openscad.OpenSCAD
flatpak install -y flathub net.meshlab.MeshLab
flatpak install -y flathub org.blender.Blender
flatpak install -y flathub com.slack.Slack
```

close and reopen terminal

### Install snaps

```bash
sudo snap install mqtt-explorer
sudo snap install hugo --channel=extended
sudo snap install bitwarden bw
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

```bash
sudo dpkg -i Downloads/zoo*.deb
```

### Ubuntu Mainline

```bash
sudo add-apt-repository ppa:cappelikan/ppa
sudo apt update && sudo apt install -y mainline
```

## Packages with options or multiple setup lines

### Thunderbird

```bash
flatpak install -y flathub org.mozilla.Thunderbird -y
```

move configuration from backup to ~/.var/app/org.mozilla.Thunderbird/.thunderbird/

turn off threading: <https://support.mozilla.org/en-US/questions/1426449>

### Pandoc

download

* <https://github.com/jgm/pandoc/releases/latest>
* <https://pandoc.org/installing.html>

prerequisites

```bash
sudo apt install -y librsvg2-bin
```

```bash
sudo dpkg -i Downloads/pandoc*.deb
```

<!-- 
### Anytype

<https://download.anytype.io/> 
-->

### Other tutorials

* [world clocks](/notebook/multiple-clocks/)
* [git clients](/notebook/install-git-clients/)
* [vscode](/notebook/vscode-setup/)
* [docker](/notebook/docker/install-docker/)
* [mosquitto](/notebook/linux-special-topics/mqtt/)
* [Nautilus Extensions](/notebook/linux-special-topics/nautilus-extensions/)

### Latex

#### Full Install

```bash
sudo apt install -y texlive-full
```

### Arduino

```bash
cd ~/Downloads
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
1. Extract installer image.  Locate the download file
1. Open Terminal and issue the command:

    ```bash
    sudo bash Downloads/cisco-*.sh
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
sudo usermod -a -G vboxusers,vboxsf $USER
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



### Numix Theme

```bash
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
