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

def worker(ws, token, loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(ws.run(token))

loop = asyncio.new_event_loop()
p = threading.Thread(target=worker, args=(m, os.environ['DISCORD_BOT_TOKEN'], loop,))
p.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)