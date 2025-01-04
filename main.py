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

from main_window import MainWindow
from tkinter import *

if __name__ == "__main__":
    window_instance = MainWindow()
    window_instance.initGui(window_instance.window_main, 20)
    #################################
    # TESTING STUFF - Add clients automatically for testing.
    window_instance.ip_text.delete(0, END) ; window_instance.ip_text.insert(0, "192.168.0.1") ; window_instance.addHost_btn.invoke()
    window_instance.ip_text.delete(0, END) ; window_instance.ip_text.insert(0, "192.168.0.2") ; window_instance.addHost_btn.invoke()
    window_instance.ip_text.delete(0, END) ; window_instance.ip_text.insert(0, "192.168.0.3") ; window_instance.addHost_btn.invoke()
    #################################
    window_instance.window_main.mainloop()
