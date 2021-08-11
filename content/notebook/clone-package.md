To clone your system to another system. Or make a backup. In terminal type:

dpkg --get-selections | grep -v deinstall > ubuntu-files
This command makes a file list of all installed packages in your system (and stores it in present working directory). Backup this file in hdd, email, etc...(this file is very small).

In the freshly installed ubuntu system run:

sudo dpkg --set-selections <./ubuntu-files (will set it up and)

apt-get -y update
apt-get dselect-upgrade
This will install only those packages you had installed (with apt-get) in the old system.

                                    (OR)
You could back up all the .deb packages from /var/cache/apt/archives/ and install them manually using:

dpkg -i *.deb
And after that running an update cycle later.
