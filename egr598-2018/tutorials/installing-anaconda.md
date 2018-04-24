---
title: Installing Anaconda
subtitle: for foldable robotics topics
class_name: EGR598:Foldable Robotics
---

## Simple Installation

### Windows Installation

#### Optional Prerequisites
1. Install Virtualbox
1. Download Windows from [dreamspark](https://webapp4.asu.edu/eacademy-sso/authn)

#### Required Steps

1. Download and install [Miniconda](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe)
    * install for all users (if possible).
    * install in the c: directory, as in c:/Miniconda3/ or likewise
    * keep all other defaults
1. Add Anaconda to the system path    
    1. go to file explorer
    1. right click on my computer
    1. on the left menu sele advanced system settings
    1. click on environment variables
    1. in the lower window, find the path variable, and click edit
    1. (in windows 10), click edit text
    1. Go to the *end* of the string, and paste in the following(with "Miniconda3" replaced by the root folder for your miniconda / anaconda installation).  **Important:** Make sure there are semicolons between each path.  Do not replace any other items in the path.  
    ```
    C:\Miniconda3;C:\Miniconda3\Scripts;C:\Miniconda3\Library\bin;
    ```

1. Install packages:
    * open up cmd *in administrator mode*, and paste the following code(line by line):

```
conda update conda
conda install setuptools cython pyyaml numpy scipy spyder sympy
conda install pyopengl pyqt pyqtgraph matplotlib jupyter pillow lxml
conda install -c conda-forge shapely
pip install ezdxf imageio meshio 
pip install pypoly2tri idealab_tools foldable_robotics pynamics
```

### Ubuntu Installation

#### Install Anaconda
1. Open a terminal window(ctrl+alt+T)
1. Paste the following code(line by line)

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
echo "export PATH="$HOME/miniconda/bin:$PATH"" >> ~/.bashrc
conda update conda
conda install setuptools cython pyyaml numpy scipy spyder sympy
conda install pyopengl pyqt pyqtgraph matplotlib jupyter pillow lxml
conda install -c conda-forge shapely
pip install ezdxf imageio meshio 
pip install pypoly2tri idealab_tools foldable_robotics pynamics
```

## Advanced: Creating a custom environment

An environment is a nice way to sandbox your install from perhaps other python projects which need different, conflicting packages.  If you want more control over your installation, do this instead of the default way of installing packages in your root installation.  [Learn More](http://conda.pydata.org/docs/using/envs.html).

### Windows

1. Open up cmd *in administrator mode*, and paste the following code(line by line):

```
conda create -n myenvironmentname
activate myenvironmentname
conda update conda
conda install setuptools cython pyyaml numpy scipy spyder sympy
conda install pyopengl pyqt pyqtgraph matplotlib jupyter pillow lxml
conda install -c conda-forge shapely
pip install ezdxf imageio meshio 
pip install pypoly2tri idealab_tools foldable_robotics pynamics
```

### Ubuntu

```
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
echo "export PATH="$HOME/miniconda/bin:$PATH"" >> ~/.bashrc
conda update conda
conda install setuptools cython pyyaml numpy scipy spyder sympy
conda install pyopengl pyqt pyqtgraph matplotlib jupyter pillow lxml
conda install -c conda-forge shapely
pip install ezdxf imageio meshio 
pip install pypoly2tri idealab_tools foldable_robotics pynamics
```

### Using your custom environment

To activate your environment you have to type

```
activate myenvironmentname
```

or, in Ubuntu,

```
source activate myenvironmentname
```

to use this environment.

Now you are Ready to open either spyder or jupyter, two good environments, to start coding!

## References
* [Managing Conda Environments](https://conda.io/docs/user-guide/tasks/manage-environments.html)
