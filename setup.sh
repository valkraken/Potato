#!/bin/bash

sudo apt install python3-pip rofi zsh git curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

pip install qtile

cp ./.config/* $HOME/.config/
cp ./local/bin/* $HOME/.local/bin/

# Creating desktop entry
sudo echo "W0Rlc2t0b3AgRW50cnldCk5hbWU9UXRpbGUKQ29tbWVudD1UaGlzIHNlc3Npb24gbG9ncyB5b3UgaW50byBRdGlsZQpFeGVjPS9ob21lL3BvdGF0by8ubG9jYWwvYmluL3F0aWxlIHN0YXJ0ClR5cGU9QXBwbGljYXRpb24KWC1HRE0tU2Vzc2lvblJlZ2lzdGVycz10cnVlCktleXdvcmRzPXdtO3RpbGluZw==" | base64 --decode > /usr/share/xsessions/qtile.desktop 
