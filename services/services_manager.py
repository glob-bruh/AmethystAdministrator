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
from tkinter import messagebox

class ServiceManagementWindow:
    def __init__(self, x, ip2find, tkDefWidth):
        self.window_serviceManage = Tk()
        self.hostArray = x
        self.ipAddress = ip2find
        self.arrayForThisSys =  []
        self.defaultWidth = tkDefWidth
        print("serviceManager")
        for i in x:
            if i[0] == ip2find:
                self.arrayForThisSys = i
        if len(self.arrayForThisSys) != 0:
            print(self.arrayForThisSys)
            winHead_lbl = Label(self.window_serviceManage, text = f"SERVICES FOR {ip2find}", font=("", 17, "bold"))
            self.services_tree = ttk.Treeview(self.window_serviceManage, columns=["port", "username"])
            self.services_tree.heading("#0", text = "Name")
            self.services_tree.heading("port", text = "Port")
            self.services_tree.heading("username", text = "Username")
            addService_btn = Button(self.window_serviceManage, text="Add Service", width = self.defaultWidth, command=lambda: ServiceManagementAddServiceWindow(self))
            removeService_btn = Button(self.window_serviceManage, text="Remove Service", width = self.defaultWidth, command=lambda: self.removeServiceFromHost())
            modifyService_btn = Button(self.window_serviceManage, text="Edit Service", width = self.defaultWidth, command=lambda: ServiceManagementEditServiceWindow(self))
            Grid.grid_rowconfigure(self.window_serviceManage, index=0, weight=1)
            Grid.grid_columnconfigure(self.window_serviceManage, index=0, weight=1)
            winHead_lbl.grid(row=0, column=0, columnspan=5)
            self.services_tree.grid(row = 1, column = 0, rowspan = 5, sticky="nsew")
            addService_btn.grid(row = 2, column = 1)
            removeService_btn.grid(row = 3, column = 1)
            modifyService_btn.grid(row = 4, column = 1)
            self.window_serviceManage.title(f"Service Manager - {self.arrayForThisSys[0]}")
            for i in self.arrayForThisSys[4]:
                # .insert(<PARENT ITEM>, <POSITION/INDEX>)
                t1 = self.arrayForThisSys[4][i]
                t2 = PhotoImage(file = "resources/pic/icons/serviceGear.png")
                #x3 = self.services_tree.insert(
                #    "", END, 
                #    text = i, 
                #    values = ( t1[0], t1[1] ),
                #    image = t2)
                x3 = self.services_tree.insert(
                    "", END, 
                    text = i, 
                    values = ( t1[0], t1[1] ))
            self.window_serviceManage.mainloop()
        
    def removeServiceFromHost(self):
        serviceCurSel = self.services_tree.item( self.services_tree.focus() )["text"]
        self.window_serviceManage.withdraw()
        x = messagebox.askquestion(title = "Remove Host?", message = f"Are you sure you want to delete the host \"{serviceCurSel}\"?")
        self.window_serviceManage.deiconify()
        if x == "yes" and serviceCurSel != "":
            self.services_tree.delete( self.services_tree.selection()[0] )
            del self.arrayForThisSys[4][serviceCurSel]

class ServiceManagementAddServiceWindow:
    def __init__(self, parent):
        windowAddServiceMgr = Tk()
        winHead_lbl = Label(windowAddServiceMgr, text = f"ADD NEW SERVICE", font=("", 17, "bold"))
        textBox1_label = Label(windowAddServiceMgr, text = "Service Name:")
        inputEntry1_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
        textBox2_label = Label(windowAddServiceMgr, text = "Ports (comma separated):")
        inputEntry2_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
        textBox3_label = Label(windowAddServiceMgr, text = "Username (optional):")
        inputEntry3_txtEnter = Entry(windowAddServiceMgr, validate = 'key')
        textBox4_label = Label(windowAddServiceMgr, text = "Password (optional):")
        inputEntry4_txtEnter = Entry(windowAddServiceMgr, show = "*", validate = 'key')
        addServiceFinish_btn = Button(
            windowAddServiceMgr, text = "Add Service",
            command = lambda: self.addServiceAndCloseWindow(
                parent,
                inputEntry1_txtEnter.get(), 
                inputEntry2_txtEnter.get(),
                inputEntry3_txtEnter.get(),
                inputEntry4_txtEnter.get() ))
        winHead_lbl.grid(row=0, column=0, columnspan=2)
        textBox1_label.grid(row=1, column=0)
        textBox2_label.grid(row=2, column=0)
        textBox3_label.grid(row=3, column=0)
        textBox4_label.grid(row=4, column=0)
        inputEntry1_txtEnter.grid(row=1, column=1)
        inputEntry2_txtEnter.grid(row=2, column=1)
        inputEntry3_txtEnter.grid(row=3, column=1)
        inputEntry4_txtEnter.grid(row=4, column=1)
        addServiceFinish_btn.grid(row=5, column=0, columnspan=2)
        windowAddServiceMgr.title("Add New Service")
        windowAddServiceMgr.mainloop()

    def addServiceAndCloseWindow(self, parent, name, ports, user, passwd):
        parent.arrayForThisSys[4][name] = [ports, user, passwd]
        #x = parent.services_tree.insert(
        #    "", END, 
        #    text = name, 
        #    values = ( ports, user ),
        #    image = PhotoImage(file = "resources/pic/icons/serviceGear.png"))
        x = parent.services_tree.insert(
            "", END, 
            text = name, 
            values = ( ports, user ))


class ServiceManagementEditServiceWindow:
    def __init__(self, parent):
        print("nothing yet")