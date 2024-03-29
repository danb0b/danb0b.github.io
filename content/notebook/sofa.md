---
title: sofa notes
---

## Sofa info

* <https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3>
* <https://github.com/ripl/SofaFramework-Docker>
* <https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu/tags>
* <https://www.sofa-framework.org/community/doc/getting-started/build/linux/>
* <https://github.com/faichele/docker-sofa-dev>
* <https://github.com/sofa-framework/sofa/issues/2485>
* <https://github.com/sofa-framework/doc/tree/master/15_Using_SOFA>
* Latest Release:
    * <https://github.com/sofa-framework/sofa/releases/tag/v23.12.01>

## VBox info

ubuntu 22.04 only:

install guest additions

```bash
sudo usermod -a -G vboxsf $USER 
sudo usermod -a -G vboxusers $USER 
```

```bash
wget https://github.com/sofa-framework/sofa/releases/download/v23.12.01/SOFA_v23.12.01_Linux.zip
unzip SOFA_v23.12.01_Linux.zip
sudo apt update
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt install libpython3.8 python3.8 python3-pip python3.8-distutils 
sudo apt install python3.10-dev python3.10-distutils pybind11-dev
curl -L https://bootstrap.pypa.io/pip/get-pip.py --output /tmp/get-pip3.py
python3.10 /tmp/get-pip3.py
export PATH=$PATH:$HOME/.local/bin
python3.10 -m pip install --upgrade pip
python3.10 -m pip install numpy scipy pybind11==2.9.1

#https://stackoverflow.com/questions/77233855/why-did-i-got-an-error-modulenotfounderror-no-module-named-distutils
sudo apt install libopengl0
# sudo apt remove python3-pil
python3.10 -m pip install numpy scipy jupyter matplotlib pillow
```

add to bashrc

```bash
export PATH=$HOME/.local/bin:$PATH

export SOFA_ROOT=$HOME/SOFA_v23.12.01_Linux
export PYTHONPATH=$PYTHONPATH:$HOME/SOFA_v23.12.01_Linux/plugins/SofaPython3/lib/python3/site-packages
export PATH=$HOME/SOFA_v23.12.01_Linux/bin:$PATH
```
```bash
nano $HOME/SOFA_v23.12.01_Linux/lib/plugin_list.conf
```

add


```bash
#SofaPython3 23.06.00 # for older version
SofaPython3 23.12.01
```

remove:

```bash
MeshSTEPLoader NO_VERSION
```

## Example

git clone https://github.com/SofaDefrost/SoftRobots.git

runSofa SoftRobots/examples/tutorials/PneunetGripper/details/step7-grabTheCube.py 



## Coding

* <https://sofapython3.readthedocs.io/en/latest/content/FirstSteps.html>
* <https://sofapython3.readthedocs.io/en/latest/content/CustomModule.html>

## GL issues

# not needed
apt install ffmpeg libsm6 libxext6  -y #<https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo>

# all that's needed
apt install libgl1 #<https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo>
apt-get install libnss3 #<https://stackoverflow.com/questions/72149564/pyqt5-doesnt-work-on-docker-importerror-libsmime3-so-cannot-open-shared-objec>

tried, not sure if it worked
pip install pyoplengl
didn't try
apt install libgl1-mesa-glx

got through that now not finding other things

apt install make g++ pkg-config libgl1-mesa-dev libxcb*-dev libfontconfig1-dev libxkbcommon-x11-dev python libgtk-3-dev #<https://stackoverflow.com/questions/62391587/qt-could-not-find-the-qt-platform-plugin-xcb>

<https://wiki.qt.io/Install_Qt_5_on_Ubuntu>

pip install pyqt5

## Tutorials

<https://softroboticstoolkit.com/book/export/html/882561>
<https://project.inria.fr/softrobot/install-get-started-2/tutorial/>
<https://github.com/SofaDefrost/SoftRobots/tree/master/examples/tutorials/Trunk/mesh>

## problem with plugins

<https://github.com/sofa-framework/sofa/releases/tag/v23.06.00>

<https://www.sofa-framework.org/community/doc/plugins/what-is-a-plugin/#plugin-loading>

```
[ERROR]   [PluginManager] Plugin loading failed (/home/danaukes/sofa/SOFA_v23.12.01_Linux/lib/libMeshSTEPLoader.so): libTKBRep.so.11: cannot open shared object file: No such file or directory
```

* <https://github.com/sofa-framework/sofa/discussions/4090>
* <https://github.com/sofa-framework/sofa/discussions/3415>
* <https://github.com/SofaDefrost/STLIB>
* <https://project.inria.fr/softrobot/install-get-started-2/download/>

