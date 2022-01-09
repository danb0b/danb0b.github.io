---
title: 11-Setup Keyboard Shortcuts
weight: 11
tags:
- ubuntu
- linux
---

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
```

restore

```
dconf load /org/gnome/desktop/wm/keybindings/ < keybindings.dconf
dconf load /org/gnome/settings-daemon/plugins/media-keys/ < media-keys.dconf
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

cat <<EOT >> media-keys.dconf
[/]
home=['<Super>e']
EOT

dconf load /org/gnome/settings-daemon/plugins/media-keys/ < media-keys.dconf

rm keybindings.dconf
rm media-keys.dconf
```
