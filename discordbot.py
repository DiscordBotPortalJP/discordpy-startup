from flask import Flask, request
import discord
import os
import traceback
import threading
import asyncio

def run(token):
    m = Mariage()
    m.run(token)

class Mariage:
    client = None

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

        asyncio.ensure_future(self.client.start(token))
        loop.run_forever()
    
    def broadcast(self, message):
        for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(message), loop=self.client.loop)
    
    def broadcastEmbed(self, embed):
         for channel in filter(lambda x : x.type == discord.ChannelType.text, self.client.get_all_channels()):
            asyncio.ensure_future(channel.send(embed=embed), loop=self.client.loop)
    
