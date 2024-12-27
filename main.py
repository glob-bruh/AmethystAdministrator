from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageTk
import threading as th
import random

import canvasController as cc

def addHost(c):
    global hostArray
    global ipAddr_txt
    global hostType_drop_val
    global hosts_tree
    x4 = cc.deviceToImg(hostType_drop_val.get())
    if x4 == "???":
        hostType_drop_val.set("workstation")
        x4 = "wrkStn"
    x2 = ipAddr_txt.get()
    x1 = cc.hostCanvas(c, x2, x4)
    x3 = hosts_tree.insert('', 'end', text = x2)
    hostArray.append( [x2, hostType_drop_val.get(), x1, x3] )
    ipAddr_txt.delete(0, END)
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
        bg="#6b6b6b")
    hosts_tree = ttk.Treeview(
        win, 
        columns=('size', 'modified'))
    ipAddr_txt = Entry(
        win,
        width = tkDefWidth,
        validate = 'key',)
    hostType_drop_val = StringVar() 
    hostType_drop_val.set( "Select Client Type" ) 
    hostType_drop = OptionMenu(
        win,
        hostType_drop_val,
        *[ "workstation", "server" ])  
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
    canvas.grid(row = 1, column = 0, rowspan = 4)
    ipAddr_txt.grid(row = 1, column = 1)
    hostType_drop.grid(row = 2, column = 1)
    addHost_btn.grid(row = 3, column = 1)
    removeHost_btn.grid(row = 4, column = 1)
    hosts_tree.grid(row = 5, column = 0, columnspan = 2)
    win.title(f"{pgrmName}")

global pgrmName  ; pgrmName = "Armtiage Bootleg"
global hostArray ; hostArray = []
windowMain = Tk()
initGui(windowMain, 20)
windowMain.mainloop()
