---
title: Installing ROS2 on an Ubuntu 22 Virtual Machine
tags:
- ros2
- ubuntu
- linux
---

ip a
sudo apt update && sudo apt full-upgrade -y
sudo shutdown now
sudo apt install ubuntu-desktop-minimal 
sudo shutdown now

sudo apt purge firefox
snap list
sudo snap remove --purge firefox
sudo snap remove --purge snap-store
sudo snap remove --purge core20
sudo snap remove --purge lxd
sudo snap remove --purge core20
sudo snap remove --purge snapd
sudo apt remove --autoremove snapd
sudo -H gedit /etc/apt/preferences.d/nonap.pref
sudo nano /etc/apt/preferences.d/nonap.pref
sudo nano /etc/apt/preferences.d/nosnap.pref
sudo apt update
sudo apt upgrade
sudo apt upgrade | grep firefox
sudo apt upgrade
./autorun.sh 
gcc make perl
sudo apt install -y gcc make perl
sudo reboot now
./autorun.sh 
sudo reboot now
sudo apt list --installed ros2
ifconfig
ip -a
ip a
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade
sudo apt install ros-humble-ros-base
sudo reboot now
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp talker
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
sudo apt install ros-dev-tools
ros2 run demo_nodes_py listener
sudo apt install ros-humble-desktop
ros2 run demo_nodes_py listener
sudo shutdown now
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_py listener
cat .bashrc
ros2 run demo_nodes_py listener
sudo shutdown
sudo shutdown now
ls /dev/net
ls -la /dev/net
sudo shutdown now
sudo usermod -a -G vboxusers $USER
cd /media/
ls
ls -la
sudo -i
cd
exit
ls
sudo chown danaukes:danaukes lecture.html
sudo apt install -y flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install -y flathub org.mozilla.firefox
flatpak install com.github.tchx84.Flatseal \
flatpak list
flatpak run Flatseal
flatpak list
flapak run com.github.tchx84.Flatseal
flatpak run com.github.tchx84.Flatseal
firefox
flatpak run org.mozilla.firefox 
sudo cp /media/sf_share/lecture.html ~/
sudo chown danaukes:danaukes lecture.html 
sudo shutdown now
ros2 run demo_nodes_cpp talker
sudo apt list --installed ros-*
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc 
source .bashrc
ros2 run demo_nodes_cpp talker
nano .bashrc
cat <<EOT >> ~/cyclonedds_pc.xml
<CycloneDDS>
    <Domain>
        <General>
            <DontRoute>true</DontRoute>
<!--            <NetworkInterfaceAddress>enp0s3</NetworkInterfaceAddress> DEPRECATED-->
        </General>
    </Domain>
</CycloneDDS>
EOT

sudo mv ~/cyclonedds_pc.xml /etc/
echo "export CYCLONEDDS_URI=/etc/cyclonedds_pc.xml" >> ~/.bashrc
source ~/.bashrc
nano /etc/cyclonedds_pc.xml 
sudo nano /etc/cyclonedds_pc.xml 
nano .bashrc 
cd /etc/
ls
ifconfig
sudo apt install net-tools
ifconfig
sudo apt install software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update && sudo apt install ros-dev-tools
sudo apt update
sudo apt upgrade
sudo apt-get install python3-rosdep
sudo rosdep init
rosdep update
sudo apt install ros-galactic-rmw-cyclonedds-cpp
sudo apt install ros-humble--rmw-cyclonedds-cpp
sudo apt install ros-humble-rmw-cyclonedds-cpp
sudo apt install net-tools -y
echo "export ROS_DOMAIN_ID=0" >> ~/.bashrc
echo "export ROS_LOCALHOST_ONLY=0" >> ~/.bashrc
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" >> ~/.bashrc
source .bashrc
cd
source .bashrc
sudo reboot now
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_cpp listener
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
tailscale status
sudo nano /etc/cyclonedds_pc.xml 
reboot now
sudo reboot now
cat /etc/cyclonedds_pc.xml 
ros2 run demo_nodes_cpp talker
cat .bashrc
nano .bashrc
sudo reboot now
sudo ufw disable
nano .bashrc
ros2 run demo_nodes_cpp listener
ros2 run demo_nodes_cpp talker
ifconfig
sudo nano /etc/cyclonedds_pc.xml 
ros2 run demo_nodes_cpp talker
nano /etc/cyclonedds_pc.xml 
sudo shutdown now
