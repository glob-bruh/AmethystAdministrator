from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageTk
import threading as th
import random

import canvasController as cc
import servicesManager as svMgr

def addHost(c):
    global windowMain
    global hostArray
    global ipAddr_txt
    global hostType_drop_val
    global hosts_tree
    x4 = cc.deviceToImg(hostType_drop_val.get())
    if x4 == "???":
        x4 = "wstn"
    x2 = ipAddr_txt.get()
    x1 = cc.hostCanvas(hostArray, windowMain, c, x2, x4)
    x3 = hosts_tree.insert(
        "", END,
        text = x2,
        values=(0, 0, 0, 0)) # get these working!
    hostArray.append( [ x2, x4, x1, x3, [] ] )
    ipAddr_txt.delete(0, END)
    hostType_drop_val.set("workstation")
    print(hostArray)

def removeHost():
    print("test")

def initGui(win, tkDefWidth):
    global ipAddr_txt
    global hostType_drop_val
    global hosts_tree
    canvas = Canvas(
        win, 
        width=500, 
        height=500, 
        bg="#171717")
    hosts_tree = ttk.Treeview(
        win, 
        columns=["deviceType", "numServ", "isOnline", "isControllable"])
    hosts_tree.heading("#0", text = "IP Address")
    hosts_tree.heading("deviceType", text = "Device Type")
    hosts_tree.heading("numServ", text = "Number of Services")
    hosts_tree.heading("isOnline", text = "Pingable")
    hosts_tree.heading("isControllable", text = "Controllable")
    ipAddr_txt = Entry(
        win,
        width = tkDefWidth,
        validate = 'key',)
    hostType_drop_val = StringVar() 
    hostType_drop_val.set("Select Client Type") 
    hostType_drop = OptionMenu(
        win,
        hostType_drop_val,
        *[ "workstation", "server", "router" ])  
    addHost_btn = Button(
        win,
        width = tkDefWidth,
        text="Add Host",
        command=lambda: addHost(canvas))
    removeHost_btn = Button(
        win,
        width = tkDefWidth,
        text="Remove Host",
        command=lambda: removeHost())
    Grid.grid_rowconfigure(win, index=0, weight=1)
    Grid.grid_columnconfigure(win, index=0, weight=1)
    canvas.grid(row = 0, column = 0, rowspan = 5, sticky="nsew")
    ipAddr_txt.grid(row = 1, column = 1)
    hostType_drop.grid(row = 2, column = 1)
    addHost_btn.grid(row = 3, column = 1)
    removeHost_btn.grid(row = 4, column = 1)
    hosts_tree.grid(row = 5, column = 0, columnspan = 2, rowspan = 4, sticky="nsew")
    win.title(f"{pgrmName}")

if __name__ == "__main__":
    global pgrmName  ; pgrmName = "Armtiage Bootleg"
    global hostArray ; hostArray = []
    global windowMain
    windowMain = Tk()
    initGui(windowMain, 20)
    windowMain.mainloop()
