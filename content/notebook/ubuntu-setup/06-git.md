---
title: 06-Install and Setup ```git```
weight: 60
tags:
- ubuntu
- linux
- git
summary: ""
---

## Git

Git is the command line program for interacting with a git repository

```bash
sudo apt install -y git kdiff3
git config --global pull.rebase false
git config --global advice.addIgnoredFile false
git config --global init.defaultBranch main
```

then configure it

```bash
git config --global user.email "yourname@yourdomain.com"
git config --global user.name "Your Name"
```

for example:

```bash
git config --global user.email "danaukes@danaukes.com"
git config --global user.name "Dan Aukes"
```
