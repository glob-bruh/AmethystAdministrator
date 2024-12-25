from tkinter import *
import random
from PIL import Image, ImageTk

class hostCanvas():
    def __init__(self, c, src):
        print("mesa host")
        self.canvas = c
        self.imgMoveData = {"x": 0, "y": 0, "item": None}
        i = f"image{random.randint(0, 9999999999)}"
        image = ImageTk.PhotoImage(Image.open(f"pic/{src}.png"))
        setattr(c, i, image)
        c.create_image(50, 50, image = getattr(c, i), tags = ("movable"))
        c.tag_bind("movable", "<ButtonPress-1>", self.imgMoveStart)
        c.tag_bind("movable", "<ButtonRelease-1>", self.imgMoveStop)
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