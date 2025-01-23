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
from devices.android import adb_wireless

class TerminalWindow:
    def __init__(self, titleNote, s):
        def enterKeyPressed(x): self.execCmdShowOut(cmdEnter_txt.get())
        if not s:
            self.currentService = LocalShellService()
        else:
            self.currentService = s
        x = cc.findMonospaceFont()[0]
        self.win = Tk()
        #cmdVert_scl = Scrollbar(cmdOut_frm, orient="vertical")
        self.cmdOut_lbl = Text(self.win, font=x, bg="black", fg="white")
        self.cmdOut_lbl.insert(END, "\nWelcome to Amethyst Admin Terminal (AAT).\n")
        self.cmdOut_lbl.configure(state="disabled")
        cmdExportOut_btn = Button(self.win, text="Export", width=10, command=lambda: self.exportOutput())
        cmdEditTerm_btn = Button(self.win, text="Personalize", width=10, command=lambda: self.editTerminal())
        cmdClearTerm_btn = Button(self.win, text="Clear", width=10, command=lambda: self.clearTerminal())
        cmdCloseWindow_btn = Button(self.win, text="Exit", width=10, command=lambda: self.closeTerminal())
        cmdEnter_txt = Entry(self.win, font=x)
        cmdSend_btn = Button(self.win, text="\u23CE", command=lambda: self.execCmdShowOut(cmdEnter_txt.get()))
        cmdEnter_txt.bind("<Return>", enterKeyPressed)
        Grid.grid_rowconfigure(self.win, index=0, weight=1)
        Grid.grid_columnconfigure(self.win, index=0, weight=1)
        self.cmdOut_lbl.grid(row=0, column=0, rowspan=6, columnspan=2, sticky="nsew")
        cmdExportOut_btn.grid(row=3, column=2)
        cmdEditTerm_btn.grid(row=4, column=2)
        cmdClearTerm_btn.grid(row=5, column=2)
        cmdCloseWindow_btn.grid(row=6, column=2)
        cmdEnter_txt.grid(row=6, column=0, sticky="nsew")
        cmdSend_btn.grid(row=6, column=1)
        self.win.title(f"{titleNote} - Terminal Window")
        self.win.mainloop()

    def execCmdShowOut(self, command):
        self.cmdOut_lbl.configure(state="normal")
        self.cmdOut_lbl.insert(END, f"\n>>> {command}")
        self.cmdOut_lbl.configure(state="disabled")
        try:
            x = self.currentService.sendCommand(command)
        except Exception as e:
            self.cmdOut_lbl.configure(state="normal")
            self.cmdOut_lbl.insert(END, f"\nCommand failed to run!\n{str(e)}\n")
            self.cmdOut_lbl.configure(state="disabled")
            self.cmdOut_lbl.see(END)
        else:
            self.cmdOut_lbl.configure(state="normal")
            self.cmdOut_lbl.insert(END, f"\n{x}")
            self.cmdOut_lbl.configure(state="disabled")
            self.cmdOut_lbl.see(END)

    def exportOutput(self):
        print("nothing yet")

    def clearTerminal(self):
        self.cmdOut_lbl.configure(state="normal")
        self.cmdOut_lbl.delete(1.0, END)
        self.cmdOut_lbl.insert(END, "\nTerminal output cleared!\n")
        self.cmdOut_lbl.configure(state="disabled")

    def editTerminal(self):
        print("Nothing here")

    def closeTerminal(self):
        self.win.destroy()


class LocalShellService:
    def sendCommand(parent, command):
        return os.popen(command).read()