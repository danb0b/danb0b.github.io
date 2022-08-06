---
title: 04-Install Common Tools
weight: 4
tags:
- ubuntu
- linux
---

## Install common tools

I've lumped these all together to be able to run it more efficiently.  You will need these tools.

This assumes you installed a "minimal" version of Ubuntu

```bash
sudo apt update
sudo apt install -y synaptic kdiff3 libreoffice samba gimp ffmpeg qdirstat net-tools wireguard openresolv fritzing audacity dconf-editor kicad vlc openssh-server remmina usb-creator-gtk gmsh tmux nmap p7zip-full sound-juicer pdfgrep gnome-tweaks webcamoid etherwake ethtool fonts-roboto* libimage-exiftool-perl clementine httrack webhttrack yt-dlp youtube-dl meld cifs-utils paper-icon-theme

#migrated away from or to flathub
#sudo apt install -y gimp wireguard synaptic kicad audacity webcamoid vlc

#sudo apt install mosquitto mosquitto_clients #only if you want mqtt
#sudo snap remove firefox
#sudo apt install firefox
#sudo apt install -y inkscape
#sudo apt install -y openssh-client #already installed
sudo apt install -y libinput-tools #not sure what this is used for
#sudo snap install shotcut --classic
sudo snap install mqtt-explorer 
sudo snap install hugo --channel=extended
#sudo snap install signal-desktop

# install
sudo apt install flatpak
#if you want to install from software GUI
sudo apt install gnome-software-plugin-flatpak
#add the flathub repo
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

flatpak install flathub org.inkscape.Inkscape -y
flatpak install flathub org.gimp.GIMP
flatpak install flathub org.mozilla.firefox -y
flatpak install flathub org.kicad.KiCad
flatpak install flathub org.audacityteam.Audacity
flatpak install flathub io.github.webcamoid.Webcamoid
flatpak install flathub org.videolan.VLC
flatpak install flathub com.bitwarden.desktop
flatpak install flathub com.slack.Slack
flatpak install flathub us.zoom.Zoom
flatpak install flathub org.gnome.Cheese
flatpak install flathub org.signal.Signal
flatpak install flathub org.shotcut.Shotcut

#sudo snap install inkscape # doesn't work well on 21.10
```

### Bitwarden

install browser plugins here:

go here: <https://bitwarden.com/download/>

### Latex

This is a big install so plan it for when you can let it go a while

```bash
#sudo apt install -y texlive-full
sudo apt install texlive-science texlive-xetex texlive-latex-recommended texlive-lang-english texlive-fonts-recommended texlive-base
```

## Optional

### Arduino

```bash
cd ~/Downloads
#sudo apt install -y arduino #outdated
python -mwebbrowser "https://www.arduino.cc/en/software"
wget https://downloads.arduino.cc/arduino-1.8.16-linux64.tar.xz
tar -xvf arduino*linux64.tar.xz 
cd arduino-1.8.16
sudo bash install.sh
```




### Mendeley Reference Manager

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


#### Mendeley Desktop on Ubuntu 22 and newer:

go to https://www.mendeley.com/download-mendeley-desktop-legacy#download

download 64-bit generic version, unzip and move to ~/apps

#### Mendeley Desktop on Ubuntu 21 and older

```
cd ~/Downloads
sudo dpkg -i mendeleydesktop*.deb
sudo apt-get install -yf
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
    echo "export PATH=\$PATH:/opt/cisco/anyconnect/bin" >> ~/.bashrc
    source ~/.bashrc 
    ```
1. to run from command line, run ```vpn connect``` or ```vpn disconnect```


### Virtualbox

```bash
sudo apt install -y virtualbox virtualbox-ext-pack
sudo usermod -a -G vboxusers $USER
```

### flathub

```bash
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

### Tor Browser

```bash
flatpak install com.github.micahflee.torbrowser-launcher
```

Old method:

```bash
#sudo add-apt-repository ppa:micahflee/ppa # this repository is deprecated
sudo apt update 
sudo apt install torbrowser-launcher
```

### Vocal

<https://flathub.org/apps/details/com.github.needleandthread.vocal>

```
flatpak install flathub com.github.needleandthread.vocal
flatpak run com.github.needleandthread.vocal
```
---

## Deprecated

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

### Zoom

```
cd ~/Downloads
wget https://asu.zoom.us/client/latest/zoom_amd64.deb
sudo dpkg -i zoom_amd64.deb 
sudo apt install -yf
```








