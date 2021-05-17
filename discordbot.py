from discord.ext import tasks
import discord
import os
import traceback


token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

channel_sent = None
"""
10秒ごとに発言するメソッドを定義している部分。
async def の1行上が定期実行を示すもので、()内で間隔を指定します。
例えば5分ごとなら(minutes=5)です。
"""
@tasks.loop(seconds=10, count=3)
async def send_message_every_10sec():
    await channel_sent.send("10秒経ったよ")

"""
今回はbotの起動直後に定期実行を開始したいので、
botの準備ができた段階で定期実行をstart()します
"""
@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel("#general")
    send_message_every_10sec.start() #定期実行するメソッドの後ろに.start()をつける


client.run(token)