from flask import Flask, request
from discordbot import Mariage
import os
import asyncio
import threading

app = Flask(__name__)
m = Mariage()

@app.route("/news/events", methods=['POST'])
def webhook():
    print(request.get_data())
    m.broadcast(request.get_data())

    return 'OK'

if __name__ == "__main__":
    t = threading.Thread(target=m.run, args=[os.environ['DISCORD_BOT_TOKEN']])
    t.start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)