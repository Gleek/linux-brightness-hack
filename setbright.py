#!/usr/bin/python
import argparse
import dbus

default = 20
bus = dbus.SessionBus()

proxy = bus.get_object('org.gnome.SettingsDaemon',
                       '/org/gnome/SettingsDaemon/Power')
iface = dbus.\
  Interface(proxy, dbus_interface='org.gnome.SettingsDaemon.Power.Screen')


cur_lev = iface.GetPercentage()
print "Current Brightness:", cur_lev 
# Description
parser = argparse.ArgumentParser(description='Sets the Monitor Brightness')

# Set int argument:
parser.add_argument("level", nargs="?", type=int, help='Integer 1 to increase or 0 to decrease')
# nargs="?" wont make error if missing argument

args = parser.parse_args()

#print 'Bright: ', args.level

if not args.level and args.level != 0:

    # Setting brightness to default value:
    leve = default
    

else:
        ar = args.level
        if ar == 1:
        	level = cur_lev + 10
        elif ar == 0:
        	level = cur_lev - 10

print "Setting brightness to: ", level

# Set brightness:
try:
    iface.SetPercentage(level)
except:
    print "Brightness on it's li"
