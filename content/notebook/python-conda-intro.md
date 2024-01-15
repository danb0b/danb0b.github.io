---
title: Python / Conda Intro
tags:
- python
- anaconda
- conda
---

## Python

# Python

## Installing

- [Anaconda](https://www.anaconda.com/products/distribution)
- [Packages](https://docs.anaconda.com/anaconda/packages/pkg-docs/)
    - [64-bit Linux](https://docs.anaconda.com/anaconda/packages/py3.10_linux-64/)

## Libraries

- Numpy
- Scipy
- Matplotlib
- Sympy
- Pandas
- Jupyter

## Other Notable Packages

- subprocess
- multiprocessing
- yaml
- opencv
- pytorch
- pyqt
- pyqtgraph
- pyserial

<!--
## Other Packages / Libraries

:::{style="font-size:12pt;"}
:::columns
:::column

- subprocess
- multiprocessing
- argcomplete
- anyqt
- asyncio
- [bokeh](https://docs.bokeh.org/en/latest/)
- yaml / pyyaml
- cudatoolkit
- cudnn
- cvxopt
- cython
- [dask](https://dask.org)
- django
- fftw
- fuel
- geos / shapely
- git
- gitpython
- graphviz
- imageio
- imagesize
- ipython
- jinja
- json5
- jupyter notebook  / [jupyterlab](https://jupyterlab.readthedocs.io/en/stable/)
- matplotlib
- mkl_fft
- [cupy](https://numfocus.org/project/cupy)
- opencv
- paramiko
- pillow
- pip
- plotly
- psutil
- pydot /pydotplus/graphviz/python-graphviz
- pyopengl
- pyqt / qt / qtpy
- pyserial
- pytest
- python-slugify
- pytorch
- pytz
- pywget / wget
- re / regex
- requests & beautifulsoup
- [scikit-image](https://scikit-image.org/) / [scikit-learn](https://scikit-learn.org/stable/)
- setuptools
- sphinx
- spyder
- sympy
- tensorflow
- theano
- [yt](https://yt-project.org/)

<https://docs.anaconda.com/anaconda/packages/py3.10_linux-64/>

-->

## Conda

```bash
conda list
```

## Conda Environments

### Create, List, and Destroy

```bash
conda create --name <env name>
conda info --envs
conda remove --name <env name> --all
```

```bash
conda activate <env name>
conda deactivate
```

```bash
conda activate <env name>
conda env export > environment.yml
```

```bash
conda list -n <env name> -r
conda install --revision <revision-num>
```

```bash
conda activate
conda init --reverse --all
rm -rf ~/anaconda3
rm -rf ~/miniconda3
```

<https://docs.anaconda.com/free/anaconda/install/uninstall/>
<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>

## Conda & ROS

- Historically, the Anaconda distribution does not play nice with ROS.

## Numpy

Great [overview](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html), oriented for MatLab Users converting to Python

## [Scipy](https://scipy.org/)

[Documentation](https://docs.scipy.org/doc/scipy/)
[API](https://docs.scipy.org/doc/scipy/reference/index.html#scipy-api)

## Major Scipy Packages

- [scipy.fft](https://docs.scipy.org/doc/scipy/reference/fft.html)
- [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html)
- [scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/interpolate.html)
- [scipy.linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html)
- [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [scipy.spatial](https://docs.scipy.org/doc/scipy/reference/spatial.html)

## [Matplotlib](https://matplotlib.org/)

- [Plot Types](https://matplotlib.org/stable/plot_types/index)
- [Examples](https://matplotlib.org/stable/gallery/index)
- [Tutorials](https://matplotlib.org/stable/tutorials/index)
- [Full API](https://matplotlib.org/stable/api/index)

## Matplotlib Types

## Pandas

- Better for *structured* array data
- Concept of a ```DataFrame```

:::{style="font-size:12pt;"}

- <https://www.educba.com/what-is-pandas/>
- <https://www.activestate.com/resources/quick-reads/what-is-pandas-in-python-everything-you-need-to-know/>
:::

## Sympy

- Symbolic Representation of

## Visualizaiton

- [Matplotlib](https://matplotlib.org/)
- bokeh
- seaborn
- [pyqtgraph](https://www.pyqtgraph.org/)
- [seaborn](https://seaborn.pydata.org/)
- yt


## Simple Conda Environment Environment

make sure you have already installed

ffmpeg gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly

```bash
conda create -n cv
conda activate cv
conda install -y jupyter matplotlib numpy scipy
conda install -y -c conda-forge opencv
```

```bash
jupyter lab
```

Open and run your code

Delete your environment

```bash
conda remove --name cv --all
```