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

import threading as th
import random
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from textwrap import dedent
from hashlib import sha256

import canvas_controller as cc
import network_verify as netV
import edit_host as eHost
import terminal as term
from services import services_manager as svMgr
#from devices.android import adb_wireless

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
            x4 = self.host_type_drop_val.get()
            if netV.validateIPv4(x2) == True:
                x1 = cc.hostCanvas(self.host_array, self.window_main, c, x2, x4)
                x3 = self.hosts_tree.insert(
                    "", END,
                    text = x2,
                    values = (x4, 0, "Pinger not running", False))
                self.host_array.append( [ x2, [x4, ""], x1, x3, {} ] )
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
        ipAddr_lbl = Label(win, width=tkDefWidth, text = "IP Address:")
        self.ip_text = Entry(win, width=tkDefWidth, validate="key")
        self.host_type_drop_val = StringVar(win)
        self.host_type_drop_val.set("workstation")
        hostType_drop = OptionMenu(
            win, self.host_type_drop_val,
            *["workstation", "server", "router", "smartphone"])
        self.addHost_btn = Button(win, width=tkDefWidth, text="Add Host", command=lambda: self.addHost(canvas))
        removeHost_btn = Button(win, width=tkDefWidth, text="Remove Host", command=lambda: self.removeHost())
        editHost_btn = Button(win, width=tkDefWidth, text="Edit Host", command=lambda: 
            eHost.EditHostWindow(self.host_array, self.hosts_tree.item( self.hosts_tree.focus() )["text"]))
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
        win.title(self.program_name)


class AboutTheProgramWindow:
    def __init__(self, program_name):
        win = Toplevel()
        title_txt = Label(win, text = program_name.upper(), font = ("", 17, "bold"))
        x = Image.open("resources/pic/logo/logoNormal.ico").resize( (125, 125) )
        pgrmLogo_png = ImageTk.PhotoImage(x)
        logo_lbl = Label(win, image=pgrmLogo_png)
        descText = ""
        try:
            CHANGE_ME_WITH_EXTREME_CAUTION_READ_THE_LICENSE = "c92648ad0606ef9256fd170e7c8566b1949382baff50fbfb7e4bc446dd7f54d0"
            fileHash = sha256()
            with open("LICENSE", "rb") as f:
                for b in iter(lambda: f.read(4096),b""):
                    fileHash.update(b)
            if fileHash.hexdigest().lower() != CHANGE_ME_WITH_EXTREME_CAUTION_READ_THE_LICENSE:
                descText = dedent("""
                    YOU HAVE BEEN SCAMMED! SOMEONE TAMPERED WITH THE LICENSE!
                    You should email me regarding how you acquired this copy of 
                    Amethyst Administrator and why it has shipped with a modified license.
                    """)
            else:
                with open("LICENSE", "r") as f:
                    for x in f:
                        descText += f"{x.strip()}\n"
        except OSError:
            descText = dedent("""
                YOU HAVE BEEN SCAMMED! WHERE IS THE LICENSE FILE?
                You should email me regarding how you acquired this copy of 
                Amethyst Administrator and why the license is not included.
                """)
        aboutDesc_lbl = Label(win, text=descText)
        openGithub_btn = Button(win, text="GitHub Page", cursor="hand2", command=lambda: webbrowser.open_new("https://github.com/glob-bruh/AmethystAdministrator"))
        experimentsWindow_btn = Button(win, text="Experiments", cursor="hand2", command=lambda: ExperimentsWindow(program_name))
        title_txt.grid(row=0, column=0, columnspan=2)
        logo_lbl.grid(row=1, column=0, columnspan=2)
        aboutDesc_lbl.grid(row=2, column=0, columnspan=2)
        openGithub_btn.grid(row=3, column=0)
        experimentsWindow_btn.grid(row=3, column=1)
        win.title(f"About {program_name}")
        win.mainloop()

class ExperimentsWindow:
    def __init__(self, program_name):
        win = Tk()
        title_lbl = Label(win, text="EXPERIMENTS", font = ("", 17, "bold"))
        warning_lbl = Label(win, text="Please use with caution!\nThese features might not work properly yet...")
        adbDebug_lbl = Label(win, text="Android Debug Bridge:")
        adbIp_lbl = Label(win, text="IP:")
        adbIpEnter_txt = Entry(win)
        adbConnectDevice_btn = Button(win, text="Spawn ADB Term", command=lambda: self.adbSpawnTerm( adbIpEnter_txt.get() ))
        termOpenNew_btn = Button(win, text="Spawn Normal Term", command=lambda: term.TerminalWindow("Local Shell", None))
        title_lbl.grid(row=0, column=0, columnspan=3)
        warning_lbl.grid(row=1, column=0, columnspan=3)
        ttk.Separator(win, orient='horizontal').grid(row=2, column=0, sticky="ew", columnspan=4)
        adbDebug_lbl.grid(row=3, column=0)
        adbIp_lbl.grid(row=4, column=0)
        adbIpEnter_txt.grid(row=4, column=1)
        adbConnectDevice_btn.grid(row=5, column=1)
        termOpenNew_btn.grid(row=6, column=1)
        ttk.Separator(win, orient='horizontal').grid(row=8, column=0, sticky="ew", columnspan=4)
        win.title(f"{program_name} Experiments")
        win.mainloop()

    def adbSpawnTerm(self, ip):
        try:
            self.adbDevice = adb_wireless.adbSession(ip)
        except OSError:
            print("Failed To Connect")
        else:
            print(f"Connected: {self.adbDevice}")
            self.adbTerm = term.TerminalWindow("ADB", self.adbDevice)

    def adbRunCmd(self, cmd):
        print(f"RUN: {cmd}")
        print(self.adbDevice)
        self.adbDevice.sendCommand(cmd)