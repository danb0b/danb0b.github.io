---
title: Gitman repository manager
icon: bi bi-github
tags:
- python
- git
summary: ""
---

A nice little package for synchronizing git repositories all over your computer

Package URL: <https://github.com/danb0b/code_git_tools>

Common commands

## Index

Create an up-to-date list of all external repositories to cut down on scanning the hard drive

```bash
gitman index
```

## List Repositories

List all the external repositories currently in the index

```bash
gitman list
```

## Clone

Clone all external repositories not listed in your ignore list in config

```bash
gitman clone
```

## Pull

Pull all non-dormant local repositories

```bash
gitman pull
```

## Status

List all the repositories that do not match with their head

```bash
gitman status
```

## Branch Status

List branches that are currently local but not remote, remote but not local, etc

```bash
gitman branch-status
```

## Reset

Reset all branches to head unless they have local unsaved changes

```bash
gitman reset
```

