import gi
#gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
#from gi.repository import Gtk
from gi.repository import Gdk

Gdk.init("")

displays = Gdk.DisplayManager().list_displays()
print("Number of displays(" + str(len(displays)) + ")")



#slaves = Gdk.Seat().get_slaves()
print("Get default display...")
display = Gdk.Display().get_default()
if (display == None):
    print("Display not found!")
    exit

devices = display.get_device_manager().list_devices(Gdk.DeviceType.MASTER)
#devices = display.get_device_manager().list_devices(Gdk.DeviceType.SLAVE)
#devices = display.get_device_manager().list_devices(Gdk.DeviceType.FLOATING)
print("Number of devices(" + str(len(devices)) + ")")
for device in devices:
    print(device.get_name())


print("Get default seat...")
seat = display.get_default_seat()
if (seat == None):
    print("Default seat not found!")
    exit

print("Get slaves...")
#slaves = seat.get_slaves(Gdk.SeatCapabilities.ALL)
slaves = seat.get_slaves(Gdk.SeatCapabilities.ALL_POINTING)
#slaves = seat.get_slaves(Gdk.SeatCapabilities.NONE)
if (slaves == None):
    print("Slaves not found!")
    exit

print("Found slaves (" + str(len(slaves)) + ")")
for slave in slaves:
    print(slave.get_name())
    
pointer = seat.get_pointer()
print(pointer.get_name())

print("================================")

#Gtk.main()