---
title: Install and Configure Atom
---

1. Install

    ```bash
    wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
    sudo sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
    sudo apt-get update
    sudo apt-get install -y atom
    apm install language-markdown markdown-preview-plus markdown-table-formatter wordcount
    # should already have texlive-full installed...
    sudo apt install latexmk
    apm install language-latex latex pdf-view
    ```

1. Load custom configuration file

    ```bash
    cp -r /my/remote/filesystem/atom/ ~/.config/
    ```