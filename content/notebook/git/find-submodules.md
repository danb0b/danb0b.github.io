---
title: Finding Submodules
---

```bash
find repos/ -not \( -path repos/external -prune \) -iname .gitmodules -type f
```

```bash
git submodule update --init --recursive
```

nano the ```.git/modules/<submodule_name>/config``` file

update the url to match the ssh spec:

```bash
url = git@<custom-header>.github.com:<orgname>/<repositoryname>.git
```