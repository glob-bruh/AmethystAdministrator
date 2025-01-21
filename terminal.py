"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
terminal - TKINTER TERMINAL FUNCTIONS:
--------------------------------------------------
fill me in
--------------------------------------------------
"""

import os
from tkinter import *
from tkinter import ttk

import canvas_controller as cc

class TerminalWindow:
    def __init__(self):
        win = Tk()
        cmdOut_frm = Frame(win, width=500, height=500)
        x = cc.findMonospaceFont()[0]
        self.cmdOut_lbl = Label(cmdOut_frm, text="Welcome", justify="left", bg="black", fg="white", font=x)
        #cmdOut_scl = Scrollbar(cmdOut_frm, orient='horizontal', command=self.cmdOut_lbl.xview)
        cmdEnter_txt = Entry(win, validate="key")
        cmdSend_btn = Button(win, text="\u23CE", command=lambda: self.execCmdShowOut( cmdEnter_txt.get() ))
        cmdCloseWindow_btn = Button(win, text="Exit", command=lambda: self.closeTerminal(win))
        cmdEditTerm_btn = Button(win, text="Personalize", command=lambda: self.editTerminal())
        cmdOut_frm.grid(row=0, column=0, columnspan=2)
        self.cmdOut_lbl.grid(row=0, column=0)
        cmdEnter_txt.grid(row=2, column=0)
        cmdSend_btn.grid(row=2, column=1)
        cmdCloseWindow_btn.grid(row=3, column=0)
        cmdEditTerm_btn.grid(row=3, column=1)
        win.title("Terminal Window")
        win.mainloop()

    def execCmdShowOut(self, command):
        result = os.popen(command).read()
        self.cmdOut_lbl.config(text=result)

    def editTerminal(self):
        print("Nothing here")

    def closeTerminal(self, win):
        win.destroy()