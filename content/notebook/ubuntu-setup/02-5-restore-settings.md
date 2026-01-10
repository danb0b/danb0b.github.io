---
title: restore configurations
weight: 25
summary: How to restore config settings from a backup
---

```bash
gpg --output ~/backup.tar.gz --decrypt /my/remote/filesystem/backup_settings.tar.gz.gpg
```

```bash
tar -xvzf ~/backup.tar.gz
```

decompress rclone settings

```bash
tar -xvzf ~/temp/rclone.tar.gz 
```

decompress gitman settings

```bash
tar -xvzf ~/temp/gitman.tar.gz 
```

decompress vscode settings

```bash
tar -xvzf ~/temp/codium.tar.gz 
```

decompress thunderbird settings

```bash
tar -xvzf ~/temp/thunderbird.tar.gz
```

decompress firefox settings

```bash
tar -xvzf ~/temp/firefox.tar.gz
```

decompress latex files

```bash
tar -xvzf ~/temp/mytex.tar.gz
```

```bash
tar -xvzf ~/temp/_ssh.tar.gz
```


```bash
dconf load /org/gnome/desktop/wm/keybindings/ < ~/temp/keybindings.dconf
dconf load /org/gnome/settings-daemon/plugins/media-keys/ < ~/temp/media-keys.dconf
dconf load /org/gnome/shell/extensions/dash-to-dock/ < ~/temp/dash-to-dock.dconf
dconf load /org/gnome/desktop/interface/ < ~/temp/interface.dconf
dconf load /com/ubuntu/touch/system/ < ~/temp/screen.dconf
```

```bash
tar -xvzf ~/temp/syncthing.tar.gz
```

reimport network connections

```bash
sudo nmcli conn reload
```

## If you don't have another device to restore from

```bash
tar -xvzf ~/temp/keys.tar.gz
```
