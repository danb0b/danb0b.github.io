---
title: Run scripts remotely over ssh with ```tmux```
tags:
  - tmux
  - bash
  - terminal
  - linux
  - ubuntu
  - ssh
weight: 99
summary: " "
---

### Overview

tmux is tool that lets you run multiple sub-sessions from one session. It's good for  running simultaneous tasks that each need a terminal window without having  to open simultaneous, separate ssh sessions or opening multiple terminal windows.

It also allows terminal sessions to persist even when ssh sessions or terminal windows are closed, whether on purpose or unexpectedly.  This is great for installing or updating software, compiling large codebases, or other long tasks where remote connections could be unstable, or where simply window space is precious  and you've got multiple things going at once.

Steps:

1. first, from a terminal window or ssh session, type ```tmux```.
1. start the thing you want to do
1. hit ```ctrl``` + ```b``` then ```d``` to leave the  sesssion running
1. you will re-enter the parent session
1. to open it again, you can type ```tmux attach```

if you have multiple tmux sessions open, you can type

```bash
tmux list-sessions
```

to see which sessions are open. Then, if you want to open a particular one, take the number of the session you want to open, and type

```bash
tmux attach -t <num>
```

where ```<num>``` is the number of the session you want to enter that you got from the ```list-sessions``` response.

## Installation

```bash
sudo apt install -y tmux
```

## Usage

create a new session

```bash
tmux
```

leave a session without stopping it: ```ctrl+b```, then ```d```

list existing sessions

```bash
tmux list-sessions
```

attach to an existing session

```bash
tmux attach -t [session-number]
```

## External References

* <https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session>
