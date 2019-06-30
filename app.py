from flask import Flask, request
from discordbot import Mariage
import discord
import bs4
import os
import asyncio
import threading

app = Flask(__name__)
m = Mariage()

@app.route("/news/events", methods=['POST'])
def webhook():
    print(request.json)
    embed = discord.Embed(
        title=request.json['feedTitle'],
        url=request.json['url'])
    embed.set_author(name=request.json['title'])
    embed.set_image(url=request.json['imageUrl'])
    soup = bs4.BeautifulSoup(request.json['content'], "html.parser")
    embed.add_field(name="おしらせ１", value=soup.div.text[0:1024])
    m.broadcastEmbed(embed)

    return 'OK'

thread = threading.Thread(target=m.run, args=(os.environ['DISCORD_BOT_TOKEN'],))
thread.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)