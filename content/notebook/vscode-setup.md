---
title: VS Code Setup and Usage
---

## Installation

Find help [here](https://code.visualstudio.com/docs/setup/linux)

Download from [here](https://code.visualstudio.com/Download)

```bash
cd ~/Downloads
sudo dpkg -i code_1.7 #.... tab complete
sudo apt install -yf
```

## Useful command-line arguments

```
Usage: code [options][paths...]
```

Example:

```
code -n ~/websites/danb0b.github.io/
```

will open a new

```
  -a --add <folder>      Add folder(s) to the last active window.
  -n --new-window        Force to open a new window.
  -r --reuse-window      Force to open a file or folder in an already opened window.
  --extensions-dir <dir> Set the root path for extensions.
  --list-extensions      List the installed extensions.
  --show-versions        Show versions of installed extensions, when using --list-extensions.
  --install-extension <ext-id | path> Installs or updates an extension. 
  --uninstall-extension <ext-id>      Uninstalls an extension.
  --enable-proposed-api <ext-id>      Enables proposed API features for
  --disable-extensions            Disable all installed extensions.
  --disable-extension <ext-id>    Disable an extension.
  --sync <on | off>               Turn sync on or off.
```

## Shortcuts

| Key Combination |       Description        |
| :-------------: | :----------------------: |
|  ctrl+shift+p   | opens the command window |
|  ctrl+shift+e   |      opens explorer      |
|  ctrl+shift+x   |     opens extensions     |
|  ctrl+shift+g   |        opens git         |
|  ctrl+shift+f   |       opens search       |
|  ctrl+shift+k   |       remove line        |
|  ctrl+shift+/   |      comment line:       |
|     ctrl+up     |       move line up       |
|    ctrl+down    |      move line down      |
|    ctrl+k,v     |         preview          |
|  ctrl+shift+i   |     format document      |
|     ctrl+i      |   italicize selection    |
|     ctrl+b      |      bold selection      |

## Extensions

from [here](https://code.visualstudio.com/docs/editor/command-line)

Slimmed Down:

```
code --install-extension redhat.vscode-yaml
code --install-extension yzane.markdown-pdf
code --install-extension yzhang.markdown-all-in-one
code --install-extension bierner.markdown-yaml-preamble
code --install-extension Pycom.pymakr-preview
code --install-extension ms-python.python
code --install-extension shd101wyy.markdown-preview-enhanced
#code --install-extension darkriszty.markdown-table-prettify #doesn't work without npm
#code --install-extension esbenp.prettier-vscode # markdown allinone formats just fine.
code --install-extension davidanson.vscode-markdownlint #highlight file problems
```

```bash
code --list-extensions
```

## Plugins

### micropython ide (bao phan)

```bash
pip install adafruit-ampy
pip3 install rshell
```

## Markdown all-in-one

go to settings
@id:editor.defaultFormatter @lang:markdown formatter
ctrl_+ shift + I then formats your document

### pymaker

1. install pymakr preview

 ```
 code --install-extension Pycom.pymakr-preview
 ```

1. navigate to pymakr tab
   2. list devices
   3. connect device
   4. open device in workspace
5. create project:  ```ctrl+shift+p``` then

#### External Resources

1. <https://github.com/pycom/pymakr-vsc/blob/HEAD/GET_STARTED.md>
2. <https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr>

Other:
<https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/>
<https://lemariva.com/blog/2018/12/micropython-visual-studio-code-as-ide>
<https://lemariva.com/blog/2018/12/micropython-visual-studio-code-as-ide>
<https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/vscode-setup.html>
<https://stackoverflow.com/questions/67647095/how-to-setup-windows-10-vscode-pymakr-for-python-programming-micropython>

## Interesting Packages

- general
  - python
  - python extension pack
  - jupyter
  - html css
  - c/c++ extension pack
- yaml
- markdown
  - markdown all in one
  - mardkown preview ehnanced
  - markdown pdf
  - markdown lint
  - markdown yaml preamble
- vscode pandoc
- git
  - git history
  - gitlens
  - git graph
- esp32 / micropython
  - micropython ide (bao phan)
  - espressif idf

after installing the above:

```
batisteo.vscode-django
bierner.markdown-yaml-preamble
DavidAnson.vscode-markdownlint
donjayamanne.githistory
donjayamanne.python-environment-manager
donjayamanne.python-extension-pack
DougFinke.vscode-pandoc
dphans.micropython-ide-vscode
eamodio.gitlens
ecmel.vscode-html-css
espressif.esp-idf-extension
KevinRose.vsc-python-indent
mhutchie.git-graph
ms-python.isort
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode.cmake-tools
ms-vscode.cpptools
ms-vscode.cpptools-extension-pack
ms-vscode.cpptools-themes
njpwerner.autodocstring
Pycom.pymakr
redhat.vscode-yaml
shd101wyy.markdown-preview-enhanced
twxs.cmake
VisualStudioExptTeam.intellicode-api-usage-examples
VisualStudioExptTeam.vscodeintellicode
wholroyd.jinja
yzane.markdown-pdf
yzhang.markdown-all-in-one
```


## Keybindings

```json
[
    {
        "key": "ctrl+down",
        "command": "editor.action.moveLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "alt+down",
        "command": "-editor.action.moveLinesDownAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+up",
        "command": "editor.action.moveLinesUpAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "alt+up",
        "command": "-editor.action.moveLinesUpAction",
        "when": "editorTextFocus && !editorReadonly"
    },
    {
        "key": "ctrl+2",
        "command": "markdown.extension.editing.toggleList"
    },
    {
        "key": "ctrl+d",
        "command": "editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "key": "ctrl+shift+k",
        "command": "-editor.action.deleteLines",
        "when": "textInputFocus && !editorReadonly"
    },
    {
        "key": "ctrl+alt+i",
        "command": "markdownlint.fixAll"
    }
]
```


## User Settings

> I removed unused pymakr devices for brevity

```json
{
    "workbench.colorTheme": "Default Dark+",
    "git.confirmSync": false,
    "pymakr.devices.configs": {
        "serial:///dev/ttyUSB0": {
            "autoConnect": "onLostConnection",
            "name": "",
            "username": "micro",
            "password": "python",
            "hidden": false,
            "rootPath": null,
            "adapterOptions": {}
        }
    },
    "security.workspace.trust.untrustedFiles": "open",
    "[markdown]": {
        "editor.defaultFormatter": "yzhang.markdown-all-in-one"
    },
    "explorer.confirmDragAndDrop": false,
    "pymakr.misc.notifications": {
        "Uploading a project will delete all existing files on the device before uploading the project folder. After uploading a project, you can start it by restarting the device. For faster uploads without file deletion, please put the device in dev mode.": "Don't show again"
    },
    "editor.fontSize": 12,
    "markdownlint.config": {
        "default": true,
        "MD007": { "indent": 4 }
    },
    "markdown.extension.orderedList.autoRenumber": false,
    "markdown.extension.list.indentationSize": "inherit"
}
```