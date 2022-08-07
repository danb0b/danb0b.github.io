---
title: Git Commands
tags:
  - bash
  - git
  - github
weight: 10
---

to clone a repository:

```bash
git clone my_git_address
```

## Branches

list local branches:

```bash
git branch
```

list remote branches:

```
git branch --remote
```

Checkout and track a remote branch:

```bash
git checkout --track origin/xyz
```

Push a local branch to a new remote branch name

```bash
git push --set-upstream origin <remotebranchname>
```

## Status

Sometimes you want to see what has changed.  ```git status``` can be used to see which files have changed since the last commit.  Otherwise, you can use ```git diff``` to more closely inspect file changes line by line


## Pushing

Push a quick commit:

If you created a local branch and need to link it to a remote:

```bash
git push --set-upstream origin <localbranchname>
```


```bash
git add *
git commit -m "commit message"
git push
```

or combined:

```bash
git add * && git commit -m "update" && git push
```

## Submodules

from [here](https://stackoverflow.com/questions/1030169/easy-way-to-pull-latest-of-all-git-submodules)

to pull submodules

```
git submodule update --init --recursive
```

```
git submodule update --recursive --remote
```

cd into the proper subdirectory
ensure you are attached to a branch:

```
git branch
```

if not check one out

```
git checkout [branchname]
```

## clean

```bash
git clean -dxf
```

## feetch all remote tags

```bash
git fetch --all --tags
```

## check out tag to a new branch


```bash
git checkout tags/<tag> -b <branch>
```

example

```bash
git checkout tags/Ubuntu-5.13.0-21.21 -b Ubuntu-5.13.0-21.21
```

## External references

* <https://devconnected.com/how-to-checkout-git-tags/>
