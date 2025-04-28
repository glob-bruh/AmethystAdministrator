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
from msgraph import GraphServiceClient
from azure.identity import InteractiveBrowserCredential

class MicrosoftGraphAPIClass:
    def get_orgID(self):
        async def func(): await self.client.users.get()
        asyncio.run(func())

    async def get_users(self):
        users = await self.client.users.get()
        if users and users.value:
            for user in users.value:
                print(user.id, user.display_name, user.mail)

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

    def __init__(self, program_name):
        self.authenticated = False
        self.authenticate()
        #asyncio.run(self.get_users())
        print("reached the end")
