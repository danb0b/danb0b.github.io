---
title: Install Common Tools
---

## Install common tools

I've lumpted these all together to be able to run it more efficiently.  You will need these tools.

This assumes you installed a "minimal" version of Ubuntu

```bash
sudo apt update
sudo apt install -y synaptic kdiff3 libreoffice samba inkscape gimp ffmpeg qdirstat net-tools wireguard fritzing audacity dconf-editor kicad vlc openssh-server remmina usb-creator-gtk gmsh tmux nmap cheese p7zip-full
sudo apt install -y openssh-client
sudo apt install -y libinput-tools #not sure what this is used for
sudo snap install shotcut --classic
sudo snap install mqtt-explorer 
sudo snap install hugo --channel=extended
```

### Latex

This is a big install so plan it for when you can let it go a while

```bash
sudo apt install -y texlive-full
```

## Optional

### Arduino

```bash
sudo apt install -y arduino
```

### Numix Theme

```
sudo apt update
sudo add-apt-repository ppa:numix/ppa
sudo apt install -y gnome-tweak-tool numix-gtk-theme numix-icon-theme numix-icon-theme-circle
```

### Screen

```bash
sudo apt install -y screen
```

### Zoom

```
cd ~/Downloads
wget https://asu.zoom.us/client/latest/zoom_amd64.deb
sudo dpkg -i zoom_amd64.deb 
sudo apt install -yf
```

### Mendeley

```
cd ~/Downloads
wget https://www.mendeley.com/repositories/ubuntu/stable/amd64/mendeleydesktop-latest
sudo dpkg -i mendeleydesktop-latest
sudo apt-get install -yf
```

### Cisco VPN for ASU

1. Go to <https://sslvpn.asu.edu/> and install the linux client
1. Extract installer image.  Locate the download file anyconnect-linux64-#.#.#####-core-vpn-webdeploy-k9.sh.
1. Open Terminal and issue the command:

    ```bash
    sudo bash anyconnect-linux64-#.#.#####-core-vpn-webdeploy-k9.sh
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

---

## Deprecated

### Ruby and Jekyll Toolchain

Trying to move away from ruby and jekyll...too hard

```bash
sudo apt-get update 
sudo apt install -y ruby git  build-essential ruby-dev pandoc-citeproc
sudo gem install bundler jekyll
```

