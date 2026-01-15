---
title: simple gitman install
weight: 26
---

```bash
sudo apt install -y git python3-pip python3-venv build-essential libffi-dev
python3 -m venv ~/envs/gitman
. envs/gitman/bin/activate
pip3 install --upgrade pip
pip3 install wheel
pip3 install git_manage
```

If there's a specific git repository you want to check out:

```bash
gitman clone -r <https://github.com/path/to/your/repository.git>
```

otherwise, use

```bash
gitman clone
```

don't forget to [initialize repositories with submodules](/notepad/git/find-submodules)