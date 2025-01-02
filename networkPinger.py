"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
networkPinger - NETWORK UPTIME MONITORING:
--------------------------------------------------
Contains code for ensuring clients added to the
program are pinged continuously.
--------------------------------------------------
"""

import threading as th
import socket
import struct

class icmpPingSend():
    def __init__():
        print("based")

class pinger(th.Thread): #for some reason target doesnt match when more than one on canvas - MENU IN GENERAL ISSUE !!! ADD IP VIEW TO TOP OF MENU TO KNOW WHO ITS FOR
    def __init__(self, ip):
        self.target = ip
        th.Thread.__init__(self)
        self.start()

    def run(self):
        print(f"bruh --> {self.target}")


def sendPingAndProcResponse(ip):
    print("nothing")