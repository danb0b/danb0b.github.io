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



## What is SSH

A way of securely and remotely connecting to another computer over tcp.

## SSH Client

Common command form

```bash
ssh user@<server-or-ip> -p <portnum> -i <identity/file/path>
```

### SSH One-liner

you can run a single command on a remote machine like this

```bash
ssh user@server 'command'
```

for example:

```bash
ssh danaukes@mycomputer 'echo "Hello World">>test.txt'
```

### Common arguments

* ```-p```: port number
* ```-i```: identity path file
* ```-v``` / ```-vv``` / ```-vvv``` / ```-vvvv```: levels of "verbosity"
* ```-o```: options you can specify

### SSH Client Configuration

You can configure your ssh client on a per-server basis with the .ssh/config file

> Note: this is an example, don't just copy/paste

Below we see an example

```txt
Host <name or *>
    # if you want to restrict your ssh client to only using keys
    IdentitiesOnly yes 
    # supply the default path to your identity file (key)
    IdentityFile <path/to/new_file>
    # default username
    User <username>
    # 
    ForwardAgent yes # set this option carefully
    AddKeysToAgent yes # set this option carefully
    ...many other options
```

The first entry to match will be used, so make sure you put more general rules, such as ```Host *``` at the end.

you can find more info here:

* <https://linuxhandbook.com/ssh-config-file/>
* <https://www.ssh.com/academy/ssh/config>
* <https://linuxize.com/post/using-the-ssh-config-file/>

or by typing

```bash
man ssh_config
```

## SSH Keys

# Create a new SSH key

1. Use a key like "ed25519"

    ```bash
    ssh-keygen -t ed25519 -f <path/to/key>
    ```

1. Select a passphrase
1. print the public key:

    ```bash
    cat <path/to/key>.pub
    ```

1. add your key(s) to authorized keys:

    There are many ways you can do this.  You can copy the key directly:

    ```bash
    cat <path/to/key>.pub >> ~/.ssh/authorized_keys
    ```

    edit the file and paste in the text:

    ```bash
    sudo nano ~/.ssh/authorized_keys
    ```

    or distribute your key to another server with ```ssh-copy-id```

    ```bash
    ssh-copy-id -f -i <path/to/your/key>.pub user@server
    ```

    you can also use a ssh one-liner:

    ```bash
    cat <path/to/your/key>.pub | \
    ssh <user_name>@<hostname-or-ip> 'cat >> .ssh/authorized_keys'
    ```

### update your .ssh/config file

These options are useful defaults setting up your client.

    ```txt
    Host *
        IdentitiesOnly yes
        IdentityFile [path/to/new_file]
        ForwardAgent yes
        AddKeysToAgent yes
        User <user>
    ```

## Default Permissions

It is important when you work with files related to secure communications, that you make it impossible for others to access your ssh keys and configuration settings

```bash
chmod 700 ~/.ssh # the .ssh directory itself
chmod 600 ~/.ssh/* # by default all the files in .ssh
chmod 644 ~/.ssh/*.pub # change public key permissions
chmod 750 $HOME
```

<https://superuser.com/questions/215504/permissions-on-private-key-in-ssh-folder>

## SSH Server

### Installing OpenSSH Server

To accept incoming ssh connections,  install ```openssh-server```

```bash
sudo apt install -y openssh-server
```

### SSH server daemon

```systemctl```  can be used to control your server.  To enable the service so that it starts with your computer, type

```bash
sudo systemctl enable ssh 
```

The next time your computer starts, it will start.  To start it immediately, type

```bash
sudo systemctl start ssh 
```

### Other service commands

```bash
sudo systemctl stop ssh 
sudo systemctl disable ssh 
sudo systemctl reload ssh 
sudo systemctl restart ssh 
```

### Server Configuration

Configuring your ssh server is done in the
```/etc/ssh/sshd_config``` file and in the
```/etc/ssh/sshd_config.d/``` directory.

If your server is running, you can get the current configuration with

```bash
sshd -T
```

## Working with the key agent

ssh-add is the "agent" that manages the keys currently available to use.

### list all keys

```bash
ssh-add -l
```

### remove all keys

```bash
ssh-add -D
```

## Other related functions

### add passphrase

if you want to change the passphrase associated with an existing key

```bash
ssh-keygen -p -f <path-to-key>
```

### create a certificate and key

Sometimes, you need to create a certificate at the same time as a key.

from here: <https://support.microfocus.com/kb/doc.php?id=7013103>:

```bash
openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem
```

## External Resources

* <https://linuxnatives.net/2019/how-to-create-good-ssh-keys>
* <https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys>
* <https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-20-04>
* <https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server>
* <https://help.ubuntu.com/community/SSH/OpenSSH/Keys>
* <https://superuser.com/questions/215504/permissions-on-private-key-in-ssh-folder>
* <https://www.tecmint.com/set-ssh-directory-permissions-in-linux/>
* <https://www.howtogeek.com/168147/add-public-ssh-key-to-remote-server-in-a-single-command/>
* <https://linuxhandbook.com/add-ssh-public-key-to-server/>
