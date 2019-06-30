from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from discordbot import Mariage
import discord
import discordbot
import bs4
import os
import asyncio
import threading
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
m = Mariage(app)

@app.route("/alive", methods=['GET'])
def alive():
    return "OK"

@app.route("/news/events", methods=['POST'])
def webhook():
    print(request.json)
   
    soup = bs4.BeautifulSoup(request.json['content'], "html.parser")
    embeds=[]
    for h2 in soup.find_all("h2", id=re.compile("^detail_")):
        print(h2)
        
        description=""
        for p in filter(lambda e : e.name=="p", findConntents(h2, lambda x : x.name != "h2" and x.name != "h3")):
            description += p.text
        embed = discord.Embed(
            title=h2.text,
            url=request.json['url'],
            description=description)
        embed.set_author(
            name=request.json['feedTitle'],
            url=request.json['feedUrl'],
            icon_url=request.json['author'])
        for img in filter(lambda e : e.name=="img", findConntents(h2, lambda x : x.name != "h2" and x.name != "h3")):
            embed.set_image(url=img.attrs["src"])
            break
        embeds.append(embed)
    m.sendNews(embeds)

    return 'OK'

def findConntents(elm, pre):
    for nx in elm.find_all_next():
        if (pre(nx)):
            yield nx
        else:
            break

thread = threading.Thread(target=m.run, args=(os.environ['DISCORD_BOT_TOKEN'],))
thread.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)