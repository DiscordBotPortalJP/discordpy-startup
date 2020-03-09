# インストールした discord.py を読み込む
import discord
import os
import random

# 自分のBotのアクセストークンに置き換えてください
pytoken = os.environ['DISCORD_BOT_TOKEN']

TEXT_CHANNEL = 536094587190771781

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    msg = "やあ！TEST Botです．よろしくね！"
    print(msg)

# こんにちはメッセージ
@client.event
async def on_message(message):
    if message.content.startswith("こんにちは"):
        if client.user != message.author:
            msg = "こんにちは " + message.author.name + "さん！"
            await message.channel.send(msg)

   

# メンバのステータスが変更されたら
@client.event
async def on_member_update(before, after):
    if before.status != after.status:
        msg = after.display_name + "さんが" + str(after.status) + "になりました"
        message = client.get_channel(536094587190771781)
        await message.send(msg)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/mine':
        if client.user != message.author:
            path = 'C:/Users/tahik/AppData/Roaming/.minecraft/screenshots'
            m = 'play.minecraft.jp\n来てね'

            dirs = os.listdir(path)
            file = random.choice(dirs)
            image = image = path + '\\' + file
            channel = client.get_channel(TEXT_CHANNEL)
            await send.channel(file=discord.File(path))
        

client.run(pytoken)
