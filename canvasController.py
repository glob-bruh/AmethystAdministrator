from tkinter import *
import random
import sys
from matplotlib import font_manager
from PIL import Image, ImageTk, ImageFont, ImageDraw
import servicesManager as svMgr


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
        delta_x = event.x - self.imgMoveData["x"]
        delta_y = event.y - self.imgMoveData["y"]
        self.canvas.move(self.imgMoveData["item"], delta_x, delta_y)
        self.imgMoveData["x"] = event.x
        self.imgMoveData["y"] = event.y

    def imgContextMenu(self, event):
        contextMenu = Menu(self.win, tearoff=0)
        contextMenu.add_command( label = "Connect To System" )
        contextMenu.add_command( label = "Service Manager", command =  lambda: svMgr.serviceManagementWindowConstruct(self.hostArr, self.ip) )
        contextMenu.add_command( label = "Browse Files")
        contextMenu.add_separator()
        contextMenu.add_command( label = "Close Menu" )
        contextMenu.tk_popup(event.x_root, event.y_root) 
        print("Context Menu")

def deviceToImg(device):
    match device:
        case "workstation":
            return "wstn"
        case "server":
            return "srvr"
        case "router":
            return "rter"
        case _:
            return "???"