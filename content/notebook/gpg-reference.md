---
title: GPG Reference
tags: 
  - linux
  - ubuntu
  - gpg
  - encryption
  - keys
---

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

