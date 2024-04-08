#!/bin/bash

sudo apt install kde-plasma-desktop

echo "Seting up service"
sudo mv ./files/plasma-i3.desktop /usr/share/xsessions
sudo mv ./files/plasma-i3.sh/usr/local/bin/
mv ./files/plasma-i3.service $HOME/.config/systemd/user
