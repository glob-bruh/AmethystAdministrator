"""
--------------------------------------------------
AMETHYST ADMINISTRATOR
https://github.com/glob-bruh/AmethystAdministrator
All content licensed under BSD-3
--------------------------------------------------
cloud_manager - CLOUD CONTROLLER FUNCTIONS:
--------------------------------------------------
Contains functions to control cloud environments, 
primarily M365.
--------------------------------------------------
"""

import os
import json
import asyncio
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from msgraph import GraphServiceClient
from azure.identity import InteractiveBrowserCredential

class MicrosoftGraphAPIClass:
    def __init__(self, program_name, domain):
        # self.authenticated = False
        # self.authenticate()
        credential = InteractiveBrowserCredential(tenant_id=domain)
        scopes = ['https://graph.microsoft.com/.default']
        self.client = GraphServiceClient(credentials=credential, scopes=scopes)
        self.authenticated = True

        if self.authenticated == True:
            x = asyncio.run(self.get_users())
        self.gui(x)
        self.win.mainloop()

    def get_orgID(self):
        async def func(): await self.client.users.get()
        asyncio.run(func())

    async def get_users(self):
        returnArr = []
        users = await self.client.users.get()
        if users and users.value:
            for user in users.value:
                returnArr.append([user.user_principal_name, user.display_name, user.id])
        print(returnArr)
        return returnArr

    def authenticate(self):
        if self.authenticated == False:
            x = json.load(open("GAPI-SECRET.json"))["DOMAIN"]
            print(x)
            try:
                credential = InteractiveBrowserCredential(tenant_id=x)
                scopes = ['https://graph.microsoft.com/.default']
                self.client = GraphServiceClient(credentials=credential, scopes=scopes)
                print(self.get_orgID())
                self.authenticated = True
                print("All Good")
            except Exception as e:
                print(e)
                print("Authentication Failed")

    def gui(self, x):
        self.win = Tk()
        self.hosts_tree = ttk.Treeview(
            self.win,
            columns=["name", "id"])
        self.hosts_tree.heading("#0", text="UPN")
        self.hosts_tree.heading("name", text="Name")
        self.hosts_tree.heading("id", text="ID")
        for i in x:
            self.hosts_tree.insert(
                "", END,
                text = i[0],
                values = (i[1], i[2]))
        self.hosts_tree.grid(row=0, column=0)