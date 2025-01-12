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

import canvas_controller as cc
import network_verify as netV

class EditHostWindow:
    def __init__(self, hArr, ip):
        if ip != "":
            self.win = Tk()
            self.ip = ip
            self.array = hArr
            winHead_lbl = Label(self.win, text = f"EDIT HOST {self.ip}", font=("", 17, "bold"))
            hostname_lbl = Label(self.win, text="Hostname:")
            self.hostname_txt = Entry(self.win)
            deviceType_lbl = Label(self.win, text="Device Type:")
            self.deviceType_drp_val = StringVar(self.win)
            for x in self.array:
                if x[0] == ip:
                    self.hostname_txt.insert(0, x[1][1])
                    self.deviceType_drp_val.set( cc.imgToDevice(x[1][0]) )
            deviceType_drp = OptionMenu(
                self.win, self.deviceType_drp_val,
                *["workstation", "server", "router"])
            saveEdit_btn = Button(self.win, text="Save and Close", command=lambda: self.saveEditChanges())
            cancelEdit_btn = Button(self.win, text="Cancel", command=lambda: self.win.destroy())
            winHead_lbl.grid(row=0, column=0, columnspan=2)
            hostname_lbl.grid(row=1, column=0)
            self.hostname_txt.grid(row=1, column=1)
            deviceType_lbl.grid(row=2, column=0)
            deviceType_drp.grid(row=2, column=1)
            saveEdit_btn.grid(row=5, column=0)
            cancelEdit_btn.grid(row=5, column=1)
            self.win.title(f"Edit Host - {self.ip}")
            self.win.mainloop()
    
    def saveEditChanges(self):
        # Canvas and TreeView needs to be updated after these are set.
        for x in self.array:
            if x[0] == self.ip:
                x[1][0] = cc.deviceToImg(self.deviceType_drp_val.get())
                x[1][1] = self.hostname_txt.get()