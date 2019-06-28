from flask import Flask, request
from discordbot import Mariage
import os
import asyncio
import threading

app = Flask(__name__)
m = Mariage()

@app.route("/news/events", methods=['POST'])
def webhook():
    m.broadcast(request.get_data())

    return 'OK'

async def start():
    await m.run(os.environ['DISCORD_BOT_TOKEN']) # use client.start instead of client.run

def run_it_forever(loop):
    loop.run_forever()

#asyncio.get_child_watcher() # I still don't know if I need this method. It works without it.

loop = asyncio.get_event_loop()
loop.create_task(start())

thread = threading.Thread(target=run_it_forever, args=(loop,))
thread.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)