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

# MacOS output
# - - - - - - - - - - - - - - - 
#Number of displays(0)
#Get default display...
#./test_seat.py:21: DeprecationWarning: Gdk.Display.get_device_manager is deprecated
#  devices = display.get_device_manager().list_devices(Gdk.DeviceType.MASTER)
#./test_seat.py:21: DeprecationWarning: Gdk.DeviceManager.list_devices is deprecated
#  devices = display.get_device_manager().list_devices(Gdk.DeviceType.MASTER)
#Number of devices(2)
#Core Pointer
#Core Keyboard
#Get default seat...
#Get slaves...
#Found slaves (0)
#Core Pointer

# Linux output
# - - - - - - - - - - - - - -
#xinput list
#⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
#⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
#⎜   ↳ VMware VMware Virtual USB Mouse         	id=7	[slave  pointer  (2)]
#⎜   ↳ VirtualPS/2 VMware VMMouse              	id=9	[slave  pointer  (2)]
#⎜   ↳ VirtualPS/2 VMware VMMouse              	id=10	[slave  pointer  (2)]
#⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
#    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
#    ↳ Power Button                            	id=6	[slave  keyboard (3)]
#    ↳ AT Translated Set 2 keyboard            	id=8	[slave  keyboard (3)]
#$ python ./test_seat.py 
#Number of displays(0)
#Get default display...
#./test_seat.py:21: DeprecationWarning: Gdk.Display.get_device_manager is deprecated
#  devices = display.get_device_manager().list_devices(Gdk.DeviceType.MASTER)
#./test_seat.py:21: DeprecationWarning: Gdk.DeviceManager.list_devices is deprecated
#  devices = display.get_device_manager().list_devices(Gdk.DeviceType.MASTER)
#Number of devices(2)
#Virtual core keyboard
#Virtual core pointer
#Get default seat...
#Get slaves...
#Found slaves (4)
#VMware VMware Virtual USB Mouse
#VirtualPS/2 VMware VMMouse
#VirtualPS/2 VMware VMMouse
#Virtual core XTEST pointer
#Virtual core pointer
