#!/bin/bash

sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock

sudo apt-get install git
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-pip
sudo pip install boto3
sudo apt-get install -f
sudo pip install numpy
sudo pip install opencv-python
sudo apt-get install build-essential


sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev liblapacke-dev

sudo apt-get install libxvidcore-dev libx264-dev

sudo apt-get install libatlas-base-dev gfortran

sudo apt-get install ffmpeg

sudo pip install Pillow
sudo pip install requests
sudo apt-get install libboost-all-dev
sudo apt-get install python-tk
sudo apt-get install python3-tk 


#Download opencv source
#https://opencv.org/releases.html

unzip opencv-3.4.0.zip
cd ~/opencv-3.4.0
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j4
sudo make install
