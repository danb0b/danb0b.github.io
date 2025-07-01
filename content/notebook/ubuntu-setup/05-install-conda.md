---
title: 05-Conda Install
weight: 50
tags:
- anaconda
- python
- terminal
- bash
- ubuntu
- linux
summary: " "
---

## Install Latest Anaconda / Miniconda

| Windows                                                                                      | Linux                                                                                     |
| :------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| [64-bit Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) | [64-bit Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) |

### Linux Install

```bash
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

1. follow the instructions
2. use the default path
3. say "yes" to initialize conda

```bash
cd ~/
source ~/.bashrc
```

### map miniconda to anaconda

```bash
mkdir ~/anaconda3
mkdir ~/anaconda3/bin
ln -s ~/miniconda3/bin/python ~/anaconda3/bin/python
echo "alias python=python3" >> .bashrc
```

## Windows Install

Set powershell-specific security settings

from <https://stackoverflow.com/questions/47800794/how-to-activate-different-anaconda-environment-from-powershell>

```bash
Set-ExecutionPolicy remotesigned
conda init powershell
```

Other security options (may break conda script)

```
#Set-ExecutionPolicy AllSigned
```

## Install Packages

Update Conda

```bash
conda update -y -n base conda
```

### Install full anaconda

If you've installed miniconda only and realize you want the full anaconda pipeline

```bash
conda install -y anaconda
```

### Conda packages not included in anaconda

```bash
conda install -y pyqtgraph pyopengl gitpython pycairo shapely 
conda install -y -c conda-forge scikit-fem vispy
#conda install -y pandoc #the version of pandoc shipped by conda is old.
#conda install -y paramiko pycrypto requests[socks]
```

<!-- conda install -y django -->

### Install pip packages

```bash
python -m pip install --upgrade pip
pip install meshio ezdxf twine pypdf pypdf4 service_identity ftd2xx pygithub paho-mqtt scp euclid3 pysolar ntplib pdf2image stem \
fake_useragent PyMuPDF pygame pysftp pyserial cma ladybug-geometry-polyskel thonny pyexiftool xlsxgrep yt-dlp microdot \
python-slugify \
pandoc-fignos pandoc-eqnos pandoc-crossref h5py
pip install git+https://github.com/pfalcon/utemplate.git
```

<!-- mkdocs mkdocs-material mkdocs-glightbox mkdocs-rss-plugin \ -->

### Fix for pandoc eqnos

```bash
pip3 install --force-reinstall --no-cache-dir git+https://github.com/nandokawka/pandoc-xnos@284474574f51888be75603e7d1df667a0890504d#egg=pandoc-xnos
```

according to [here](https://github.com/tomduck/pandoc-xnos/pull/29), until the PR is merged, do the above.

### gmsh

the pip version of gmsh has issues on ubuntu, so  use apt to install

```bash
#pip install gmsh
pip install pygmsh
```



### pandoc citeproc

windows

```bash
pip install pandoc-citeproc
```

ubuntu

```bash
#deprecated, not available
sudo apt install -y pandoc-citeproc
```

### Pip packages that need a compiler (optional)

```bash
sudo apt install -y build-essential
pip install esptool
#pip install spectrum pybullet roslibpy # not used
```

### Update everything to make sure it's all consistent

```bash
conda update -y --all
```

### Wayland Pyqtgraph / qt5 issue

<https://stackoverflow.com/questions/69994530/qt-qpa-plugin-could-not-find-the-qt-platform-plugin-wayland>

add this to .bashrc

export QT_QPA_PLATFORM="xcb"


## Other Environments

### PyChrono

To install chrono, you must make a different environment, as it conflicts with some of the packages here.

```bash
sudo apt install -y libirrlicht-dev

conda create -n chrono
conda activate chrono
conda install pip
conda install -y -c projectchrono/label/develop pychrono
conda install -y spyder numpy matplotlib scipy
conda install -c dlr-sc pythonocc-core #permits you to use python-occ to generate some geometry
```

Options

```bash
conda install -y -c projectchrono pychrono # to install the stable install
conda install -y -c conda-forge irrlicht # not sure it's needed
```

---------------------

## Older Stuff

### Kivy Development specific packages (optional)

```
#python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
#python -m pip install kivy.deps.gstreamer
```

### Packages required for some of my vision based packages. (opencv downgrades python)

```bash
conda install opencv
pip install
#pip install smtplib pygraphviz
```

### CX_freeze

Useful older package for making executables.  Old instructions

go to cx_freeze mod

```bash
python setup.py install
```

### Older debuggable python

```bash
conda create -y -n debug python=3.5 spyder=3.1.4
activate debug
conda update conda
conda install pip
conda install -y menuinst
conda install -y  ipykernel=4.8 cython mkl imageio jinja2 jupyter lxml matplotlib networkx numpy pandoc pillow pyflakes pyqt pyyaml ruamel_yaml scipy setuptools sphinx spyder sympy tornado
conda install -y paramiko pyqtgraph pyopengl gitpython pycairo
#conda install -y -c conda-forge shapely
conda install -y shapely
conda install -y -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core
python -m pip install --upgrade pip
pip install meshio pygmsh ezdxf twine pypdf4

#python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
#python -m pip install kivy.deps.gstreamer

# go to cx_freeze mod
python setup.py install

conda update -y --all
#stuff required for pydevtools
conda install pycrypto opencv requests pyserial
pip install ntplib pygame pygraphviz pysftp smtplib
```

### PythonOCC

```bash
conda create -y -n occ python ipykernel=4.8 matplotlib numpy pyqt pyyaml spyder
activate occ
conda install pip
conda install -y -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core
conda install -y  ipykernel=4.8 matplotlib numpy pyqt pyyaml spyder
conda update -y -n base conda
conda update -y --all
```

### OpenCV install

```bash
conda create -n opencv python=3.7
conda activate opencv
conda install pip
conda install spyder opencv pyopencv
pip install imutils
```

### Conda packages not available from main channels

```bash
conda install -c conda-forge scikit-geometry poppler
```

### pychrono

```bash
conda  install projectchrono/label/develop::pychrono
```

----

## server install

Just for servers, no research code running

```bash
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
cd ~/
source ~/.bashrc
conda update -y -n base conda
conda install -y pip gitpython requests[socks] pyyaml
python -m pip install --upgrade pip
pip install twine service_identity pygithub scp pysftp


mkdir ~/anaconda3
mkdir ~/anaconda3/bin
ln -s ~/miniconda3/bin/python ~/anaconda3/bin/python


```
