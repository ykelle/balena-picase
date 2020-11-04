#!/bin/bash

SourcePath=https://raw.githubusercontent.com/RetroFlag/retroflag-picase/master

#RetroFlag pw io ;2:in ;3:in ;4:in ;14:out 1----------------------------------------
wget -O  "/mnt/boot/overlays/RetroFlag_pw_io.dtbo" "$SourcePath/RetroFlag_pw_io.dtbo"

#Reboot to apply changes----------------------------
echo "RetroFlag Pi Case installation done. Will now reboot after 3 seconds."
sleep 3
reboot
#-----------------------------------------------------------


