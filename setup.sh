#!/bin/bash

sudo apt install python3-pip rofi zsh git curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

pip install qtile

cp ./.config/* $HOME/.config/
cp ./local/bin/* $HOME/.local/bin/

# Creating desktop entry
sudo echo "" | base64 --decode > /usr/share/xsession/qtile.desktop 
