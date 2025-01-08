---
title: SSH General Reference
weight: 1
summary: The most useful SSH-specific commands
tags:
  - ubuntu
  - linux
  - ssh
  - encryption
  - keys
---

# Create a new SSH key

1. Use a key like "ed25519"

    ```bash
    ssh-keygen -t ed25519 -f <path/to/key>
    ```

2. print the public key:

    ```bash
    cat <path/to/key>.pub
    ```

3. add your key(s) to authorized keys:

    edit:

    ```bash
    sudo nano ~/.ssh/authorized_keys
    ```

    or copy directly:

    ```bash
    cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
    ```

    or distribute your keys with ```ssh-copy-id```

    ```bash
    ssh-copy-id -f -i <path/to/your/key>.pub user@server
    ```

1. update your .ssh/config file

    ```txt
    Host *
        IdentitiesOnly yes
        IdentityFile [path/to/new_file]
        ForwardAgent yes
        AddKeysToAgent yes
        User <user>
    ```

## Default Permissions

```bash
chmod 700 ~/.ssh # the .ssh directory itself
chmod 600 ~/.ssh/* # by default all the files in .ssh
chmod 644 ~/.ssh/*.pub # change public key permissions
```

## Other Helpful Stuff

### list all keys

```bash
ssh-add -l
```

### remove all keys

```bash
ssh-add -D
```

### add passphrase

```bash
ssh-keygen -p -f <path-to-key>
```

### create cert/key

from [here](https://support.microfocus.com/kb/doc.php?id=7013103):

openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem

## References

* <https://linuxnatives.net/2019/how-to-create-good-ssh-keys>
* <https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys>
* <https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-20-04>
* <https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server>
* <https://help.ubuntu.com/community/SSH/OpenSSH/Keys>
