"""
Return text based on the tab number passed
"""

def descriptions(index):
	if index == 0:
		return text_0
	elif index == 1:
		return text_1
	elif index == 2:
		return text_2
	elif index == 3:
		return text_3
	elif index == 4:
		return text_4
	elif index == 5:
		return text_5
	elif index == 6:
		return text_6
	elif index == 7:
		return text_7
	elif index == 8:
		return text_8
	elif index == 9:
		return text_9
	elif index == 10:
		return text_10
	elif index == 20:
		return text_20
	elif index == 30:
		return text_30
	else:
		return text_no

text_0 = """
Help Text for Machine Tab

Configuration Name is letters, numbers, spaces (replaced by underscore)
Version = 1.1 or higher

IP Address 10.10.10.10 is recommended to avoid conflicts on your LAN
	10.10.10.10 W5 Down W6 Up
	192.168.1.121 W5 Down W6 Down

Maximum Linear Velocity is in User Units per second.

Firmware
To read the current firmware select the IP Address first.
	After reading the current firmware the Copy button will place the text in the clipboard.
To flash a card select the firmware and IP Address first.
	After flashing Reload or Power Cycle the card
"""

text_1 = """
Help Text for Display Tab
Offset and Feedback display use relative (including offsets) or absolute machine.
Overrides use percent of programed value.
QtPyVCP can only be installed on Debian 9
"""

text_2 = """
Help Text for Axis Tab

Joints must be configured starting with 0 and not skipping any.

Any joint can have any axis letter.

Scale is the number of steps to move one user unit (inch or mm).
Limits are in user units.
Velocity is user units per second, Acceleration is user units per second per second

Axis, PID Settings and StepGen Settings are required.

Homing fields are optional.

For gantry type of machines just select the same axis for each joint.
"""

text_3 = """
Help Text for Spindle Tab
"""

text_4 = """
Help Text for Inputs Tab

Inputs are optional

If the input is a type that is associated with an axis the axis must be
specified.
"""

text_5 = """
Help Text for Outputs Tab

Outputs are optional.
"""

text_6 = """
Help Text for Options Tab

On Screen Prompt for Manual Tool Change
	This option is if you run G code with more than one tool and the tools can be
	preset like BT and Cat holders. If you have collet type like ER and R8 you
	should not check this and you should only one tool per G code program and
	touch it off before running the program.

Hal User Interface
	This option enables halui which exports hal pins so they can be connected to
	physical or VCP or used in your hal configuration. These include pins related
	to abort, tool, spindle, program, mode, mdi, coolant, max velocity, machine,
	lube, joint, jog, feed override, rapid override, e stop, axis and home.

PyVCP Panel
	This option adds the connections and a basic PyVCP panel.

GladeVCP Panel
	Not functioning at this point.

Debug Options
	This sets the debug level that is used when an error happens. When an error
	occours the error information is sent to dmesg. Open a terminal and clear
	dmesg with sudo dmesg -c then run your configuration and to view the error
	in a terminal type dmesg.
"""

text_7 = """
Help Text for PLC Tab

Classicladder PLC will add a basic PLC to the configuration. You can also set
the number of components that Classicladder starts with.
"""

text_8 = """
Help Text for Pins Tab

If you have the 7i96 connected press get pins to get the current pinout
"""

text_9 = """
Help Text for Info Tab

Get CPU information and NIC information
"""
text_10 = """
Help Text for PC Tab

To check if the network packet time is ok get the CPU speed from the Info Tab.
Then get the tmax time and put those values into the boxes then hit calculate.
Make sure you select if the CPU speed is gHz or mHz.

To get tMax you must have the 7i96 connected to the PC and be running the
configuration with LinuxCNC.
"""

text_20 = """
Help Text for Building the Configuration

Opening the sample ini file and modifying is the fastest way to get a working configuration.
Check Configuration will scan the configuration for errors
Build Configuration will build all the configuration files needed.
	The ini file is always overwritten.
	The configName.hal file will always be overwritten.
	The tool table, variable file, postgui.hal, custom.hal, configName.clp,
	configName.xml files are never overwritten if present. To get a new one delete
	the file and a new one will be created when you build the configuration.
"""

text_30 = """
Help Text for PC Setup

7i96 card requires the Master Branch of LinuxCNC

Mesa Ethernet Cards require LinuxCNC Uspace and the PREEMPT kernel.

Instructions to download and install Debian 9 and LinuxCNC Uspace with the
desktop of your choice

https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/
drill down to the latest version of the nonfree amd64 iso-cd netinst.iso

Burn to a CD if you have a PCI Ethernet card remove it, setup with the on board LAN only
Boot from the CD
Graphical Install, Do Not enter a Root Password! Just hit enter
Debian desktop environment, Mate, SSH server,Print server, standard system utilities

after booting to Debian 9 open a terminal
sudo nano /etc/lightdm/lightdm.conf
to log in without your user name a password uncomment and add your user name
autologin-user=yourusername
autologin-user-timeout=0
CTRL X and yes to save and exit.

Open the Synaptic Package Manager
search for linux-image and install linux-image-latest.version-rt

reboot the pc

in a terminal
uname -a     # it should report back PREEMT RT
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install dirmngr
sudo apt-get install software-properties-common
*** to get the buildbot current build
sudo apt-key adv --keyserver hkp://keys.gnupg.net --recv-key E0EE663E
sudo add-apt-repository "deb http://buildbot.linuxcnc.org/ stretch master-rtpreempt"
sudo apt-get update
sudo apt-get install linuxcnc-uspace

Configure the network adapter to work with an Ethernet card
To find the Ethernet adapter name
ip link show

sudo nano /etc/network/interfaces
auto enp0s25 << change to match your interface name
  iface enp0s25 inet static
    address 10.10.10.1
    netmask 255.255.255.0

shutdown and install a second LAN card if you need to connect to the internet

for git and programming tools
sudo apt-get install git-core git-gui make gcc

to add open in terminal to caja
sudo apt-get install caja-open-terminal

to be able to edit the menu add mozo
sudo apt-get install mozo
You will find it in System > Control Center > Main Menu
"""

text_no = """
No Help is found for this tab
"""

