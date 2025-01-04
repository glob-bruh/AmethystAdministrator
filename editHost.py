"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
editHost - CLASSES FOR THE "EDIT HOST" WINDOW:
--------------------------------------------------
Contains functions needed to allow for editing
hosts already present in the program.
--------------------------------------------------
"""

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from textwrap import dedent
import threading as th
import random

import canvasController as cc
import networkVerify as netV

class EditHostWindow:
    def __init__(self, hArr, ip):
        self.win = Tk()
        self.win.title(f"Edit Host - {ip}")
        print("Test")