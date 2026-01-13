---
title: Micropython on Linux
tags:
- linux
- ubuntu
- micropython
---

```bash
sudo apt install -y build-essential libffi-dev git pkg-config
git clone https://github.com/<your-user-name>/micropython
cd micropython
git remote add upstream https://github.com/micropython/micropython
git checkout -b dev-branch
cd ports/unix
make submodules
make
sudo make install
cd build-stadaard
.micropython
```

## External Resources

* <https://docs.micropython.org/en/latest/develop/gettingstarted.html#building-the-unix-port-of-micropython>
