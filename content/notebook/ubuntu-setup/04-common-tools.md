---
title: Install Common Tools
weight: 40
tags:
- ubuntu
- linux
---

This assumes you installed a "minimal" version of Ubuntu

## ```apt``` packages first

```bash
sudo apt update && sudo apt upgrade-y
```bash
sudo apt install -y synaptic kdiff3 samba gimp ffmpeg qdirstat net-tools wireguard openresolv fritzing  dconf-editor kicad vlc openssh-server remmina usb-creator-gtk gmsh tmux nmap p7zip-full sound-juicer pdfgrep gnome-tweaks etherwake ethtool fonts-roboto* libimage-exiftool-perl httrack webhttrack yt-dlp youtube-dl meld cifs-utils paper-icon-theme gnome-shell-extensions libheif-examples autossh qrencode zbar-tools qtqr v4l2loopback-dkms v4l-utils gitg htop
# sudo apt install -y clementine # not my favorite
sudo apt install -y darktable
```

## Flatpak

If you haven't yet already...

```bash
# install
sudo apt install flatpak
#if you want to install from software GUI
sudo apt install gnome-software-plugin-flatpak
#add the flathub repo
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## Install flatpaks

```bash
flatpak install flathub org.inkscape.Inkscape -y
flatpak install flathub org.gimp.GIMP -y
flatpak install flathub org.mozilla.firefox -y
flatpak install flathub org.kicad.KiCad -y
flatpak install flathub org.audacityteam.Audacity -y
#flatpak install flathub io.github.webcamoid.Webcamoid -y #virtual camera driver not working
flatpak install flathub org.videolan.VLC -y
flatpak install flathub com.bitwarden.desktop -y
flatpak install flathub com.slack.Slack -y
flatpak install flathub us.zoom.Zoom -y
flatpak install flathub org.gnome.Cheese -y
flatpak install flathub org.signal.Signal -y
flatpak install flathub org.shotcut.Shotcut -y
flatpak install com.github.micahflee.torbrowser-launcher -y
flatpak install com.obsproject.Studio -y
flatpak install org.libreoffice.LibreOffice -y
flatpak install org.gpodder.gpodder -y
#flatpak install org.darktable.Darktable -y # font issue
flatpak install flathub md.obsidian.Obsidian -y
flatpak install flathub org.gnome.Rhythmbox3 -y
```

close and reopen terminal

### Install snaps

```bash
sudo snap install mqtt-explorer
sudo snap install hugo --channel=extended
sudo snap install rpi-imager 
```

## Packages with options or multiple setup lines

### Thunderbird

```bash
flatpak install flathub org.mozilla.Thunderbird
```

move configuration from backup to ~/.var/app/org.mozilla.Thunderbird/.thunderbird/

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

### Webcamoid

```bash
cd Downloads
wget "https://github.com/webcamoid/webcamoid/releases/download/9.0.0/webcamoid-portable-linux-9.0.0-x86_64.AppImage"
mv webcamoid-portable-linux-9.0.0-x86_64.AppImage cd ~/apps
cd ~/apps
chmod +x webcamoid-portable-linux-9.0.0-x86_64.AppImage
./webcamoid-portable-linux-9.0.0-x86_64.AppImage
```

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
cd arduino-1.8.19-linux64
sudo bash install.sh
```

### Mendeley Reference Manager

go to [mendeley](https://www.mendeley.com/download-mendeley-desktop-legacy#download), download 64-bit generic version, unzip and move to ~/apps

```bash
mkdir ~/apps
cd ~/apps
wget https://www.mendeley.com/autoupdates/installer/Linux-x64/stable-incoming -O mendeley-desktop.tar.bz2
tar -xvjf mendeley-desktop.tar.bz2 
rm mendeley-desktop.tar.bz2 
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

### Cisco VPN for ASU

1. Go to <https://sslvpn.asu.edu/> and install the linux client
1. Extract installer image.  Locate the download file anyconnect-linux64-#.#.#####-core-vpn-webdeploy-k9.sh.
1. Open Terminal and issue the command:

    ```bash
    sudo bash anyconnect-linux*.sh
    ```

1. add to path

    ```bash
    echo "export PATH=\$PATH:/opt/cisco/anyconnect/bin" >> ~/.bashrc
    source ~/.bashrc 
    ```
1. to run from command line, run ```vpn connect``` or ```vpn disconnect```


### Virtualbox

```bash
sudo apt install -y virtualbox virtualbox-ext-pack
sudo usermod -a -G vboxusers $USER
```

### Common Windows Fonts

Derived from [here](https://askubuntu.com/questions/651441/how-to-install-arial-font-and-other-windows-fonts-in-ubuntu):

```bash
sudo apt install ttf-mscorefonts-installer
sudo fc-cache -f
```

<!--
### Tor Browser

Old method:

```bash
#sudo add-apt-repository ppa:micahflee/ppa # this repository is deprecated
sudo apt update 
sudo apt install torbrowser-launcher
```
-->

## Optional


### Mosquitto

```bash
sudo apt install mosquitto mosquitto_clients
```

---

## Deprecated


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






