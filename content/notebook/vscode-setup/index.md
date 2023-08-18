---
title: VS Code Setup and Usage
---


## Installation

- Main [Website](https://code.visualstudio.com/)
- Find help [here](https://code.visualstudio.com/docs/setup/linux)
- Download from [here](https://code.visualstudio.com/Download)

```bash
cd ~/Downloads
sudo dpkg -i code_1.7* #.... tab complete
sudo apt install -yf
```

## Useful command-line arguments

```
Usage: code [options][paths...]
```

Example:

```bash
code -n ~/websites/danb0b.github.io/
```

will open a new

```bash
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
|      alt+z      |  switch text wrap mode   |

## Extensions

from [here](https://code.visualstudio.com/docs/editor/command-line)

Slimmed Down:

```bash
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

<!--
### micropython ide (bao phan)

```bash
pip install adafruit-ampy
pip3 install rshell
```
-->

## Markdown all-in-one

go to settings
@id:editor.defaultFormatter @lang:markdown formatter
ctrl_+ shift + I then formats your document

### pymaker

1. install pymakr preview

 ```bash
 code --install-extension Pycom.pymakr-preview
 ```

1. navigate to pymakr tab
   2. list devices
   3. connect device
   4. open device in workspace
5. create project:  ```ctrl+shift+p``` then

## Python

### Debugging

see this [reference](https://codelovingyogi.medium.com/vscode-debugging-python-scripts-with-args-d8ac1cf9a191) to add a debug configuration

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

```bash
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

located in ```~/.config/Code/User/keybindings.json```

recent settings [here](keybindings.json)

## User Settings

located in ```~/.config/Code/User/settings.json```

recent settings [here](settings.json)

## Working with Python

ctrl+shift+p then "python select interpreter"

- <https://code.visualstudio.com/docs/python/python-tutorial>
- <https://www.pythontutorial.net/getting-started/setup-visual-studio-code-for-python/>
- <https://theproductiveengineer.net/how-to-set-up-vs-code-for-python/>
