from tkinter import *
from tkinter import ttk

class deviceControlPanel:
    def __init__(self, titleNote):
        self.win = Tk()
        self.win.title(f"{titleNote} - Remote Administrator Tools")
        self.win.geometry("400x300")
        self.win.resizable(0, 0)
        notebook = ttk.Notebook(self.win)
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Processes")
        tab2 = ttk.Frame(notebook)
        notebook.add(tab2, text="Services")
        tab3 = ttk.Frame(notebook)
        notebook.add(tab3, text="Defensive")
        tab4 = ttk.Frame(notebook)
        notebook.add(tab4, text="Persistence")
        tab5 = ttk.Frame(notebook)
        notebook.add(tab5, text="Fun/PoC")
        tab6 = ttk.Frame(notebook)
        notebook.add(tab6, text="Destructive")
        tab7 = ttk.Frame(notebook)
        notebook.add(tab7, text="Spy")
        notebook.pack(expand=True, fill="both")
        self.win.mainloop()