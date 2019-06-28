from flask import Flask, request
import discord
import os
import traceback
import threading
import asyncio

client = discord.Client()
app = Flask(__name__)

def broadcast(message):
    for channel in filter(lambda x : x.type == discord.ChannelType.text, client.get_all_channels()):
        asyncio.ensure_future(channel.send(message), loop=client.loop)

@app.route("/news/events", methods=['POST'])
def webhook():
    print(request.get_data())
    broadcast(request.get_data())
    return 'OK'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    print(message.content)

port = int(os.environ.get("PORT", 5000))
#app.run(host='0.0.0.0', port=port)

t = threading.Thread(target=app.run, args=['0.0.0.0', port])
t.start()
client.run(os.environ['DISCORD_BOT_TOKEN'])