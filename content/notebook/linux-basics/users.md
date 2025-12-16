---
title: User Management
tags:
- linux
- ubuntu
summary: "Managing Users in Linux / Ubuntu"
---

## Password

```bash
sudo passwd <username>
```

you may want to remove your keyring lock file as it doesn't always update:

```bash
rm ~/.local/share/keyrings/login.keyring 
```

## Users, groups

From:

* <https://linuxize.com/post/how-to-add-and-delete-users-on-ubuntu-20-04/>
* <https://askubuntu.com/questions/410244/is-there-a-command-to-list-all-users-also-to-add-delete-modify-users-in-the>

## Create a new user

```bash
sudo adduser username
```

This runs an interactive q&a to create a new user, which is fine  if you are interacting with bash.  If you want to script, you can use ```useradd```, a lower-level command with more command-line options that permits you to enter a password in the command options, add the user to groups right away, and create the home directory.

```bash
useradd -m my_new_username -p $(openssl passwd my_custom_password) \
&& usermod -s /bin/bash my_new_username \
&&  usermod -aG sudo,other_groups,another_group my_new_username
```

you can create a new user and group by specifying groupid and uid, too, if you need to be specific.

```bash
MYUSER=ubuntu
MYGID=1000
MYUID=1000

groupadd -g ${MYGID} ${MYUSER}
useradd -u ${MYUID} -g ${MYGID} -p $(perl -e 'print crypt($ARGV[0], \
"password")' 'password') -G adm,sudo ${MYUSER} && mkdir /home/${MYUSER} \
&& chown ${MYUSER}:${MYUSER} /home/${MYUSER}
```

note the two ways to generate a valid password are to substitute

```bash
-p $(perl -e 'print crypt($ARGV[0], "password")' 'password')
```

with

```bash
-p $(openssl passwd my_custom_password)
```

if you have openssl installed.   Also note the different approach to encrypting the password (lower-level) and creating directories.

### Create a non-login user

Useful for creating a user that should not have login privileges

```bash
sudo adduser <username> --disabled-login
```

## Groups

Create a new group with

```bash
sudo addgroup groupname
```

You can also create a new group by gid

```bash
groupadd -g <group-id> <groupname>
```

Find groups associated with current user:

```bash
groups $USER
```

Add new user to new groups

```bash
sudo usermod -aG adm username
sudo usermod -aG sudo username
#...
```

### Directly modify groups user belongs to  

Unlike the last command(```-aG```), ```-G``` redefines rather than appends

```bash
sudo usermod -G usergroup,othergroup username
```

### Remove a user from a particular group

sudo deluser <username> <groupname>

### Change password

You can change the password with:

```bash
passwd [username]
```

delete root password

```bash
sudo passwd -l root
```

### Remove User

remove user from group

```bash
sudo deluser username groupname
```

remove user completely

```bash
sudo deluser --remove-home username
```

more tips here: <https://www.howtogeek.com/656549/how-to-delete-a-user-on-linux-and-remove-every-trace/>

### delete group

```bash
groupdel <groupname>
```

### Force new password

```bash
passwd --expire <username_here>
```

### Expire / unexpire

from here: <https://askubuntu.com/questions/282806/how-to-enable-or-disable-a-user>

Expire Account

Let the account expire to disallowing a user from logging in from any source including ssh:

```bash
# disallow peter from logging in
sudo usermod --expiredate 1 peter
```

This is how you can reenable that account:

```bash
# set expiration date of peter to Never
sudo usermod --expiredate "" peter
```

### List all users / groups

users:

```bash
cut -d: -f1 /etc/passwd
getent passwd
```

groups:

```bash
cut -d: -f1 /etc/group
getent group
```

### find out who is logged on

```bash
users
who
whoami
```

## List login times including boots

list login dates / times, users, etc

```bash
last
```
