# MACCHANGER

Linux MAC Changer Tool

A Python programmed MAC Address Changer Tool for Linux OS 
------------------------------------------------------------------------------
@@@@@@@@   @@@@@@@   @@@@@@   @@@@@@@    @@@@@@@   @@@@@@    @@@@@@    @@@@@@ 
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@
     @@!  !@@       @@!  @@@  @@!  @@@  !@@       @@!  @@@  !@@       @@!  @@@
    !@!   !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@!       !@!  @!@
   @!!    !@!       @!@!@!@!  @!@!!@!   !@!       @!@  !@!  !!@@!!    @!@!@!@!
  !!!     !!!       !!!@!!!!  !!@!@!    !!!       !@!  !!!   !!@!!!   !!!@!!!!
 !!:      :!!       !!:  !!!  !!: :!!   :!!       !!:  !!!       !:!  !!:  !!!
:!:       :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!      !:!   :!:  !:!
::: ::::   ::: :::  ::   :::  ::   :::   ::: :::  ::::: ::  :::: ::   ::   :::
: :: : :   :: :: :   :   : :   :   : :   :: :: :   : :  :   :: : :     :   : :
------------------------------------------------------------------------------
Why to change the MAC:
1.	As we know that the MAC Address is a unique Address assigned to the network adapter by the Manufacturer, changing it to whatever MAC Address we want can be used to Increase Anonymity.
2.	The MAC Address is often used by filters on the Network to allow devices to connect to the Network and do specific tasks, so being able to change the MAC Address of our device to another device’s MAC Address will allow us to impersonate other devices.
3.	Bypass Filters.

**Tool Usage:**
When running the linux distro as root all we have to do is typing: *python3 macchanger.py --help* to get the usage manual of the tool, anyways if we weren’t using it as root we will have to sudo the command: *sudo python3 macchanger.py --help*, because changing the MAC Address requires root privileges.
We have to specify the Network Interface we like to change its MAC and the new MAC Address we like to assign, so the command must be like:
sudo python3 macchanger.py -i [the interface name] -m [the MAC address to assign]
Or
sudo python3 macchanger.py --interface [the interface name] --mac [the MAC address to assign]

example:
sudo python3 macchanger.py -i eth0 -m 10:20:30:40:50:60
