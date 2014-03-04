#!/bin/bash
cur_br=$(cat /sys/class/backlight/acpi_video0/brightness)
newbr=$cur_br
if [ $1 = "inc" ]
then
	newbr=$(($cur_br+1))
elif [ $1 = "dec" ]
then 
	newbr=$(($cur_br-1))
fi
sudo echo "$newbr">/sys/class/backlight/acpi_video0/brightness
	

