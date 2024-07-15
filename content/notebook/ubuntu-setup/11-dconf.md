---
title: 11-Setup Dconf
weight: 110
tags:
- ubuntu
- linux
- dconf
---

## Introduction

Dconf is where many keyboard shortcuts and user preferences exist.  I have a couple tweaks I like to load.

## Load your previously saved settings

```bash

dconf load /org/gnome/desktop/wm/keybindings/ < my/remote/filesystem/keybindings.dconf
dconf load /org/gnome/settings-daemon/plugins/media-keys/ < my/remote/filesystem/media-keys.dconf
```

## More Info on Backup and Restore From command line

from <https://askubuntu.com/questions/682513/how-to-backup-restore-system-custom-keyboard-shortcuts>:

backup:
```
dconf dump /org/gnome/desktop/wm/keybindings/ > keybindings.dconf
dconf dump /org/gnome/settings-daemon/plugins/media-keys/ > media-keys.dconf
dconf dump /org/gnome/shell/extensions/dash-to-dock/ > dash-to-dock.dconf
dconf dump /org/gnome/desktop/interface/ > interface.dconf
dconf dump /com/ubuntu/touch/system/ >> screen.dconf
```

restore

```
dconf load /org/gnome/desktop/wm/keybindings/ < keybindings.dconf
dconf load /org/gnome/settings-daemon/plugins/media-keys/ < media-keys.dconf
dconf load /org/gnome/shell/extensions/dash-to-dock/ < dash-to-dock.dconf
dconf load /org/gnome/desktop/interface/ < interface.dconf
dconf load /com/ubuntu/touch/system/ < screen.dconf
```


## Full Config

suggestion from [here](https://unix.stackexchange.com/questions/77277/how-to-append-multiple-lines-to-a-file):

```
cat <<EOT >> keybindings.dconf
[/]
maximize=@as []
minimize=['<Super>Down']
show-desktop=['<Super>m']
toggle-maximized=['<Super>Up']
unmaximize=@as []
EOT

dconf load /org/gnome/desktop/wm/keybindings/ < keybindings.dconf
rm keybindings.dconf

cat <<EOT >> media-keys.dconf
[/]
home=['<Super>e']
EOT

dconf load /org/gnome/settings-daemon/plugins/media-keys/ < media-keys.dconf
rm media-keys.dconf

cat <<EOT >> dash-to-dock.dconf
[/]
dash-max-icon-size=32
extend-height=false
preferred-monitor-by-connector='primary'
show-trash=false
EOT

dconf load /org/gnome/shell/extensions/dash-to-dock/ < dash-to-dock.dconf
rm dash-to-dock.dconf

cat <<EOT >> interface.dconf
[/]
clock-format='12h'
color-scheme='prefer-light'
cursor-theme='Yaru'
document-font-name='Sans 11'
font-antialiasing='rgba'
font-hinting='slight'
font-name='Ubuntu 11'
gtk-theme='Yaru'
icon-theme='Yaru'
monospace-font-name='Ubuntu Mono 13'
show-battery-percentage=true
text-scaling-factor=0.85
EOT

dconf load /org/gnome/desktop/interface/ < interface.dconf
rm interface.dconf


```


