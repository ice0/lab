import gi
#gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
#from gi.repository import Gtk
from gi.repository import Gdk

#slaves = Gdk.Seat().get_slaves()
print("Get default display...")
display = Gdk.Display().get_default()
if (display == None):
    print("Display not found!")
    exit

print("Get default seat...")
seat = display.get_default_seat()
if (seat == None):
    print("Default seat not found!")
    exit

print("Get slaves...")
#slaves = seat.get_slaves(Gdk.SeatCapabilities.ALL)
slaves = seat.get_slaves(Gdk.SeatCapabilities.NONE)
if (slaves == None):
    print("Slaves not found!")
    exit
    
print("Found slaves (" + str(len(slaves)) + ")")

#slaves = seat.get_slaves(Gdk.SeatCapabilities.ALL_POINTING)

#for slave in slaves:
#    print(slave.get_name())

print("================================")

#Gtk.main()