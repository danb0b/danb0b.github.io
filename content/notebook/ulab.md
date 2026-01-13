---
title: Compliling uLab for micropython
---

```bash
sudo apt update && sudo apt install -y \
python3 \
git \
python3-pip \
python3-virtualenv \
python3-venv \
wget \
flex \
bison \
gperf \
cmake \
libusb-1.0-0-dev

git clone https://github.com/v923z/micropython-ulab.git ulab && \
git clone https://github.com/micropython/micropython.git
export BUILD_DIR=$(pwd)
cd $BUILD_DIR/micropython/

git clone -b v5.2.3 --recursive https://github.com/espressif/esp-idf.git

cd $BUILD_DIR/micropython/esp-idf

./install.sh esp32
. ./export.sh
which idf.py

cd $BUILD_DIR/micropython/ports/esp32

cd $BUILD_DIR/micropython/mpy-cross
make

cd $BUILD_DIR/micropython/ports/esp32
make submodules

cd $BUILD_DIR/micropython/ports/esp32
cat << EOT | tee makefile
BOARD = ESP32_GENERIC
USER_C_MODULES = $(BUILD_DIR)/ulab/code/micropython.cmake

include Makefile
EOT

cmake .
make
```

* <https://github.com/v923z/micropython-ulab>
* <https://www.danaukes.com/notebook/micropython-on-linux/>
* <https://stackoverflow.com/questions/36022051/docker-no-such-file-or-directory>
* <https://www.pythonpool.com/resolving-usr-bin-env-python-no-such-file-or-directory-error/>
* <https://samialperenakgun.com/blog/2022/04/save-docker-bash-history/>
* <https://esp32.com/viewtopic.php?t=23020>
* <https://github.com/micropython/micropython/wiki/Build-Troubleshooting>
* <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html>
* <https://github.com/espressif/esp-iot-solution/issues/309>
* <https://github.com/espressif/esp-iot-solution/blob/master/examples/common_components/boards/CMakeLists.txt#L35>
* <https://stackoverflow.com/questions/51086180/visual-studio-wants-ninja-generator-even-though-i-dont-have-it-installed>
* <https://github.com/micropython/micropython/issues/9035>
* <https://github.com/micropython/micropython/tree/master/ports/esp32#setting-up-esp-idf-and-the-build-environment>
* <https://github.com/espressif/esp-idf>
* <https://github.com/micropython/micropython/issues/15287>
* <https://stackoverflow.com/questions/48596147/why-does-my-esp32-keep-on-reseting-after-startup#60733260>
