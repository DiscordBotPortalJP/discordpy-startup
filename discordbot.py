from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, or_, and_
from sqlalchemy.orm import relationship
from one_time_scheduler import OneTimeScheduler
from itertools import groupby
import discord
import os
import traceback
import threading
import asyncio
import re
import datetime
import pytz
import math

class Mariage:
    client = None
    app = None
    db = SQLAlchemy()
    __scheduler = OneTimeScheduler()

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
    
    class Boss(db.Model):
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(256))
        fluctuation = Column(String(512))
        field = Column(String(256))
        pop_interval_minutes = Column(Integer)
        random = Column(Boolean, default=False)
        schedules = relationship("Schedule", backref="boss")
        
        def __init__(self, name, fluctuation, field, pop_interval_minutes):
            self.name = name
            self.fluctuation = fluctuation
            self.field = field
            self.pop_interval_minutes = pop_interval_minutes

        def __repr__(self):
            return '<Boss %r>' % self.name
    
    class Schedule(db.Model):
        # メッセージIDそのまま使う
        id = Column(Integer, primary_key=True)
        channel_id = Column(String(18), nullable=False, index=True)
        boss_id = Column(Integer, ForeignKey('boss.id'), nullable=False)
        pop_time= Column(DateTime)
        status =  Column(String(32), index=True)
        user_id = Column(Integer)

        def get_jst_pop_time(self):
            return pytz.timezone('Asia/Tokyo').localize(self.pop_time)

        def __init__(self, id, channel_id, boss_id):
            self.channel_id = channel_id
            self.id = id
            self.boss_id = boss_id
        
        def __repr__(self):
            return '<Schedule %r>' % self.pop_time
        
    def run(self, token):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = discord.Client()
        self.__scheduler.run_asyncio(loop)

        @self.client.event
        async def on_ready():
            print('Logged in as')
            print(self.client.user.name)
            print(self.client.user.id)
            print('------')

        def __clean_schedule():
            target = datetime.datetime.now() - datetime.timedelta(days=7)
            with self.app.app_context():
                schedules = self.db.session.query(self.Schedule).filter(self.Schedule.status=='end', or_(self.Schedule.pop_time==None, self.Schedule.pop_time < target))
                for schedule in schedules:
                    self.db.session.delete(schedule)
                self.db.session.commit()
        
        async def __report(schedules, target_id=None):
            for channel_id, group in groupby(schedules, key=lambda s: s.channel_id):
                report = ''
                for schedule in group:
                    report = report + schedule.get_jst_pop_time().strftime("%H:%M:%S") + ' ' + schedule.boss.name
                    if target_id != None and schedule.id == target_id:
                        report = report + ' ← New\n'
                    else:
                        report = report + '\n'
                if report != '':
                    channel = self.client.get_channel(int(schedule.channel_id))
                    await channel.send(report + '======================')
        
        async def __hunt_report(channel_id, target_id=None):
            now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
            with self.app.app_context():
                schedules = self.db.session.query(self.Schedule).filter(self.Schedule.channel_id==channel_id, self.Schedule.pop_time > now, or_(self.Schedule.status=='remind', self.Schedule.status=='alerm')).order_by(self.Schedule.pop_time.asc())
                await __report(schedules, target_id=target_id)
        
        async def __remind_report():
            now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
            with self.app.app_context():
                schedules = self.db.session.query(self.Schedule).filter(self.Schedule.pop_time > now, or_(self.Schedule.status=='remind', self.Schedule.status=='alerm')).order_by(self.Schedule.channel_id.asc(), self.Schedule.pop_time.asc())
                await __report(schedules)
        
        def __set_remind(message_id, pop_time, now):
            remind_minites = (pop_time - now - datetime.timedelta(minutes=5)).total_seconds() / 60
            self.__scheduler.after_minutes(remind_minites, lambda : asyncio.ensure_future(remind(message_id), loop=self.client.loop), job_id=message_id)
            return remind_minites
        
        async def remind(message_id):
            with self.app.app_context():
                schedule = self.db.session.query(self.Schedule).filter_by(id=message_id, status='remind').first()
                if schedule == None:
                    return
                schedule.status = 'alerm'
                self.db.session.commit()
                channel = self.client.get_channel(int(schedule.channel_id))
                now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
                remind_minites = __set_alerm(schedule.id, schedule.get_jst_pop_time(), now)
                await channel.send(str(math.ceil(remind_minites)) + '分後(' + schedule.get_jst_pop_time().strftime("%H:%M:%S") +')に' + schedule.boss.name + 'が湧きます。')
                
        def __set_alerm(message_id, pop_time, now):
            remind_minites = (pop_time - now).total_seconds() / 60
            self.__scheduler.after_minutes(remind_minites, lambda : asyncio.ensure_future(alerm(message_id), loop=self.client.loop), message_id)
            return remind_minites

        async def alerm(message_id):
            with self.app.app_context():
                schedule = self.db.session.query(self.Schedule).filter_by(id=message_id, status='alerm').first()
                if schedule == None:
                    return
                schedule.status = 'end'
                self.db.session.commit()
                channel = self.client.get_channel(int(schedule.channel_id))
                msg = await channel.send(schedule.boss.name + 'が湧くよ！！！End報告お待ちしております。')
                next_schedule = self.Schedule(msg.id, str(channel.id), schedule.boss_id)
                next_schedule.status = 'registed'
                next_schedule.pop_time = schedule.get_jst_pop_time()
                self.db.session.add(next_schedule)
                self.db.session.commit()
                await msg.add_reaction('🔚')
                await msg.add_reaction('❌')
                if schedule.boss.random:
                    await msg.add_reaction('🔄')

        @self.client.event
        async def on_reaction_add(reaction, user):
            # リアクション送信者がBotだった場合は無視する
            if user.bot:
                return
            if reaction.emoji == '🔚':
                with self.app.app_context():
                    schedule = self.db.session.query(self.Schedule).filter_by(id=reaction.message.id, status='registed').first()
                    if schedule != None:
                        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
                        # 倒してからEND押すまでの時間を考慮して10秒ほど手前にしておく
                        pop_time = now + datetime.timedelta(minutes=schedule.boss.pop_interval_minutes) - datetime.timedelta(seconds=10)
                        schedule.pop_time = pop_time
                        schedule.status = 'remind'
                        schedule.user_id = user.id
                        self.db.session.commit()
                        
                        await __hunt_report(schedule.channel_id, schedule.id)
                        __set_remind(schedule.id, pop_time, now)
            elif reaction.emoji == '❌':
                with self.app.app_context():
                    schedule = self.db.session.query(self.Schedule).filter_by(id=reaction.message.id).filter(and_(self.Schedule.status!='end')).first()
                    if schedule != None:
                        if schedule.status != 'registed':
                            self.__scheduler.cancel(schedule.id)
                        schedule.status = 'end'
                        self.db.session.commit()
                        
                        await reaction.message.channel.send(schedule.boss.name + '討伐リマインドを取り消しました。')
            elif reaction.emoji == '🔄':
                with self.app.app_context():
                    schedule = self.db.session.query(self.Schedule).filter_by(id=reaction.message.id, status='registed').filter(self.Schedule.pop_time!=None).first()
                    if schedule != None:
                        pop_time = schedule.get_jst_pop_time() + datetime.timedelta(minutes=schedule.boss.pop_interval_minutes)
                        schedule.pop_time = pop_time
                        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
                        remind_seconds = (pop_time - now - datetime.timedelta(minutes=5)).total_seconds()
                        if now > pop_time:
                            schedule.status = 'end'
                            self.db.session.commit()
                        elif remind_seconds > 0:
                            schedule.status = 'remind'
                            self.db.session.commit()
                            __set_remind(schedule.id, pop_time, now)
                            await __hunt_report(schedule.channel_id, schedule.id)
                        else:
                            schedule.status = 'alerm'
                            self.db.session.commit()
                            __set_alerm(schedule.id, pop_time, now)
                            await __hunt_report(schedule.channel_id, schedule.id)

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
            # 「/hunt_report」と発言したらボス時間登録する
            if message.content.startswith('/hunt_report'):
                await __hunt_report(str(message.channel.id))
            # 「/hunt」と発言したらボス時間登録する
            if message.content.startswith('/hunt '):
                items = message.content.split()
                with self.app.app_context():
                    boss = None
                    bosses = self.Boss.query.all()
                    for item in bosses:
                        if re.match(item.fluctuation, items[1], re.IGNORECASE):
                            boss = item
                            break
                    if boss != None:
                        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
                        before = self.db.session.query(self.Schedule).filter_by(boss_id=boss.id, channel_id=str(message.channel.id)).filter(and_(self.Schedule.status!='end')).first()
                        if before != None :
                            if before.status == 'registed' or now > before.get_jst_pop_time():
                                before.status = 'end'
                                self.db.session.commit()
                            else:
                                await message.channel.send(boss.name + 'は未消化のリマインダーがあります。')
                                return
                        
                        if len(items) > 2:
                            end_time = __get_end_time(items[2], now)
                            if end_time == None:
                                await message.channel.send('時刻が不正です。')
                                return
                            pop_time = end_time + datetime.timedelta(minutes=boss.pop_interval_minutes)
                            if pop_time < now:
                                await message.channel.send('手遅れです。' + boss.name + 'は' + pop_time.strftime("%H:%M:%S") + 'にEndしています。')
                                return
                            msg = await message.channel.send(boss.name + ' End')
                            schedule = self.Schedule(msg.id, str(message.channel.id), boss.id)
                            schedule.pop_time = pop_time
                            schedule.user_id = message.author.id
                            remind_seconds = (pop_time - now - datetime.timedelta(minutes=5)).total_seconds()
                            if remind_seconds > 0:
                                schedule.status = 'remind'
                                self.db.session.add(schedule)
                                self.db.session.commit()
                                __set_remind(schedule.id, pop_time, now)
                            else:
                                schedule.status = 'alerm'
                                self.db.session.add(schedule)
                                self.db.session.commit()
                                __set_alerm(schedule.id, pop_time, now)
                            await msg.add_reaction('❌')
                            await __hunt_report(schedule.channel_id, schedule.id)
                        else:
                            msg = await message.channel.send(boss.name + 'を狩るんですね！End報告お待ちしております。')
                            schedule = self.Schedule(msg.id, str(message.channel.id), boss.id)
                            schedule.status = 'registed'
                            self.db.session.add(schedule)
                            self.db.session.commit()
                            await msg.add_reaction('🔚')
                            await msg.add_reaction('❌')
                    else:
                        #if items[1] in map(lambda x : x.name, message.channel.members):
                        #    kill = items[1]
                        #    await message.channel.send(kill + 'をリアルハントするんですねっ💖💖💖')
                        #else:
                        await message.channel.send('なんだそりゃ？？？')
        def __get_end_time(str_date, now):
            if re.match('^[0-2]?[0-9]:[0-5]?[0-9]:[0-5]?[0-9]$', str_date):
                end_time = datetime.datetime.strptime(str(now.year) + '/'  +  str(now.month) + '/'+  str(now.day)+ ' ' + str_date + '+0900', '%Y/%m/%d %H:%M:%S%z')
                if end_time > now:
                    return end_time - datetime.timedelta(days=1)
                return end_time
            if re.match('^[0-2]?[0-9]:[0-5]?[0-9]$', str_date):
                end_time = datetime.datetime.strptime(str(now.year) + '/'  +  str(now.month) + '/'+  str(now.day)+ ' ' + str_date + ':00+0900', '%Y/%m/%d %H:%M:%S%z')
                if end_time > now:
                    return end_time - datetime.timedelta(days=1)
                return end_time
            if re.match('^[0-5]?[0-9]$', str_date):
                end_time = datetime.datetime.strptime(str(now.year) + '/'  +  str(now.month) + '/'+  str(now.day) + ' ' + str(now.hour) + ':' + str_date + ':00+0900', '%Y/%m/%d %H:%M:%S%z')
                if end_time > now:
                    end_time = end_time - datetime.timedelta(hours=1)
                if end_time > now:
                    return end_time - datetime.timedelta(days=1)
                return end_time
            return None

        asyncio.ensure_future(self.client.start(token))

        with self.app.app_context():
            for schedule in self.db.session.query(self.Schedule).filter(or_(self.Schedule.status=='remind', self.Schedule.status=='alerm')):
                now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
                if schedule.status == 'remind':
                    remind_seconds = (schedule.get_jst_pop_time() - now - datetime.timedelta(minutes=5)).total_seconds()
                    if remind_seconds > 0:
                        __set_remind(schedule.id, schedule.get_jst_pop_time(), now)
                    else:
                        schedule.status = 'end'
                        self.db.session.commit()
                elif schedule.status == 'alerm':
                    alerm_seconds = (schedule.get_jst_pop_time() - now).total_seconds()
                    if alerm_seconds > 0:
                        __set_alerm(schedule.id, schedule.get_jst_pop_time(), now)
                    else:
                        schedule.status = 'end'
                        self.db.session.commit()
        self.__scheduler.never_hour(lambda : asyncio.ensure_future(__remind_report(), loop=self.client.loop))
        self.__scheduler.never_wednesday('06:00', __clean_schedule)
        loop.run_forever()
    
    def broadcast(self, message):
        for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(message), loop=self.client.loop)
    
    def broadcastEmbed(self, embed):
         for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
    
    def sendNews(self, embeds):
        with self.app.app_context():
            #news = list(map(lambda x : x.url, self.News.query.all()))
            for event in self.Event.query.all():
                channel=self.client.get_channel(int(event.channel_id))
                if (channel!=None):
                    for embed in embeds:
                        #if (embed.url not in news):
                        asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
                        #entry = self.News(embed.url)
                        #self.db.session.add(entry)
                        #news.append(embed.url)
            #self.db.session.commit()

    def sendTweet(self, embed):
        with self.app.app_context():
            for tweet in self.Tweet.query.all():
                channel=self.client.get_channel(int(tweet.channel_id))
                if (channel!=None):
                    asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
