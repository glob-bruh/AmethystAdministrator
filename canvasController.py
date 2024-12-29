"""
-------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmthystAdministrator
All content licensed under BSD-3
-------------------------------------------------
canvasController - CANVAS CONTROLLER FUNCTIONS:
-------------------------------------------------
Contains functions to manipulate the canvas
widget on the main window and its images.
-------------------------------------------------
"""

from tkinter import *
import random
import sys
from matplotlib import font_manager
from PIL import Image, ImageTk, ImageFont, ImageDraw

import main as m
import servicesManager as svMgr
import networkPinger as netPing

class hostCanvas():
    def __init__(self, hArr, win, c, ip, src):
        self.win = win
        self.hostArr = hArr
        self.canvas = c
        self.ip = ip
        self.imgMoveData = {"x": 0, "y": 0, "item": None}
        i = f"image{random.randint(0, 9999999999)}"
        image = Image.open(f"resources/pic/devicePic/{src}.png")
        imgWidth, imgHeight = image.size
        x = ImageDraw.Draw(image)
        match sys.platform:
            case "linux":   file = font_manager.findfont("hack")
            case "windows": file = font_manager.findfont("consolas")
            case "mac":     file = font_manager.findfont("sf mono")
            case _:         file = font_manager.findfont("sans serif")
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(file, 20)
        # x.text((x, y),"Sample Text",(r,g,b))
        x.text((0, imgHeight - 25), ip, (255,255,255), font = font)
        image = ImageTk.PhotoImage(image)
        setattr(c, i, image)
        c.create_image(50, 50, image = getattr(c, i), tags = ("movable"))
        c.tag_bind("movable", "<ButtonPress-1>", self.imgMoveStart)
        c.tag_bind("movable", "<ButtonRelease-1>", self.imgMoveStop)
        c.tag_bind("movable", "<Button-3>", self.imgContextMenu)
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
        contextMenu.add_command( label = "Connect via Terminal" )
        contextMenu.add_command( label = "Connect via Remote Desktop" )
        contextMenu.add_command( label = "Remote Administration Tools" )
        contextMenu.add_separator()
        contextMenu.add_command( label = "Auto-ping: OFF", command = lambda: netPing.pinger(self.ip) )
        contextMenu.add_separator()
        contextMenu.add_command( label = "Service Manager", command =  lambda: svMgr.serviceManagementWindowConstruct(self.hostArr, self.ip) )
        contextMenu.add_command( label = "Browse Files")
        contextMenu.add_separator()
        contextMenu.add_command( label = "Close Menu" )
        contextMenu.tk_popup(event.x_root, event.y_root)


def genImgDeviceLookup():
    return [
        ["workstation", "wstn"],
        ["server", "srvr"],
        ["router", "rter"]
    ]

def imgToDevice(img):
    x = genImgDeviceLookup()
    for i in x:
        if i[1] == img:
            return i[0]
    return "???"

def deviceToImg(device):
    x = genImgDeviceLookup()
    for i in x:
        if i[0] == device:
            return i[1]
    return "???"
