"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
canvasController - CANVAS CONTROLLER FUNCTIONS:
--------------------------------------------------
Contains functions to manipulate the canvas
widget on the main window and its images.
--------------------------------------------------
"""

import random
import sys
from tkinter import *
from matplotlib import font_manager
from PIL import Image, ImageTk, ImageFont, ImageDraw

import network_pinger as netPing
import edit_host as eHost
from services import services_manager as svMgr
from services import services_processor as svProc
from modules.views.device_control_panel import deviceControlPanel as viewDCP


class hostCanvas():
    def __init__(self, parent, hArr, win, c, ip, src):
        # do note that the random number image ident will eventually cause collisions
        self.parent = parent
        self.win = win
        self.hostArr = hArr
        self.canvas = c
        self.ip = ip
        self.imgMoveData = {"x": 0, "y": 0, "item": None}
        i = f"image{random.randint(0, 9999999999)}"
        image = Image.open(f"resources/pic/downloaded/{src}.png")
        imgWidth, imgHeight = image.size
        self.imageAccess = Image.open(f"resources/pic/downloaded/accessBad.png")
        imgWidth2, imgHeight2 = self.imageAccess.size
        image.paste(self.imageAccess, (imgWidth - 40, imgHeight - 50), self.imageAccess)
        x = ImageDraw.Draw(image)
        file = findMonospaceFont()[1]
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(file, 14)
        # x.text((x, y),"Sample Text",(r,g,b))
        x.text((0, imgHeight - 15), ip, (125, 125, 125), font=font)
        image = ImageTk.PhotoImage(image)
        setattr(c, i, image)
        self.imgCanvasID = c.create_image(50, 50, image = getattr(c, i), tags = ("movable", i))
        c.tag_bind("movable", "<ButtonPress-1>", self.imgMoveStart)
        c.tag_bind("movable", "<ButtonRelease-1>", self.imgMoveStop)
        c.tag_bind(i, "<Button-3>", self.imgContextMenu)
        c.tag_bind("movable", "<B1-Motion>", self.imgMove)

    def imgMoveStart(self, event):
        self.imgMoveData["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self.imgMoveData["x"] = event.x
        self.imgMoveData["y"] = event.y

    def imgMoveStop(self, event):
        self.imgMoveData["item"] = None
        self.imgMoveData["x"] = 0
        self.imgMoveData["y"] = 0

    def imgMove(self, event):
        dX = event.x - self.imgMoveData["x"]
        dY = event.y - self.imgMoveData["y"]
        self.canvas.move(self.imgMoveData["item"], dX, dY)
        self.imgMoveData["x"] = event.x
        self.imgMoveData["y"] = event.y

    def imgContextMenu(self, event):
        contextMenu = Menu(self.win, tearoff=0)
        for i in self.hostArr:
            if i[0] == self.ip:
                match i[1][1]:
                    case "ip": 
                        contextMenu.add_command(label=f"IP Address: {self.ip}", command=lambda: eHost.EditHostWindow(self.parent, self.hostArr, self.ip))
                        contextMenu.add_separator()
                        #contextMenu.add_command(label="Connect via Terminal", command=lambda: svProc.AndroidDebugBridge(self.ip))
                        contextMenu.add_command(label="Connect via Terminal", command=lambda: svProc.determineService(self.hostArr, self.ip))
                        contextMenu.add_command(label="Connect via Remote Desktop")
                        contextMenu.add_command(label="Remote Administration Tools", command=lambda: viewDCP(self.win))
                        contextMenu.add_separator()
                        contextMenu.add_command(label="Auto-ping: OFF", command=lambda: netPing.pinger(self.ip))
                        contextMenu.add_separator()
                        contextMenu.add_command(label="Service Manager", command=lambda: svMgr.ServiceManagementWindow(self.hostArr, self.ip, 15))
                        contextMenu.add_command(label="Browse Files")
                    case "cloud":
                        contextMenu.add_command(label=f"Cloud ID: {self.ip}", command=lambda: eHost.EditHostWindow(self.parent, self.hostArr, self.ip))
                        contextMenu.add_separator()
                        contextMenu.add_command(label="Connect to Cloud", command=lambda: print("no cloud yet."))
                        contextMenu.add_command(label="Manage Cloud", command=lambda: print("no cloud to manage yet."))
        contextMenu.add_separator()
        contextMenu.add_command(label = "Close Menu")
        contextMenu.tk_popup(event.x_root, event.y_root)

def removeHostFromCanvas(host):
    host.canvas.delete(host.imgCanvasID)

def findMonospaceFont():
    match sys.platform:
        case "linux":  x = "hack"
        case "win32":  x = "consolas"
        case "darwin": x = "sf mono"
        case _:        x = "sans serif"
    return [x, font_manager.findfont(x)]