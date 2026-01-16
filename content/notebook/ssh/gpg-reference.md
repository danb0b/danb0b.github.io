---
title: GPG Reference
tags: 
  - linux
  - ubuntu
  - gpg
  - encryption
  - keys
weight: 2
---
## Introduction

GPG is a great tool for encrypting files and handling the keys to do so.  The following commands are incredibly useful if you want to work with gpg from the command-line

# Commands

## Install and Setup

1. Install gnupg, nautilus integration (seahorse), and restart nautilus

    ```bash
    sudo apt install -y gnupg
    ```

1. Install kleopatra

    ```bash
    apt install -y kleopatra
    ```

## Import Keys

Configuration files can include sensitive information such as passwords, contact information, or other personal information you don't wish to share, even though you may wish to store it in the cloud for easy retrieval.  In that case it's a good idea to encrypt those files with a personal key.  Here is how you load your previously generated key so you can unencrypt them.

```bash
gpg --import "my/remote/filesystem/keys/file.asc"
```

## Generate

1. Run the generation script

    ```bash
    gpg --expert --full-gen-key
    ```

    1. Select option 9
    1. set expiration
    1. provide user info
    1. create passphrase

or use the quick version:

```bash
 gpg --quick-generate-key "test2 <test@test>" "default" "default" "never"
```

### Export

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

### encrypt a file without passphrase dialog

gpg --encrypt --passphrase-file </path/to/passphrase> --sign -r <who_to_sign_for> </path/to/file/to/encrypt>

#### Export

```bash
gpg --export-secret-keys --armor user-id > privkey.asc
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

an interface will open:

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

```bash
gpg --edit-key <key id>
```

```text
gpg> passwd
```

enter the password

```save```

```q``` to exit

## encrypt without passphrase dialog

```bash
gpg --encrypt --passphrase-file </path/to/passphrase> --sign -r <who_to_sign_for> </path/to/file/to/encrypt>
```

## External references

* <https://www.linuxbabe.com/security/a-practical-guide-to-gpg-part-1-generate-your-keypair>
* <https://stackoverflow.com/questions/33361068/gnupg-there-is-no-assurance-this-key-belongs-to-the-named-user>
* <https://www.cyberciti.biz/faq/linux-unix-gpg-change-passphrase-command/>
* <https://security.stackexchange.com/questions/235346/gpg-quick-generate-key-user-id-algo-usage-expire-any-way-to-include-a>
