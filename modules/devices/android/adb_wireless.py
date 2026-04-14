"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
adb_wireless - WIRELESS ADB CLASSES AND TOOLS:
--------------------------------------------------
This file contains classes for using Android
Debugging Bridge (ADB) wirelessly. 
--------------------------------------------------
"""

import os
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from adb_shell.auth.keygen import keygen

class adbSession:
    def __init__(self, ip):
        if not os.path.isfile("adbkey"):
            keygen("adbkey")
        privateKey = open("adbkey").read()
        publicKey  = open("adbkey.pub").read()
        signer = PythonRSASigner(publicKey, privateKey)
        self.device = AdbDeviceTcp(ip, 5555, default_transport_timeout_s=9)
        self.device.connect(rsa_keys=[signer], auth_timeout_s=0.1)
    
    def sendCommand(self, command):
        x = self.device.shell(command)
        return x