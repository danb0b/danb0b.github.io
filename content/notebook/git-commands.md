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

delete local git branch 

```bash
git branch -d <local name>
```

delete remote branch

```bash
git push origin --delete <remote/branch-name>
```

## Status

Sometimes you want to see what has changed.  ```git status``` can be used to see which files have changed since the last commit.  Otherwise, you can use ```git diff``` to more closely inspect file changes line by line

```bash
git status
```

```bash
git diff
```

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

## log

```bash
git log
```

use this to find the commit hash for prior commits.  you can use this to reset

## reset

reset to head

```bash
git reset
```

reset to specific commit

```bash
git reset <hash>
```

reset index to head and reset files

```bash
git reset --hard
```

## clean

interactive clean

```bash
git clean -i
```

force the removal of all untracked files

```bash
git clean -dxf
```
## restore

```bash
git restore <path/to/file>
```

restore all files of the type ```.c```

```bash
git restore '*.c'
```


## Submodules

create

```
git submodule add <repo_address> <your/local/path>
```

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

## ignore

echo "docs/lectures/lecture.html" >> .gitignore

## External references

* <https://devconnected.com/how-to-checkout-git-tags/>

## Remove files from git tree without deleting

<https://stackoverflow.com/questions/1143796/remove-a-file-from-a-git-repository-without-deleting-it-from-the-local-filesyste>

```bash
git rm --cached path/to/the/file
```


## Stash changes

from [here](https://www.freecodecamp.org/news/git-stash-commands/)

```bash
git stash

git stash --include-untracked

git stash pop
```

## git merge

```bash
git checkout master
git merge featureBranch
```
