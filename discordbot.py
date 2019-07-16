from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
import discord
import os
import traceback
import threading
import asyncio

class Mariage:
    client = None
    app = None
    db = SQLAlchemy()

    def __init__(self, app):
        self.db.init_app(app)
        self.app = app
    
    class Event(db.Model):
        channel_id = Column(String(18), primary_key=True)

        def __init__(self, channel_id):
            self.channel_id = channel_id

        def __repr__(self):
            return '<Event %r>' % self.channel_id
    
    class Tweet(db.Model):
        channel_id = Column(String(18), primary_key=True)

        def __init__(self, channel_id):
            self.channel_id = channel_id

        def __repr__(self):
            return '<Tweet %r>' % self.channel_id
    
    class News(db.Model):
        url = Column(String(128), primary_key=True)

        def __init__(self, url):
            self.url = url
        
        def __repr__(self):
            return '<News %r>' % self.url

    def run(self, token):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = discord.Client()

        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

        @self.client.event
        async def on_message(message):
            # メッセージ送信者がBotだった場合は無視する
            if message.author.bot:
                return
            # 「/neko」と発言したら「にゃーん」が返る処理
            if message.content == '/neko':
                await message.channel.send('にゃーん')
            # 話しかけた人に返信する
            if self.client.user in message.mentions: # 話しかけられたかの判定
                reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
                await message.channel.send(reply) # 返信メッセージを送信
            # メンバーのリストを取得して表示
            if message.content == '/members':
                print(message.guild.members)
            # 役職のリストを取得して表示
            if message.content == '/roles':
                print(message.guild.roles)
            # テキストチャンネルのリストを取得して表示
            if message.content == '/text_channels':
                print(message.guild.text_channels)
            # ボイスチャンネルのリストを取得して表示
            if message.content == '/voice_channels':
                print(message.guild.voice_channels)
            # カテゴリチャンネルのリストを取得して表示
            if message.content == '/category_channels':
                print(message.guild.categories)
            # イベント配信チャンネル登録
            if message.content == '/join_news':
                if (not message.author.guild_permissions.administrator):
                    await message.channel.send('何様のつもり？')
                    return
                with self.app.app_context():
                    event = self.db.session.query(self.Event).filter_by(channel_id=str(message.channel.id)).first()
                    if (event != None):
                        await message.channel.send('もう入ってるよっ！')
                        return
                    else:
                        event = self.Event(message.channel.id)
                        self.db.session.add(event)
                        self.db.session.commit()
                        await message.channel.send('こんどからお知らせするよっ！')
            if message.content == '/leave_news':
                if (not message.author.guild_permissions.administrator):
                    await message.channel.send('何様のつもり？')
                    return
                with self.app.app_context():
                    event = self.db.session.query(self.Event).filter_by(channel_id=str(message.channel.id)).first()
                    if (event != None):
                        self.db.session.delete(event)
                        self.db.session.commit()
                        await message.channel.send('さよならだね...')
                        return
                    else:
                        await message.channel.send('お知らせしてないよ？？？')
            # ツイート配信チャンネル登録
            if message.content == '/join_tweet':
                if (not message.author.guild_permissions.administrator):
                    await message.channel.send('何様のつもり？')
                    return
                with self.app.app_context():
                    tweet = self.db.session.query(self.Tweet).filter_by(channel_id=str(message.channel.id)).first()
                    if (tweet != None):
                        await message.channel.send('もう入ってるよっ！')
                        return
                    else:
                        tweet = self.Tweet(message.channel.id)
                        self.db.session.add(tweet)
                        self.db.session.commit()
                        await message.channel.send('こんどから囀るよっ！')
            if message.content == '/leave_tweet':
                if (not message.author.guild_permissions.administrator):
                    await message.channel.send('何様のつもり？')
                    return
                with self.app.app_context():
                    tweet = self.db.session.query(self.Tweet).filter_by(channel_id=str(message.channel.id)).first()
                    if (tweet != None):
                        self.db.session.delete(tweet)
                        self.db.session.commit()
                        await message.channel.send('さよならだね...')
                        return
                    else:
                        await message.channel.send('お知らせしてないよ？？？')

        asyncio.ensure_future(self.client.start(token))
        loop.run_forever()
    
    def broadcast(self, message):
        for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(message), loop=self.client.loop)
    
    def broadcastEmbed(self, embed):
         for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
    
    def sendNews(self, embeds):
        with self.app.app_context():
            news = list(map(lambda x : x.url, self.News.query.all()))
            for event in self.Event.query.all():
                channel=self.client.get_channel(int(event.channel_id))
                if (channel!=None):
                    for embed in embeds:
                        if (embed.url not in news):
                            asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
                            entry = self.News(embed.url)
                            self.db.session.add(entry)
                            news.append(embed.url)
            self.db.session.commit()

    def sendTweet(self, embed):
        with self.app.app_context():
            for tweet in self.Tweet.query.all():
                channel=self.client.get_channel(int(tweet.channel_id))
                if (channel!=None):
                    asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
