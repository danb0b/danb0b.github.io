---
title: NixOS Setup
tags:
- linux
- nixos
---

## External Resources

- <https://nixos.org/manual/nixos/stable/index.html#preface>
- <https://nixos.org/manual/nixos/stable/index.html#sec-changing-config>
- <https://nixos.org/manual/nixos/stable/index.html#ch-configuration>


```

  networking.hostName = "dannix";
  nixpkgs.config.allowUnfree = true;

  #virtualisation.virtualbox.host.enable = true;
  #users.extraGroups.vboxusers.members = [ "user-with-access-to-virtualbox" ];
  #virtualisation.virtualbox.host.enableExtensionPack = true;

  services.openssh.enable = true;
  users.users.danaukes.openssh.authorizedKeys.keys = [ "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICBtlkBLsL3EMYRjY9eI9lA3xe8goNWAJnyo+TaKxq/y danaukes@danaukes-Precision-7920-Tower" ];

  networking.firewall.enable = true;
  networking.firewall.allowedTCPPorts = [ 22 ];

  system.autoUpgrade.enable = true;
  system.autoUpgrade.allowReboot = true;

  virtualisation.virtualbox.guest.enable = true;
  virtualisation.virtualbox.guest.x11 = true;

  services.flatpak.enable = true;
  xdg.portal.extraPortals = [ pkgs.xdg-desktop-portal-kde ];

```


```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## Virtualbox

https://nixos.wiki/wiki/VirtualBox

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
com.slack.Slack \
us.zoom.Zoom \
org.gnome.Cheese \
org.signal.Signal \
org.shotcut.Shotcut \
com.github.micahflee.torbrowser-launcher \
com.obsproject.Studio \
org.libreoffice.LibreOffice \
org.gpodder.gpodder \
md.obsidian.Obsidian \
org.gnome.Rhythmbox3 \
org.raspberrypi.rpi-imager \
com.authy.Authy
```

## VSCode

from: <https://nixos.wiki/wiki/Visual_Studio_Code>


environment.systemPackages = with pkgs; [ vscode ];

environment.systemPackages = with pkgs; [
  (vscode-with-extensions.override {
    vscodeExtensions = with vscode-extensions; [
      bbenoist.nix
      ms-python.python
      ms-azuretools.vscode-docker
      ms-vscode-remote.remote-ssh
    ] ++ pkgs.vscode-utils.extensionsFromVscodeMarketplace [
      {
        name = "remote-ssh-edit";
        publisher = "ms-vscode-remote";
        version = "0.47.2";
        sha256 = "1hp6gjh4xp2m1xlm1jsdzxw9d8frkiidhph6nvl24d0h8z34w49g";
      }
    ];
  })
];


## Home Manager

### Installation

<https://nix-community.github.io/home-manager/index.html#sec-install-standalone>