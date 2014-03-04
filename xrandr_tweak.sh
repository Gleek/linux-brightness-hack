old_brightness=$(xrandr --verbose | grep rightness | awk '{ print $2 }')
#echo $old_brightness
bright=$1
if [ $bright -eq 1 ]
then
br=$(echo "$old_brightness+.1;scale=2"|bc)
elif [ $bright -eq 0 ]
then
br=$(echo "$old_brightness-.1;scale=2"|bc)
fi
tes=$(echo "$br*10;scale=0"|bc)
#echo $br
tes=${tes/.*}
if [ $tes -lt 10 -a $tes -gt 0 ]
then 
xrandr --output "LVDS1" --brightness "$br"
fi
