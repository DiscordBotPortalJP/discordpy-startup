from flask import Flask, request
import discord
import os
import traceback
import threading
import asyncio

app = Flask(__name__)

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

def startHook():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#@app.route("/", methods=['POST'])
@app.route("/news/events", methods=['POST'])
def webhook():
    print(request.get_data())
    for channel in filter(lambda x : x.type == discord.ChannelType.text, client.get_all_channels()):
        asyncio.ensure_future(channel.send(request.get_data()), loop=client.loop) 

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

t = threading.Thread(target=startHook)

t.start()
client.run(token)
