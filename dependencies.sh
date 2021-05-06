#!/bin/bash
echo "Installing dependencies for python program"
echo "Please wait"

if [ $(whoami) != 'root' ]
then
    echo "
This script needs to be run as root, or with sudo:
    sudo $0
"
    exit 1
fi

### install python3 pip
sudo apt install python3-pip
### Install argon2-cffi 
pip3 install argon2-cffi
### Install tkinter
apt-get install python3-tk
