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

from tkinter import *
#from tkinter import colorchooser
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading as th
import random

import canvasController as cc
import servicesManager as svMgr
import networkVerify as netV

def addHost(c, deviceType_drp):
    global windowMain
    global hostArray
    global ipAddr_txt
    global hosts_tree
    x2 = ipAddr_txt.get()
    x = False
    for i in hostArray:
        if i[0] == x2:
            messagebox.showwarning(title = "Host Already Exists", message = f"Host with the IP address of \"{x2}\" already exists.")
            x = True
    if x == False:
        x4 = cc.deviceToImg(deviceType_drp.get())
        if x4 == "???":
            x4 = "wstn"
        t = cc.imgToDevice(x4)
        if netV.validateIPv4(x2) == True:
            x1 = cc.hostCanvas(hostArray, windowMain, c, x2, x4)
            x3 = hosts_tree.insert(
                "", END,
                text = x2,
                values = (t, 0, "Pinger not running", False))
            hostArray.append( [ x2, x4, x1, x3, {} ] )
        else:
            # https://docs.python.org/3/library/tkinter.messagebox.html
            messagebox.showwarning(title = "Not a Valid IPv4", message = f"The text \"{x2}\" is not a valid IPv4 address.")
    ipAddr_txt.delete(0, END)
    deviceType_drp.set("workstation")
    print(hostArray)

def removeHost():
    global hosts_tree
    global hostArray
    x = hosts_tree.focus()
    treeCurSel = hosts_tree.item(x)["text"]
    x = messagebox.askquestion(title = "Remove Host?", message = f"Are you sure you want to delete the host \"{treeCurSel}\"?")
    if x == "yes":
        i = 0
        for t in hostArray:
            if t[0] == treeCurSel:  break
            else:                   i += 1
        cc.removeHostFromCanvas(hostArray[i][2]) 
        hostArray.pop(i) # update treelist to match
        print(hostArray)

def initGui(win, tkDefWidth):
    global ipAddr_txt
    global hostType_drop_val
    global hosts_tree
    global addHost_btn # TESTING
    canvas = Canvas(win, width=500, height=500, bg="#171717")
    hosts_tree = ttk.Treeview(
        win, 
        columns=["deviceType", "numServ", "isOnline", "isControllable"])
    hosts_tree.heading("#0", text = "IP Address")
    hosts_tree.heading("deviceType", text = "Device Type")
    hosts_tree.heading("numServ", text = "Number of Services")
    hosts_tree.heading("isOnline", text = "Pingable")
    hosts_tree.heading("isControllable", text = "Controllable")
    ipAddr_lbl = Label(win, width = tkDefWidth, text = "IP Address:")
    ipAddr_txt = Entry(win, width = tkDefWidth, validate = 'key')
    hostType_drop_val = StringVar() 
    hostType_drop_val.set("Select Client Type") 
    hostType_drop = OptionMenu(
        win, hostType_drop_val,
        *[ "workstation", "server", "router" ])  
    addHost_btn = Button(win, width = tkDefWidth, text="Add Host", command=lambda: addHost(canvas, hostType_drop_val))
    removeHost_btn = Button(win, width = tkDefWidth, text="Remove Host", command=lambda: removeHost())
    Grid.grid_rowconfigure(win, index=0, weight=1)
    Grid.grid_columnconfigure(win, index=0, weight=1)
    canvas.grid(row = 0, column = 0, rowspan = 6, sticky="nsew")
    ipAddr_lbl.grid(row = 1, column = 1)
    ipAddr_txt.grid(row = 2, column = 1)
    hostType_drop.grid(row = 3, column = 1)
    addHost_btn.grid(row = 4, column = 1)
    removeHost_btn.grid(row = 5, column = 1)
    hosts_tree.grid(row = 6, column = 0, columnspan = 2, rowspan = 4, sticky="nsew")
    x = Image.open("resources/pic/logo/logoNormal.ico")
    pgrmLogo_ico = ImageTk.PhotoImage(x)
    win.wm_iconphoto(False, pgrmLogo_ico)
    win.title(f"{pgrmName}")

if __name__ == "__main__":
    global pgrmName  ; pgrmName = "Amethyst Administrator"
    global hostArray ; hostArray = []
    global windowMain
    windowMain = Tk()
    initGui(windowMain, 20)
    #################################
    # TESTING STUFF - Add clients automatically for testing.
    global addHost_btn # remember to remove this from initGui()
    ipAddr_txt.delete(0, END) ; ipAddr_txt.insert(0, "192.168.0.1") ; addHost_btn.invoke()
    ipAddr_txt.delete(0, END) ; ipAddr_txt.insert(0, "192.168.0.2") ; addHost_btn.invoke()
    ipAddr_txt.delete(0, END) ; ipAddr_txt.insert(0, "192.168.0.3") ; addHost_btn.invoke()
    #################################
    windowMain.mainloop()
