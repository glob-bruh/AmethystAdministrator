from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageTk
import threading as th
import random

def addHost():
    global hostArray
    global ipAddr_txt
    global hosts_tree
    hostArray.append( [ ipAddr_txt.get() ] )
    hosts_tree.insert('', 0, 'gallery', text = hostArray[0])
    ipAddr_txt.delete(0, END)

def removeHost():
    print("test")

##################################################
# [ REDACTED - PRIVATE IMAGE MANIPULATION CODE ] #
##################################################

def initGui(tkDefaultWidth):
    global windowMain
    global ipAddr_txt
    global hosts_tree
    windowMain = Tk()
    canvas = Canvas(
        windowMain, 
        width=500, 
        height=500, 
        bg="#00FF00")
    hosts_tree = ttk.Treeview(
        windowMain, 
        columns=('size', 'modified'))
    ipAddr_txt = Entry(
        windowMain,
        width = tkDefaultWidth,
        validate = 'key',)
    addHost_btn = Button(
        windowMain,
        width = tkDefaultWidth,
        text="Add Host",
        command=lambda: addHost())
    removeHost_btn = Button(
        windowMain,
        width = tkDefaultWidth,
        text="Remove Host",
        command=lambda: removeHost())
    canvas.grid(row = 1, column = 0, rowspan = 4)
    ipAddr_txt.grid(row = 1, column = 1)
    addHost_btn.grid(row = 2, column = 1)
    removeHost_btn.grid(row = 3, column = 1)
    hosts_tree.grid(row = 5, column = 0, columnspan = 2)
    addImage(canvas, "wrkStn", "n", 250, 250)
    windowMain.title(f"{pgrmName}")

global pgrmName  ; pgrmName = "Armtiage Bootleg"
global hostArray ; hostArray = []
initGui(20)
windowMain.mainloop()
