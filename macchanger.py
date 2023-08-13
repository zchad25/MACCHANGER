#!/usr/bin/env python3

import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="Interface", help="The Interface to change its MAC")
    parser.add_option("-m", "--mac", dest="Mac", help="The new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.Interface:
        parser.error("[-] C'mon enter the Interface, use --help for more info.")
    elif not options.Mac:
        parser.error("[-] C'mon enter the new MAC address, use --help for more info.")
    return options
def mac_changer(Interface, Mac):
    print("[*] Changing The MAC Address of " + Interface + " to " + Mac)
    subprocess.call(["ifconfig", Interface, "down"])
    subprocess.call(["ifconfig", Interface, "hw", "ether", Mac])
    subprocess.call(["ifconfig", Interface, "up"])
def get_current_mac(Interface):
    ifconfig_result = subprocess.check_output(["ifconfig", Interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Could not read MAC Address.")

def print_banner():
    print("")
    print("------------------------------------------------------------------------------")
    print("@@@@@@@@   @@@@@@@   @@@@@@   @@@@@@@    @@@@@@@   @@@@@@    @@@@@@    @@@@@@ ")
    print("@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@")
    print("     @@!  !@@       @@!  @@@  @@!  @@@  !@@       @@!  @@@  !@@       @@!  @@@")
    print("    !@!   !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@!       !@!  @!@")
    print("   @!!    !@!       @!@!@!@!  @!@!!@!   !@!       @!@  !@!  !!@@!!    @!@!@!@!")
    print("  !!!     !!!       !!!@!!!!  !!@!@!    !!!       !@!  !!!   !!@!!!   !!!@!!!!")
    print(" !!:      :!!       !!:  !!!  !!: :!!   :!!       !!:  !!!       !:!  !!:  !!!")
    print(":!:       :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!      !:!   :!:  !:!")
    print("::: ::::   ::: :::  ::   :::  ::   :::   ::: :::  ::::: ::  :::: ::   ::   :::")
    print(": :: : :   :: :: :   :   : :   :   : :   :: :: :   : :  :   :: : :     :   : :")
    print("------------------------------------------------------------------------------")

print_banner()
options = get_arguments()
current_mac = get_current_mac(options.Interface)
print("[*] Current MAC = " + str(current_mac))
mac_changer(options.Interface, options.Mac)
current_mac = get_current_mac(options.Interface)
if current_mac == options.Mac:
    print("[*] MAC Address was successfully changed to " + current_mac)
else:
    print("[-] MAC Address did not get changed.")

