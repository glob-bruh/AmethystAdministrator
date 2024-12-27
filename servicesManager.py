from tkinter import *
from tkinter import ttk

def serviceManagementWindowConstruct(x, ip2find):
    print("serviceManager")
    arrayForThisSys = []
    for i in x:
        if i[0] == ip2find:
            arrayForThisSys = i
    if len(arrayForThisSys) != 0:
        arrayForThisSys[4] = {
            "ssh": ["22", "testUser", "P@55W0rd"]
        } # THIS IS FOR TESTING = Port has to be str for things that use multiple ports (so they can be declared as "various")
        print(arrayForThisSys)
        windowServiceMgr = Toplevel()
        services_tree = ttk.Treeview(
            windowServiceMgr,
            columns=["port", "username"])
        services_tree.heading("#0", text = "Name")
        services_tree.heading("port", text = "Port")
        services_tree.heading("username", text = "Username")
        addService_btn = Button(
            windowServiceMgr,
            text="Add Service",
            command=lambda: addServiceToHost())
        removeService_btn = Button(
            windowServiceMgr,
            text="Remove Service",
            command=lambda: removeServiceFromHost())
        modifyService_btn = Button(
            windowServiceMgr,
            text="Edit Service",
            command=lambda: modifyServiceFromHost())
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