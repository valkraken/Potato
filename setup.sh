#!/bin/bash

printf "Select arcitecture:\n[1] Ubuntu\n[2] Arch \n> "
read os

if [ $os = 1 ]; then
  sudo apt update && sude apt upgrade -y
  sudo apt install python3-pip rofi zsh git curl
  pip install qtile
fi

if [ $os = 2 ]; then
  sudo pacman -Syu
  sudo pacman -S rofi zsh git curl nvim python-psutil
  git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
fi



echo 'export PATH="$HOME/.local/bin:$PATH"' >> $HOME/.bashrc
source $HOME/.bashrc


sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


mkdir $HOME/.config
mkdir -p $HOME/.local/share/fonts

cp ./.config/* $HOME/.config/
cp ./local/* $HOME/.local/

fc-cache -f -v 


# Creating desktop entry
sudo echo "W0Rlc2t0b3AgRW50cnldCk5hbWU9UXRpbGUKQ29tbWVudD1UaGlzIHNlc3Npb24gbG9ncyB5b3UgaW50byBRdGlsZQpFeGVjPS9ob21lL3BvdGF0by8ubG9jYWwvYmluL3F0aWxlIHN0YXJ0ClR5cGU9QXBwbGljYXRpb24KWC1HRE0tU2Vzc2lvblJlZ2lzdGVycz10cnVlCktleXdvcmRzPXdtO3RpbGluZw==" | base64 --decode > /usr/share/xsessions/qtile.desktop 
