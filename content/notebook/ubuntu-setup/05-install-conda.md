---
title: 05-Conda Install
weight: 5
tags:
  - anaconda
  - python
  - terminal
  - bash
  - ubuntu
  - linux
  - anaconda
---

## Install Latest Anaconda / Miniconda

| Windows                                                                            | Linux                                                                           |
|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [64-bit Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) | [64-bit Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) |


### Linux Install
```
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

follow the instructions

```
cd ~/
source ~/.bashrc
```

## Windows Install

Set powershell-specific security settings

from <https://stackoverflow.com/questions/47800794/how-to-activate-different-anaconda-environment-from-powershell>

```
Set-ExecutionPolicy remotesigned
conda init powershell
```

Other security options (may break conda script)
```
#Set-ExecutionPolicy AllSigned
```

## Install Packages

Update Conda

```
conda update -y -n base conda
```

### Install full anaconda

If you've installed miniconda only and realize you want the full anaconda pipeline

```
conda install -y anaconda
```

### Conda packages not included in anaconda

```
conda install -y django paramiko pyqtgraph pyopengl gitpython pycairo shapely pycrypto requests[socks]
```

### Install pip packages

```
python -m pip install --upgrade pip
pip install meshio gmsh pygmsh ezdxf twine pandoc-fignos pandoc-eqnos pypdf4 service_identity ftd2xx pygithub paho-mqtt pandoc-crossref scp euclid3 pysolar ntplib pdf2image stem fake_useragent PyMuPDF pygame pysftp pyserial cma ladybug-geometry-polyskel
```

### pandoc citeproc

windows

```
pip install pandoc-citeproc
```

ubuntu

```
sudo apt install -y pandoc-citeproc
```

### Pip packages that need a compiler (optional)

```
pip install spectrum pybullet roslibpy
```


### Update everything to make sure it's all consistent

```
conda update -y --all
```

### map miniconda to anaconda

```
mkdir ~/anaconda3
mkdir ~/anaconda3/bin
ln -s ~/miniconda3/bin/python ~/anaconda3/bin/python
```

## Other Environments

### PyChrono

To install chrono, you must make a different environment, as it conflicts with some of the packages here.

```
sudo apt install libirrlicht-dev

conda create -n chrono
conda activate chrono
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

```
conda install opencv
pip install
#pip install smtplib pygraphviz
```

### CX_freeze

Useful older package for making executables.  Old instructions

go to cx_freeze mod

```
python setup.py install
```

### Older debuggable python

```
conda create -y -n debug python=3.5 spyder=3.1.4
activate debug
conda update conda
conda install -y menuinst
conda install -y  ipykernel=4.8 cython mkl imageio jinja2 jupyter lxml matplotlib networkx numpy pandoc pillow pyflakes pyqt pyyaml ruamel_yaml scipy setuptools sphinx spyder sympy tornado
conda install -y django paramiko pyqtgraph pyopengl gitpython pycairo
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

```
conda create -y -n occ python ipykernel=4.8 matplotlib numpy pyqt pyyaml spyder
activate occ
conda install -y -c conda-forge -c dlr-sc -c pythonocc -c oce pythonocc-core
conda install -y  ipykernel=4.8 matplotlib numpy pyqt pyyaml spyder
conda update -y -n base conda
conda update -y --all
```


### OpenCV install
```
conda create -n opencv python=3.7
conda activate opencv
conda install spyder opencv pyopencv
pip install imutils
```

### Conda packages not available from main channels

```
conda install -c conda-forge scikit-geometry poppler
```

### pychrono

```
conda  install projectchrono/label/develop::pychrono
```

----

## server install

Just for servers, no research code running

```
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