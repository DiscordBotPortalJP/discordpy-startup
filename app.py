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
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
m = Mariage(app)

@app.route("/alive", methods=['GET'])
def alive():
    return "OK"

@app.route("/test/news/events", methods=['POST'])
def test():
    print(request.json)
    return "OK"
    
@app.route("/news/events", methods=['POST'])
def news_events():
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

@app.route("/news/tweets", methods=['POST'])
def news_tweets():
    print(request.json)

    embed = discord.Embed(
            url=request.json['link'],
            description=request.json['tweet'])
    embed.set_author(
            name=request.json['name'],
            icon_url=request.json['author'])
    
    m.sendTweet(embed)

    return 'OK'
    

def findConntents(elm, pre):
    for nx in elm.find_all_next():
        if (pre(nx)):
            yield nx
        else:
            break

if __name__ == "__main__":
    with app.app_context():
        m.db.create_all()
        boss = m.Boss('カスパ', '([かカ][すス][パぱ])|(caspa)', '68', 6)
        m.db.session.add(boss)
        m.db.session.commit()

thread = threading.Thread(target=m.run, args=(os.environ['DISCORD_BOT_TOKEN'],))
thread.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)