---
title: Conda Install
tags:
  - anaconda
  - python
  - terminal
  - bash
---

## Install Latest Anaconda / Miniconda

| Windows                                                                            | Linux                                                                           |
|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [64-bit Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) | [64-bit Miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) |


### Linux script
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

## Set powershell-specific security settings

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

<!--
## Full Script

```
conda update -y -n base conda
conda install -y anaconda
conda install -y django paramiko pyqtgraph pyopengl gitpython pycairo shapely pycrypto requests[socks]
conda install -c conda-forge scikit-geometry poppler
python -m pip install --upgrade pip
pip install meshio pygmsh ezdxf pandoc-fignos pandoc-eqnos pypdf4 service_identity ftd2xx pygithub twine paho-mqtt pandoc-crossref scp euclid3 pysolar pdf2image stem fake_useragent PyMuPDF ntplib pygame pysftp pyserial
pip install spectrum pybullet roslibpy
conda update -y --all
```
-->

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

### Pychrono Install

```
conda create -n chrono
conda activate chono
#conda install -c projectchrono pychrono
conda install numpy matplotlib spyder
conda install -c projectchrono/label/develop pychrono
conda install -c dlr-sc pythonocc-core
conda install spyder
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
