---
title: installing gitman on windows
summary: " "
---

Support for multiple github accounts
 
## install choco

Set-ExecutionPolicy AllSigned
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

## Install Git

choco install -y git.install --params "/NoShellIntegration /NoCredentialManager /GitAndUnixToolsOnPath"
choco install -y gitextensions

choco install -y kdiff3
choco install -y notepadplusplus
    
python -m venv $HOME/envs/gen

## Install git management tool

envs/gen/scripts/activate

pip install git_manage

## get config file

### generate keys

### Add keys to github acct

### Steps to get git to recognize github ssh keys

open git bash

```
which git
cd /mingw64/bin
bash
exec ssh-agent bash
ssh-add -l
ssh-add ~/path/to/your/key

```

## add a .ssh/config file

you need to configure your ssh client to apply keys associated with different github users.


## Generate token

Go to github and do that:

<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>

## Create new user

python envs\gen\Scripts\gitman  -u new --update-config list-github

## External Resources

* <https://github.com/chocolatey-community/chocolatey-packages/blob/master/automatic/git.install/ARGUMENTS.md>
* <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>
