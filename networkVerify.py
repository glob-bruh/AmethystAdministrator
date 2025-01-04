"""
------------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
------------------------------------------------------
networkVerify - NETWORK VERIFICATION FUNCTIONS:
------------------------------------------------------
Contains a set of functions to verify networks details
such as IP addresses and subnets. 
------------------------------------------------------
"""


def validateIPv4(ipInput):
    x = ipInput.split(".")
    if len(x) < 4 or len(x) > 4:
        return False
    else:
        for i in x:
            try:        n = int(i)
            except:     return False
            if n > 254: return False
        return True