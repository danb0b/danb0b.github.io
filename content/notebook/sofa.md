## Sofa info

https://sofapython3.readthedocs.io/en/latest/content/Installation.html#using-python3
https://github.com/ripl/SofaFramework-Docker
https://hub.docker.com/r/sofaframework/sofabuilder_ubuntu/tags
https://www.sofa-framework.org/community/doc/getting-started/build/linux/
https://github.com/faichele/docker-sofa-dev
https://github.com/sofa-framework/sofa/issues/2485
https://github.com/sofa-framework/doc/tree/master/15_Using_SOFA



## VBox info

ubuntu 22.04 only:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install libpython3.8 python3.8 python3-pip python3.8-distutils #https://stackoverflow.com/questions/77233855/why-did-i-got-an-error-modulenotfounderror-no-module-named-distutils
sudo apt remove python3-pil
python3.8 -m pip install numpy scipy jupyter matplotlib pillow
sudo apt install libopengl0
add to bashrc
export PATH=/home/danaukes/.local/bin:$PATH

export SOFA_ROOT=/home/danaukes/sofa/SOFA_v23.06.00_Linux
export PYTHONPATH=$PYTHONPATH:/home/danaukes/sofa/SOFA_v23.06.00_Linux/plugins/SofaPython3/lib/python3/site-packages
export PATH=/home/danaukes/sofa/SOFA_v23.06.00_Linux/bin:$PATH

     
sudo usermod -a -G vboxsf $USER 
sudo usermod -a -G vboxusers $USER 

```




## Docker info

https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f
https://medium.com/@18bhavyasharma/setting-up-and-running-jupyter-notebook-in-a-docker-container-d2acd713ce66
https://www.dataquest.io/blog/docker-data-science/
https://towardsdev.com/run-a-jupyter-notebook-in-a-docker-container-on-your-local-device-80ccd9570e4f

## Jupyter setup and security

https://jupyter-server.readthedocs.io/en/latest/operators/security.html#
https://jupyter-server.readthedocs.io/en/latest/users/configuration.html\


## Coding


* <https://sofapython3.readthedocs.io/en/latest/content/FirstSteps.html>
* <https://sofapython3.readthedocs.io/en/latest/content/CustomModule.html>

## GL issues

#not needed
apt install ffmpeg libsm6 libxext6  -y #https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo

#all that's needed
apt install libgl1 #https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo
apt-get install libnss3 #https://stackoverflow.com/questions/72149564/pyqt5-doesnt-work-on-docker-importerror-libsmime3-so-cannot-open-shared-objec

tried, not sure if it worked
pip install pyoplengl
didn't try
apt install libgl1-mesa-glx


got through that now not finding other things

apt install make g++ pkg-config libgl1-mesa-dev libxcb*-dev libfontconfig1-dev libxkbcommon-x11-dev python libgtk-3-dev #https://stackoverflow.com/questions/62391587/qt-could-not-find-the-qt-platform-plugin-xcb

https://wiki.qt.io/Install_Qt_5_on_Ubuntu


pip install pyqt5

