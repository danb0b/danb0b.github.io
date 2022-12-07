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

| Key Combination | Description              |
|:---------------:|:------------------------ |
|  ctrl+shift+p   | opens the command window |
|  ctrl+shift+e   | opens explorer           |
|  ctrl+shift+x   | opens extensions         |
|  ctrl+shift+g   | opens git                |
|  ctrl+shift+f   | opens search             |


##  Extensions

from [here](https://code.visualstudio.com/docs/editor/command-line)

Slimmed Down:

```
code --install-extension redhat.vscode-yaml
code --install-extension yzane.markdown-pdf
code --install-extension yzhang.markdown-all-in-one
code --install-extension bierner.markdown-yaml-preamble
code --install-extension Pycom.pymakr-preview
code --install-extension ms-python.python
```

```bash
code --list-extensions
```

## Plugins

###  micropython ide (bao phan)

```bash
pip install adafruit-ampy
pip3 install rshell
```

### pymaker 


1. install pymakr preview

	```
	code --install-extension Pycom.pymakr-preview
	```

1. navigate to pymakr tab
	1. list devices
	2. connect device
	3. open device in workspace
2. create project:  ```ctrl+shift+p``` then 

#### External Resources

1. <https://github.com/pycom/pymakr-vsc/blob/HEAD/GET_STARTED.md>
2. <https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr>

Other:
https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/
https://lemariva.com/blog/2018/12/micropython-visual-studio-code-as-ide
https://lemariva.com/blog/2018/12/micropython-visual-studio-code-as-ide
https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/vscode-setup.html
https://stackoverflow.com/questions/67647095/how-to-setup-windows-10-vscode-pymakr-for-python-programming-micropython



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