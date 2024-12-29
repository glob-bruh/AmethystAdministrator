"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
servicesManager - SERVICE MANAGEMENT TOOL CODE:
--------------------------------------------------
Contains functions for service manager window and
its related functions and sub-windows. 
--------------------------------------------------
"""

from tkinter import *
from tkinter import ttk

def serviceManagementWindowConstruct(x, ip2find):
    global arrayForThisSys
    print("serviceManager")
    arrayForThisSys = []
    for i in x:
        if i[0] == ip2find:
            arrayForThisSys = i
    if len(arrayForThisSys) != 0:
        print(arrayForThisSys)
        windowServiceMgr = Toplevel()
        services_tree = ttk.Treeview(windowServiceMgr, columns=["port", "username"])
        services_tree.heading("#0", text = "Name")
        services_tree.heading("port", text = "Port")
        services_tree.heading("username", text = "Username")
        addService_btn = Button(windowServiceMgr, text="Add Service", command=lambda: addServiceToHost())
        removeService_btn = Button(windowServiceMgr, text="Remove Service", command=lambda: removeServiceFromHost())
        modifyService_btn = Button(windowServiceMgr, text="Edit Service", command=lambda: modifyServiceFromHost())
        Grid.grid_rowconfigure(windowServiceMgr, index=0, weight=1)
        Grid.grid_columnconfigure(windowServiceMgr, index=0, weight=1)
        services_tree.grid(row = 0, column = 0, rowspan = 5, sticky="nsew")
        addService_btn.grid(row = 1, column = 1)
        removeService_btn.grid(row = 2, column = 1)
        modifyService_btn.grid(row = 3, column = 1)
        windowServiceMgr.title(f"{arrayForThisSys[0]} - Service Manager")
        for i in arrayForThisSys[4]:
            # .insert(<PARENT ITEM>, <POSITION/INDEX>)
            t1 = arrayForThisSys[4][i]
            t2 = PhotoImage(file = "resources/pic/icons/serviceGear.png")
            x3 = services_tree.insert(
                "", END, 
                text = i, 
                values = ( t1[0], t1[1] ),
                image = t2)
        windowServiceMgr.mainloop()

def addServiceToHost():
    windowAddServiceMgr = Tk()
    textBox1_label = Label(windowAddServiceMgr, text = "Service Name:")
    inputEntry1_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
    textBox2_label = Label(windowAddServiceMgr, text = "Ports (comma separated):")
    inputEntry2_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
    textBox3_label = Label(windowAddServiceMgr, text = "Username (optional):")
    inputEntry3_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
    textBox4_label = Label(windowAddServiceMgr, text = "Password (optional):")
    inputEntry4_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
    addServiceFinish_btn = Button(
        windowAddServiceMgr, text = "Add Service",
        command = lambda: addServiceAndCloseWindow(
            windowAddServiceMgr,
            inputEntry1_txtEnter.get(), 
            inputEntry2_txtEnter.get(),
            inputEntry3_txtEnter.get(),
            inputEntry4_txtEnter.get() ))
    textBox1_label.grid(row = 0, column = 0)
    textBox2_label.grid(row = 1, column = 0)
    textBox3_label.grid(row = 2, column = 0)
    textBox4_label.grid(row = 3, column = 0)
    inputEntry1_txtEnter.grid(row = 0, column = 1)
    inputEntry2_txtEnter.grid(row = 1, column = 1)
    inputEntry3_txtEnter.grid(row = 2, column = 1)
    inputEntry4_txtEnter.grid(row = 3, column = 1)
    addServiceFinish_btn.grid(row = 4, column = 0, columnspan = 2)
    windowAddServiceMgr.title("Add New Service")
    windowAddServiceMgr.mainloop()

def addServiceAndCloseWindow(win, name, ports, user, passwd):
    global arrayForThisSys
    arrayForThisSys[4][name] = [ports, user, passwd]
    win.destroy()