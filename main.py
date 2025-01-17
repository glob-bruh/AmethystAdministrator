"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
main - MAIN PYTHON FILE:
--------------------------------------------------
This file is the first thing executed. 
--------------------------------------------------
"""

import sys
import random
from main_window import MainWindow
from tkinter import *
from textwrap import dedent

def showBanner():
    print(dedent("""
           ___               __    __               __         ___      __          _          _        __               __            
          / _ |  __ _  ___  / /_  / /   __ __  ___ / /_       / _ | ___/ /  __ _   (_)  ___   (_)  ___ / /_  ____ ___ _ / /_ ___   ____
         / __ | /  ' \/ -_)/ __/ / _ \ / // / (_-</ __/      / __ |/ _  /  /  ' \ / /  / _ \ / /  (_-</ __/ / __// _ `// __// _ \ / __/
        /_/ |_|/_/_/_/\__/ \__/ /_//_/ \_, / /___/\__/      /_/ |_|\_,_/  /_/_/_//_/  /_//_//_/  /___/\__/ /_/   \_,_/ \__/ \___//_/   
                                      /___/                                                                                            
        ================================================ AMETHYST ADMINISTRATOR =======================================================
    """))


def showHelp():
    print(dedent("""
    ----------------------------
    AMETHYST ADMINISTRATOR HELP:
    ----------------------------
    Usage: python3 ./main.py
    ----------------------------
    > Nothing - Launch AA normally.
    > Testing - Adds 3 pre-configured test hosts when started.
    ----------------------------
    """))
    exit(0)


if __name__ == "__main__":
    showBanner()
    window_instance = MainWindow()
    window_instance.initGui(window_instance.window_main, 20)
    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "help":
                showHelp()
            case "testing":
                window_instance.ip_text.delete(0, END) ; window_instance.ip_text.insert(0, "192.168.0.1") ; window_instance.addHost_btn.invoke()
                window_instance.host_array[0][1][1] = "WORKSTATION-" + str(random.randint(00000, 99999))
                window_instance.host_array[0][4] = {'Finance SSH': ['22', 'sys', 'p@ssw0rd']}
                window_instance.ip_text.delete(0, END) ; window_instance.ip_text.insert(0, "192.168.0.2") ; window_instance.addHost_btn.invoke()
                window_instance.host_array[1][1][1] = "WORKSTATION-" + str(random.randint(00000, 99999))
                window_instance.host_array[1][4] = {'Workshop SSH': ['22', 'sys', 'p@ssw0rd']}
                window_instance.ip_text.delete(0, END) ; window_instance.ip_text.insert(0, "192.168.0.3") ; window_instance.addHost_btn.invoke()
                window_instance.host_array[2][1][1] = "WORKSTATION-" + str(random.randint(00000, 99999))
                window_instance.host_array[2][4] = {'Front Desk FTP': ['21', 'sys', 'p@ssw0rd']}
    window_instance.window_main.mainloop()
