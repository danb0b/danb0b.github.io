---
title: Git Commands
tags:
  - bash
  - git
  - github
weight: 10
summary: a handy cheatsheet of my most used and looked up git commands
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

```bash
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
#or
git push -d <remote> <remote branch name>
```

check out all remote branches to a local branch:

```bash
for remote in `git branch -r | grep -v /HEAD`; do git checkout --track $remote ; done
```

from [here](https://stackoverflow.com/questions/379081/track-all-remote-git-branches-as-local-branches)

## Status

Sometimes you want to see what has changed.  ```git status``` can be used to see which files have changed since the last commit.  Otherwise, you can use ```git diff``` to more closely inspect file changes line by line

```bash
git status
```

```bash
git diff
```

```bash
git diff --color=always <commit hash> | less -r
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

```bash
git submodule add <repo_address> <your/local/path>
```

from [here](https://stackoverflow.com/questions/1030169/easy-way-to-pull-latest-of-all-git-submodules)

to pull submodules

```bash
git submodule update --init --recursive
```

```bash
git submodule update --recursive --remote
```

cd into the proper subdirectory
ensure you are attached to a branch:

```bash
git branch
```

if not check one out

```bash
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

## pull and merge upstream changes into forked branch

```bash
git clone path/to/my_repo.git
cd my_repo
git remote add upstream path/to/upstream_repo.git
git fetch upstream

git pull upstream master
or
git rebase upstream/master

git push --force
git push origin main
```

from [here](https://stackoverflow.com/questions/40983514/most-efficient-way-to-keep-a-fork-up-to-date) and [here](https://www.digitalocean.com/community/questions/how-to-keep-your-forked-github-repository-up-to-date)

## Adding a second remote

```bash
git remote add <name-of-new-remote> https://github.com/OWNER/REPOSITORY.git
git remote -v
git push <name-of-new-remote> <branch>
```

<https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories>

```bash
git push --set-upstream <name-of-new-remote> <branch>
git branch --track <name-of-new-remote> <branch>
```

### push all branches and tags from one remote to another

assuming your original remote is called "origin"

```bash
git push <name-of-new-remote> --tags "refs/remotes/origin/*:refs/heads/*"
```

<https://stackoverflow.com/questions/37884832/git-push-all-branches-from-one-remote-to-another-remote>

## Gitignore

To check what gitignore rule is causing a particular path to be ignored, run git check-ignore:

```bash
git check-ignore -v path/to/check
```

from [here](https://stackoverflow.com/questions/49638204/the-following-paths-are-ignored-by-one-of-your-gitignore-files)

## Merge Unrelated branches

<https://stackoverflow.com/questions/1425892/how-do-you-merge-two-git-repositories>

```bash
cd path/to/project-a
git filter-repo --to-subdirectory-filter project-a

cd path/to/project-b
git remote add project-a /path/to/project-a
git fetch project-a --tags
git merge --allow-unrelated-histories project-a/master # or any branch you want to merge
git remote remove project-a
```

## merge with squash

```bash
git merge --squash <tag or branch>
```

for example

```bash
git merge --squash wip
```

## Environments with multiple users

if you're sharing the same login and want to ensure you each commit changes, you can use

```bash
git -c user.name="User Name" -c user.email="<email@address.com>" commit -m "my commit message"
```

Example

```bash
git -c user.name="Dan Aukes" -c user.email="danaukes@danaukes.com" commit -m "made a change"
```

also if you want to use a one-time identity,

```bash
git -c core.sshCommand="ssh -i <path-to-key>" push --force
```

from: 

* <https://stackoverflow.com/questions/11579311/git-commit-as-different-user-without-email-or-only-email>
* <https:/stackoverflow.com/questions/7927750/>
