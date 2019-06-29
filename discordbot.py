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
    client = None

    def run(self, token):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = discord.Client()
        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

        @self.client.event
        async def on_message(message):
            print(message.content)
        
        asyncio.ensure_future(self.client.start(token))
        loop.run_forever()
    
    def broadcast(self, message):
        print(request.get_data())
        for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(message), loop=self.client.loop)
    
