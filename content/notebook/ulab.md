---
title: Compliling uLab for micropython
---

```bash
sudo apt update && sudo apt install \
python3 \
git \
python3-pip \
python3-virtualenv \
python3-venv

sudo apt install \
wget \
flex \
bison \
gperf \
cmake

# libusb-1.0-0
# dfu-util \
# libssl-dev \
# libffi-dev \
# ccache \
# ninja-build \

git clone https://github.com/v923z/micropython-ulab.git ulab && \
git clone https://github.com/micropython/micropython.git
export BUILD_DIR=$(pwd)
cd $BUILD_DIR/micropython/

#git clone -b v4.0.2 --recursive https://github.com/espressif/esp-idf.git# bad info
git clone -b v5.3.1 --recursive https://github.com/espressif/esp-idf.git

cd $BUILD_DIR/micropython/esp-idf

./install.sh esp32
. ./export.sh
which idf.py

cd $BUILD_DIR/micropython/ports/esp32

./install.sh
. ./export.sh
./install.sh
./install.sh
cd $BUILD_DIR/micropython/
cd esp-idf
./install.sh
cat install.sh
python
which python
alias python=python3
./install.sh
which python3
ln --help
echo $PATH
which python3
ln -s /usr/bin/python3 /usr/bin/python
./install.sh 
cat .bash_history
history -a
./install.sh 
./install.sh 
. ./export.sh
cd $BUILD_DIR/micropython/mpy-cross
make
cat ~/.bash_history 
cd $BUILD_DIR/micropython/ports/esp32
make submodules

cd $BUILD_DIR/micropython/ports/esp32
cat << EOT | tee makefile
BOARD = ESP32_GENERIC
USER_C_MODULES = $(BUILD_DIR)/ulab/code/micropython.cmake

include Makefile
EOT

cat Makefile 
make
apt install nano
mv Makefile makefile
git restore Makefile
make
nano makefile
make
cd ../../
cd esp-idf/
./install.sh 
. ./export.sh
cd $BUILD_DIR/micropython/ports/esp32
make
cat make
cat makefile
cat Makefile
grep idf.py Makefile 
ls
getenv
cd ../../
find . -iname idf.py
cd $BUILD_DIR/micropython/ports/esp32
make submodules
cd $BUILD_DIR/micropython/ports/esp32
make .
make
cmake .
ccmake .
make .
apt install cmake
make 
cmake 
cmake ./
cd
cd /micropython/esp-idf/
./install.sh esp32
which idf.py
cd $BUILD_DIR/micropython/ports/esp32
make
cmake 
cmake .
cat CMakeLists.txt 
nano CMakeLists.txt 
clear
make
cmake .
nano CMakeLists.txt 
make
git reset --hard
cat << EOT | tee makefile
BOARD = GENERIC
USER_C_MODULES = $(BUILD_DIR)/ulab/code/micropython.cmake

include Makefile
EOT

make
nano makefile 
make
apt install ninja
apt install python-ninja
apt install python3-ninja
cmake .
history -a
```

* <https://duckduckgo.com/?t=ffab&q=micropython+ulab+&ia=web>
* <https://github.com/v923z/micropython-ulab>
* <https://www.danaukes.com/notebook/micropython-on-linux/>
* <https://duckduckgo.com/?q=python+no+such+file+or+directory+docker&t=ffab&ia=web>
* <https://stackoverflow.com/questions/36022051/docker-no-such-file-or-directory>
* <https://www.pythonpool.com/resolving-usr-bin-env-python-no-such-file-or-directory-error/>
* <https://duckduckgo.com/?q=docker+save+current+terminal%27s+history&t=ffab&ia=web>
* <https://samialperenakgun.com/blog/2022/04/save-docker-bash-history/>
* <https://duckduckgo.com/?q=ulab+bin%2Fsh%3A+1%3A+idf.py%3A+not+found&t=ffab&ia=web>
* <https://esp32.com/viewtopic.php?t=23020>
* <https://github.com/micropython/micropython/wiki/Build-Troubleshooting>
* <https://duckduckgo.com/?t=ffab&q=install++xtensa-esp32-elf-gcc&ia=web>
* <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html>
* <https://github.com/espressif/esp-iot-solution/issues/309>
* <https://github.com/espressif/esp-iot-solution/blob/master/examples/common_components/boards/CMakeLists.txt#L35>
* <https://duckduckgo.com/?t=ffab&q=ulab+CMake+Error%3A+Error%3A+generator+%3A+NinjaDoes+not+match+the+generator+used+previously%3A+Unix+Makefiles&ia=web>
* <https://stackoverflow.com/questions/51086180/visual-studio-wants-ninja-generator-even-though-i-dont-have-it-installed>
* <https://duckduckgo.com/?t=ffab&q=failed+to+resolve+component+%27esp_adc%27&ia=web>
* <https://github.com/micropython/micropython/issues/9035>
* <https://github.com/micropython/micropython/tree/master/ports/esp32#setting-up-esp-idf-and-the-build-environment>
* <https://github.com/espressif/esp-idf>