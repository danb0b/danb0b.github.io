---
title: installing gitman on windows
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

```
git bash
which git
cd /mingw64/bin
bash
exec ssh-agent bash
ssh-add -l
ssh-add ~/path/to/your/key

```

## Generate token

Go to github and do that

## Create new user

python envs\gen\Scripts\gitman  -u new --update-config list-github

## External Resources

* <https://github.com/chocolatey-community/chocolatey-packages/blob/master/automatic/git.install/ARGUMENTS.md>
