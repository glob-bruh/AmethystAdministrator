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
    def __init__(self, target):
        self.target = target
        self.port = None
        self.data = b"ping pong!"
        self.ttl = 64
        self.icmp_id = 12345
        print("based")
        print(f"bruh --> {self.target}")
    
    def sendPacket(self):
        icmp_type = 8
        icmp_code = 0
        icmp_chksum = 0
        icmp_seq = 1
        icmp_header = struct.pack(
            "!BBHHH", icmp_type, icmp_code, 
            icmp_chksum, self.icmp_id, icmp_seq)

class pinger(th.Thread):
    def __init__(self, ip):
        self.target = ip
        th.Thread.__init__(self)
        self.start()

    def run(self):
        icmpPingSend(self.target)


def sendPingAndProcResponse(ip):
    print("nothing")