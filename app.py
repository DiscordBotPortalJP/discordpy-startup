from flask import Flask, request
import os
import asyncio
import threading

app = Flask(__name__)

def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

@app.route("/news/events", methods=['POST'])
def webhook():
    print(request.get_data())
    m.broadcast(request.get_data())

    return 'OK'