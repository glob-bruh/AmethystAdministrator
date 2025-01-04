"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
editHost - CLASSES FOR THE "EDIT HOST" WINDOW:
--------------------------------------------------
Contains functions needed to allow for editing
hosts already present in the program.
--------------------------------------------------
"""

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from textwrap import dedent
import threading as th
import random

import canvasController as cc
import networkVerify as netV

class EditHostWindow:
    def __init__(self, hArr, ip):
        self.win = Tk()
        winHead_lbl = Label(self.win, text = f"EDIT HOST {ip}", font=("", 17, "bold"))
        hostname_lbl = Label(self.win, text="Hostname:")
        hostname_txt = Entry(self.win)
        deviceType_lbl = Label(self.win, text="Device Type:")
        self.deviceType_drp_val = StringVar(self.win)
        for x in hArr:
            if x[0] == ip:
                self.deviceType_drp_val.set( cc.imgToDevice(x[1]) )
        deviceType_drp = OptionMenu(
            self.win, self.deviceType_drp_val,
            *["workstation", "server", "router"])
        saveEdit_btn = Button(self.win, text="Save and Close")
        cancelEdit_btn = Button(self.win, text="Cancel")
        winHead_lbl.grid(row=0, column=0, columnspan=2)
        hostname_lbl.grid(row=1, column=0)
        hostname_txt.grid(row=1, column=1)
        deviceType_lbl.grid(row=2, column=0)
        deviceType_drp.grid(row=2, column=1)
        saveEdit_btn.grid(row=5, column=0)
        cancelEdit_btn.grid(row=5, column=1)
        self.win.title(f"Edit Host - {ip}")
        self.win.mainloop()