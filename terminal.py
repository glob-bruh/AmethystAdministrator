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
    def __init__(self, titleNote):
        win = Tk()
        x = cc.findMonospaceFont()[0]
        #cmdVert_scl = Scrollbar(cmdOut_frm, orient="vertical")
        self.cmdOut_lbl = Text(win, font=x, bg="black", fg="white")
        self.cmdOut_lbl.insert(END, "\nWelcome to Amethyst Admin Terminal (AAT).\n")
        self.cmdOut_lbl.configure(state="disabled")
        cmdEditTerm_btn = Button(win, text="Personalize", width=10, command=lambda: self.editTerminal())
        cmdClearTerm_btn = Button(win, text="Clear", width=10, command=lambda: self.clearTerminal())
        cmdCloseWindow_btn = Button(win, text="Exit", width=10, command=lambda: self.closeTerminal(win))
        cmdEnter_txt = Entry(win, font=x)
        cmdSend_btn = Button(win, text="\u23CE", command=lambda: self.execCmdShowOut(cmdEnter_txt.get()))
        Grid.grid_rowconfigure(win, index=0, weight=1)
        Grid.grid_columnconfigure(win, index=0, weight=1)
        self.cmdOut_lbl.grid(row=0, column=0, rowspan=6, columnspan=2, sticky="nsew")
        cmdEditTerm_btn.grid(row=4, column=2)
        cmdClearTerm_btn.grid(row=5, column=2)
        cmdCloseWindow_btn.grid(row=6, column=2)
        cmdEnter_txt.grid(row=6, column=0, sticky="nsew")
        cmdSend_btn.grid(row=6, column=1)
        win.title(f"{titleNote} - Terminal Window")
        win.mainloop()

    def execCmdShowOut(self, command):
        #result = os.popen(f"{command} 2>&1").read() <-- NOT CROSS PLATFORM
        result = os.popen(command).read()
        self.cmdOut_lbl.configure(state="normal")
        self.cmdOut_lbl.insert(END, f"\n>>> {command}\n{result}")
        self.cmdOut_lbl.configure(state="disabled")
        self.cmdOut_lbl.see(END)

    def clearTerminal(self):
        self.cmdOut_lbl.configure(state="normal")
        self.cmdOut_lbl.delete(1.0, END)
        self.cmdOut_lbl.insert(END, "\nTerminal output cleared!\n")
        self.cmdOut_lbl.configure(state="disabled")

    def editTerminal(self):
        print("Nothing here")

    def closeTerminal(self, win):
        win.destroy()