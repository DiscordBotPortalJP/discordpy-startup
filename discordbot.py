from flask import Flask, request
import discord
import os
import traceback
import threading
import asyncio

class Mariage:
    client = discord.Client()

    def run(self, token):
        self.client.run(token)
    
    def broadcast(self, message):
        print(request.get_data())
        for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(message), loop=self.client.loop)
    
    @client.event
    async def on_ready():
        print('Logged in as')
        #print(client.user.name)
        #print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        print(message.content)