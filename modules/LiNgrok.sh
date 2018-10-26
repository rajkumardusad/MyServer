#!/bin/bash
# Tool Name :- MyServer
# Author :- Rajkumar Dusad
# Date :- 22/5/2018
# Powered By :- Aex Software's
file="ngrok"
pkg install tar -y
pkg install curl -y
apt-get install curl -y 
apt-get install tar -y
sudo apt-get install curl -y
sudo apt-get install tar -y
if [ -f "/usr/bin/$file" ]; then
    first=1
    echo "skipping downloading"
fi
if [ -f "/data/data/com.termux/files/usr/bin/$file" ]; then
    first=1
    echo "skipping downloading"
fi
if [ "$first" != 1 ];then
    if [ ! -f "/usr/bin/sudo" ]; then
        echo "downloading Ngrok"
        if [ "$(dpkg --print-architecture)" = "aarch64" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "arm" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "i686" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "i386" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "armhf" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "armv7" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "arm64" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "armv8" ];then
            cd ~/ && curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz -o ngrok.tar.gz
        else
            echo "unknown architecture"
            exit 1
        fi
    fi
    if [ -f "/usr/bin/sudo" ]; then
        echo "downloading Ngrok"
        if [ "$(dpkg --print-architecture)" = "aarch64" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "arm" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "i686" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "i386" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "armhf" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "armv7" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "arm64" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz -o ngrok.tar.gz
        elif [ "$(dpkg --print-architecture)" = "armv8" ];then
            cd ~/ && sudo curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz -o ngrok.tar.gz
        else
            echo "unknown architecture"
            exit 1
        fi
    fi
fi
cd ~/ && tar -xvzf ngrok.tar.gz
cd ~/ && rm -rf ngrok.tar.gz
if [ -d "/bin/" ]; then
    mv -v ~/ngrok /usr/bin/
    chmod +x /usr/bin/ngrok
fi
if [ -f "/usr/lib/sudo" ]; then
    sudo mv -v ~/ngrok /usr/bin/
    sudo chmod +x /usr/bin/ngrok
    cd ~/ && sudo rm -rf ngrok.tar.gz
fi
if [ -d "/data/data/com.termux/files/usr/bin/" ]; then
    mv -v ~/ngrok /data/data/com.termux/files/usr/bin/
    chmod +x /data/data/com.termux/files/usr/bin/ngrok
fi
