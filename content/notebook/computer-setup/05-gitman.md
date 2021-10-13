---
title: install gitman
weight: 5
---

Gitman is my python based package for scanning a computer and pulling all your repositories off.  If you haven't ever set up gitman before, run it once to create a blank config file, located in ~/.config/gitman/config.yaml

1. Restore From a backup

    ```bash
    mkdir ~/.config
    mkdir ~/.config/gitman
    gpg --output ~/.config/gitman/config.yaml --decrypt ~/my/remote/filesystem/backup_settings/config.yaml.gpg
    ```
    
1. [Install miniconda](/notebook/conda_install/)

1. Install gitman and clone all files 

    ```bash
    mkdir ~/code
    cd ~/code
    git clone git@danb0b.github.com:danb0b/code_git_tools.git
    echo "export PYTHONPATH=\$PYTHONPATH:$(realpath ~)/code/code_git_tools/python" >> ~/.bashrc
    echo "export PATH=\$PATH:$(realpath ~)/code/code_git_tools/python/git_manage" >> ~/.bashrc
    sudo chmod +x ~/code/code_git_tools/python/git_manage/gitman
    source ~/.bashrc
    gitman clone
    ```
