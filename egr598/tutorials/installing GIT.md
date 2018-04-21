---
title: Installing git
class_logo: "../graphics/ClassLogo.pdf"
university_logo: "../graphics/UniversityLogo.pdf"
---

# In Windows
1. download and install [git extensions](https://github.com/gitextensions/gitextensions/releases).
    * Recent Release [2.48.05](https://github.com/gitextensions/gitextensions/releases/download/v2.48.05/GitExtensions-2.48.05-SetupComplete.msi)
    * install for all users
    * select all sub-programs to install(kdiff, msysgit, and windows credential store).
    * keep putty as default.
    * Other programs will then install.
    * In the git install when it asks about shell integration, select the option which allows git commands and unix commands from the cmd shell.
    * Keep all other options default
    * select a language(english)
    * set your username and password in the git extensions settings window that pops up

# In Ubuntu

1. Open up a terminal window (ctrl+alt+t)
1. Paste the following code(substituting in your name and email) to install git.

```sudo apt-get update
sudo apt-get install -y git
git config --global user.name "LastName, Firstname"
git config --global user.email "email@address.com"
```
