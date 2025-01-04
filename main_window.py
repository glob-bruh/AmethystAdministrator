"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
main_window - MAIN WINDOWS PYTHON FILE:
--------------------------------------------------
This file contains classes for important windows. 
--------------------------------------------------
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from textwrap import dedent
import threading as th
import random
import webbrowser

import canvasController as cc
import servicesManager as svMgr
import networkVerify as netV
import editHost as modHost


class MainWindow:
    def __init__(self, program_name: str = "Amethyst Administrator", window_main=Tk()):
        self.window_main = window_main
        self.host_array = []
        self.ip_text = None
        self.host_type_drop_val = None
        self.hosts_tree = None
        self.program_name = program_name

    def addHost(self, c):
        x2 = self.ip_text.get()
        x = False
        for i in self.host_array:
            if i[0] == x2:
                messagebox.showwarning(title = "Host Already Exists", message = f"Host with the IP address of \"{x2}\" already exists.")
                x = True
        if x == False:
            x4 = cc.deviceToImg(self.host_type_drop_val.get())
            if x4 == "???":
                x4 = "wstn"
            t = cc.imgToDevice(x4)
            if netV.validateIPv4(x2) == True:
                x1 = cc.hostCanvas(self.host_array, self.window_main, c, x2, x4)
                x3 = self.hosts_tree.insert(
                    "", END,
                    text = x2,
                    values = (t, 0, "Pinger not running", False))
                self.host_array.append( [ x2, x4, x1, x3, {} ] )
            else:
                # https://docs.python.org/3/library/tkinter.messagebox.html
                messagebox.showwarning(title = "Not a Valid IPv4", message = f"The text \"{x2}\" is not a valid IPv4 address.")
        self.ip_text.delete(0, END)
        self.host_type_drop_val.set("workstation")
        print(self.host_array)

    def removeHost(self):
        treeCurSel = self.hosts_tree.item( self.hosts_tree.focus() )["text"]
        x = messagebox.askquestion(title = "Remove Host?", message = f"Are you sure you want to delete the host \"{treeCurSel}\"?")
        if x == "yes" and treeCurSel != "":
            i = 0
            for t in self.host_array:
                if t[0] == treeCurSel:  break
                else:                   i += 1
            cc.removeHostFromCanvas(self.host_array[i][2]) 
            self.hosts_tree.delete(self.host_array[i][3])
            self.host_array.pop(i)
            print(self.host_array)

    def initGui(self, win, tkDefWidth):
        canvas = Canvas(win, width=500, height=500, bg="#171717")
        self.hosts_tree = ttk.Treeview(
            win,
            columns=["deviceType", "numServ", "isOnline", "isControllable"])
        self.hosts_tree.heading("#0", text="IP Address")
        self.hosts_tree.heading("deviceType", text="Device Type")
        self.hosts_tree.heading("numServ", text="Number of Services")
        self.hosts_tree.heading("isOnline", text="Pingable")
        self.hosts_tree.heading("isControllable", text="Controllable")
        ipAddr_lbl = Label(win, width = tkDefWidth, text = "IP Address:")
        self.ip_text = Entry(win, width=tkDefWidth, validate="key")
        self.host_type_drop_val = StringVar()
        self.host_type_drop_val.set("Select Client Type")
        hostType_drop = OptionMenu(
            win, self.host_type_drop_val,
            *["workstation", "server", "router"])
        self.addHost_btn = Button(win, width=tkDefWidth, text="Add Host", command=lambda: self.addHost(canvas))
        removeHost_btn = Button(win, width=tkDefWidth, text="Remove Host", command=lambda: self.removeHost())
        editHost_btn = Button(win, width=tkDefWidth, text="Edit Host", command=lambda: 
            modHost.EditHostWindow(self.host_array, self.hosts_tree.item( self.hosts_tree.focus() )["text"]))
        aboutTheProgram_btn = Button(win, text=f"About", command=lambda: AboutTheProgramWindow(self.program_name))
        Grid.grid_rowconfigure(win, index=0, weight=1)
        Grid.grid_columnconfigure(win, index=0, weight=1)
        canvas.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.hosts_tree.grid(row=7, column=0, columnspan=2, rowspan=4, sticky="nsew")
        ipAddr_lbl.grid(row=1, column=1)
        self.ip_text.grid(row=2, column=1)
        hostType_drop.grid(row=3, column=1)
        self.addHost_btn.grid(row=4, column=1)
        removeHost_btn.grid(row=5, column=1)
        editHost_btn.grid(row=6, column=1)
        aboutTheProgram_btn.grid(row=11, column=0)
        self.pgrmLogo_ico = ImageTk.PhotoImage( Image.open("resources/pic/logo/logoNormal.ico") )
        win.wm_iconphoto(False, self.pgrmLogo_ico)
        win.title(f"{self.program_name}")

class AboutTheProgramWindow:
    def __init__(self, program_name):
        win = Toplevel()
        title_txt = Label(win, text = program_name.upper(), font = ("", 20, "bold"))
        x = Image.open("resources/pic/logo/logoNormal.ico").resize( (125, 125) )
        pgrmLogo_png = ImageTk.PhotoImage(x)
        logo_lbl = Label(win, image = pgrmLogo_png)
        descText = ""
        try:
            with open("LICENSE", "r") as f:
                for x in f:
                    descText += f"{x.strip()}\n"
        except OSError:
            descText = dedent("""
                YOU HAVE BEEN SCAMMED! WHERE IS THE LICENSE FILE?
                You should email me regarding how you acquired this copy of 
                Amethyst Administrator and why the license is not included.
                """)
        aboutDesc_lbl = Label(win, text = descText)
        openGithub_btn = Button(win, text = "GitHub Page", cursor = "hand2", command = lambda: webbrowser.open_new("https://github.com/glob-bruh/AmethystAdministrator"))
        title_txt.grid(row=0, column=0)
        logo_lbl.grid(row=1, column=0)
        aboutDesc_lbl.grid(row=2, column=0)
        openGithub_btn.grid(row=3, column=0)
        win.title(f"About {program_name}")
        win.mainloop()