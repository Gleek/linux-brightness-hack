linux-brightness-hack
=====================

Scripts to change brightness in a X-windows system.
Find detail in http://noobpanic.wordpress.com/2014/02/27/fixing-brightness

###Usage###
#####brchange.sh#####
- To increase brightness <code>sudo brchange.sh inc</code>. This will increase the brightness by 10%.
- To decrease brightness <code>sudo brchange.sh dec </code>. This will decrease the brightness by 10%.
- To run it automatically add the script in /etc/sudoers (Refer to blog for details).
- Run it with <code>gnome-terminal -x bash -c "sudo /path/to/brchange.sh inc"</code> or <code>gnome-terminal -x bash -c "sudo /path/to/brchange.sh dec"</code>

#####setbright.py#####
- Use <code>python /path/to/script 1</code> to increase brightness by 10%.
- Use <code>python /path/to/script 0</code> to decrease brightness by 10%.

#####xrandr_tweak.sh#####
- Use <code>xrandr_tweak.sh 1</code> to increase brightness by 10%.
- Use <code>xrandr_tweak.sh 0</code> to decrease brightness by 10%.
