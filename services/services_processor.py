"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
services_processor - SERVICES PROCESSOR:
--------------------------------------------------
fill me in
--------------------------------------------------
"""

from tkinter import *
from tkinter import messagebox

import terminal as term
from devices.android import adb_wireless

def determineService(hArr, ip):
    for x in hArr:
        if x[0] == ip:
            serviceList = x[4]
    e = [False, ""]
    for x in serviceList:
        try:
            print(f"Try: {serviceList[x][0]}")
            match int(serviceList[x][0]):
                case 21:   print("No file mgmnt yet.")
                case 22:   SSHServiceLaunch() # this is to text except, doesnt exist yet.  
                case 5555: AndroidDebugBridge(ip)
        except Exception as thisEx:
            e[0] = True
            e[1] += f"\n\u2022 Service \"{x}\": {str(thisEx)}."
    if e[0] == True:
        messagebox.showwarning(title="Failed to connect to service(s)", message=f"Failed to connect to one or more services running on {ip}!{e[1]}") # shows up only when window is closed? Also check for successful connection to a service. 


class AndroidDebugBridge:
    def __init__(self, ip):
        self.adbDevice = adb_wireless.adbSession(ip)
        self.adbTerm = term.TerminalWindow("ADB", self.adbDevice)