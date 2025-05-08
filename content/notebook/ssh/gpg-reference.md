---
title: GPG Reference
tags: 
  - linux
  - ubuntu
  - gpg
  - encryption
  - keys
weight: 2
summary: " "
---

### create a new key

```bash
gpg --full-generate-key
```

### import

```bash
gpg --import <filename>
```

### export

```bash
gpg --export-secret-keys <filename>.gpg
```

adding --armor ensures the key is saved in ASCII format:


```bash
gpg --armor --export-secret-keys <filename>.gpg
```


### List gpg keys

```bash
gpg --list-keys
gpg --list-secret-keys
```

prints out ids

### delete gpg secret keys

```bash
gpg --delete-secret-keys KEYIDFROMABOVE
gpg --delete-keys KEYIDFROMABOVE
```

### decrypt

```bash
gpg --output /my/path/to/output_file.ext --decrypt /my/encrypted/source/file.gpg
```

### importing and trusting keys

```bash
gpg --list-keys
#or
gpg -K
```

copy the <KEY_ID>

```bash
gpg --edit-key <KEY_ID>
```

```text
gpg> trust

  1 = I don't know or won't say
  2 = I do NOT trust
  3 = I trust marginally
  4 = I trust fully
  5 = I trust ultimately
  m = back to the main menu
```

1. select 5, yes
1. type ```q``` to exit


## Update passphrase

gpg --edit-key <key id>

gpg> passwd

enter the password

```save```
q to exit

## encrypt without passphrase dialog

```bash
gpg --encrypt --passphrase-file </path/to/passphrase> --sign -r <who_to_sign_for> </path/to/file/to/encrypt>
```

## External references

* <https://stackoverflow.com/questions/33361068/gnupg-there-is-no-assurance-this-key-belongs-to-the-named-user>
* <https://www.cyberciti.biz/faq/linux-unix-gpg-change-passphrase-command/>
