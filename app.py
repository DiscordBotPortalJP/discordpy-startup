from flask import Flask, request
from discordbot import Mariage
import os
import asyncio
import threading

class WebApp:
    app = Flask(__name__)

    def __init__(self, m):
        self.m = m
    
    @app.route("/news/events", methods=['POST'])
    def webhook():
        print(request.get_data())
        m.broadcast(request.get_data())

        return 'OK'
    
    def run(self):
        port = int(os.environ.get("PORT", 5000))
        self.app.run(host='0.0.0.0', port=port)

m = Mariage()
w = WebApp(m)

t = threading.Thread(target=w.run)

def main():
    t.start()
    m.run(os.environ['DISCORD_BOT_TOKEN'])

if __name__ == '__main__':
    main()