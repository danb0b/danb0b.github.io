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

## Basic Functionality

To get the same functionality as explained in the answer recommending screen, you would need to do the following:

1. ssh into the remote machine
1. start tmux by typing tmux into the shell
1. start the process you want inside the started tmux session
1. leave/detach the tmux session by typing Ctrl+b and then d

You can now safely log off from the remote machine, your process will keep running inside tmux. When you come back again and want to check the status of your process you can use tmux attach to attach to your tmux session.

If you want to have multiple sessions running side-by-side, you should name each session using Ctrl+b and $. You can get a list of the currently running sessions using tmux list-sessions, now attach to a running session with command tmux attach-session -t <session-name>.

tmux can do much more advanced things than handle a single window in a single session. For more information have a look in man tmux or the tmux GitHub page. In particular, here's an FAQ about the main differences between screen and tmux.

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
