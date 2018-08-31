import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

#slaves = Gdk.Seat().get_slaves()
display = Gdk.Display().get_default()
if (display == None):
    print("Display not found!")
    exit

seat = display.get_default_seat()
if (seat == None):
    print("Default seat not found!")
    exit

#slaves = seat.get_slaves(Gdk.SeatCapabilities.ALL)
slaves = seat.get_slaves(Gdk.SeatCapabilities.ALL_POINTING)

for slave in slaves:
    print(slave.get_name())

Gtk.main()