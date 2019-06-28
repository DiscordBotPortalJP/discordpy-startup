from flask import Flask, request
import discord
import os
import traceback
import threading
import asyncio

def run(token):
    m = Mariage()
    m.run(token)

class Mariage:
    client = discord.Client()

    def run(self, token):
        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

        @self.client.event
        async def on_message(message):
            print(message.content)
        
        self.client.run(token)
    
    def broadcast(self, message):
        print(request.get_data())
        for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(message), loop=self.client.loop)
    
