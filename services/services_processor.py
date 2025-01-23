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

#def determineService(ip, port, cred):
#    print("test")


class AndroidDebugBridge:
    def __init__(self, ip):
        try: 
            self.adbDevice = adb_wireless.adbSession(ip)
        except OSError:
            print("Failed To Connect")
        else:
            print(f"Connected: {self.adbDevice}")
            self.adbTerm = term.TerminalWindow("ADB", self.adbDevice)