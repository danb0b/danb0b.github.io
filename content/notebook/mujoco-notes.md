---
title: Mujoco / Conda Usage notes
---

## Conda-based installation

If you've got conda, you should use conda packages, otherwise the render engine will not see your system graphics libraries, even if you install them.

```python
#conda create --name mujoco_env
conda create -n mujoco_env python=3.9
conda activate mujoco_env
# cannot install jupyter, but you can install jupyter lab, according to this: <https://stackoverflow.com/questions/50675004/conflicting-python-version-in-jupyter-notebookconda>
conda install jupyterlab
conda install -c conda-forge glew
conda install -c conda-forge mesalib
conda install -c anaconda mesa-libgl-cos6-x86_64
conda install -c menpo glfw3
pip install mujoco
pip install mediapy
```

```python
conda env config vars set MUJOCO_GL=egl PYOPENGL_PLATFORM=egl
conda deactivate && conda activate mujoco_env
```

```python
conda env config vars set MUJOCO_GL=asdf PYOPENGL_PLATFORM=asdf
conda deactivate && conda activate mujoco_env
```

```python
conda env config vars set MUJOCO_GL=asdf PYOPENGL_PLATFORM=asdf
conda deactivate && conda activate mujoco_env
```


```python
conda deactivate
conda remove --name mujoco_env --all
```
### Resources

* <https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>


## External Resources

* Pytorch [instructions](https://pytorch.org/rl/reference/generated/knowledge_base/MUJOCO_INSTALLATION.html) for installing mujoco **(extremely helpful**)
* [Github repository](https://github.com/deepmind/mujoco)
* [Binary Releases](https://github.com/deepmind/mujoco/releases)
* [Documentation](https://mujoco.readthedocs.io/)
* Mujoco interactive [tutorial](https://colab.research.google.com/github/deepmind/mujoco/blob/main/python/tutorial.ipynb)

--------------------

## Old Information, disregard

This information is for a traditional python installation, which I did not have.  So it's old / bad information.

## Install

If you have conda installed, you shouldn't install these packages, as conda will be looking for libraries installed in conda

```python
pip install mujoco mediapy
sudo apt install -y libglfw3 libglew2.2 libgl1-mesa-glx libosmesa6
sudo apt install -y libegl-dev libegl1 libegl1-mesa libegl1-mesa-dev
sudo apt install libosmesa6-dev
sudo apt-get install libglew-dev libglew2.2
```

## OSMESA

again, this is a hack for compensating for the libraries loaded on your system instead of conda

<https://stackoverflow.com/questions/58424974/anaconda-importerror-usr-lib64-libstdc-so-6-version-glibcxx-3-4-21-not-fo>

export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so.2.2:/usr/lib/x86_64-linux-gnu/libGL.so.1:/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.30

## Issue with GLFW

> FatalError: an OpenGL platform library has not been loaded into this process, this most likely means that a valid OpenGL context has not been created before mjr_makeContext was called

<https://github.com/openai/mujoco-py/issues/187#issuecomment-384905400>

sudo apt install -y libglfw3 libglew2.0 libgl1-mesa-glx libosmesa6
conda install -c conda-forge glew
conda install -c conda-forge mesalib
conda install -c anaconda mesa-libgl-cos6-x86_64
conda install -c menpo glfw3

* <https://pytorch.org/rl/reference/generated/knowledge_base/MUJOCO_INSTALLATION.html>

