---
title: Install and Setup SSH
weight: 06
---

```bash
mkdir ~/keys
gpg --output ~/keys/folder/key_filename1 --decrypt my/remote/filesystem/ssh/key_filename1.pgp
gpg --output ~/keys/folder/key_filename2 --decrypt my/remote/filesystem/ssh/key_filename2.pgp

mkdir ~/.ssh
cp my/remote/filesystem/ssh/config ~/.ssh/config

chmod 600 ~/keys/*
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*
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
