import asyncio

import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzA0OTYzNzc5ODU0ODYwMjk4.Xqky1Q.5DOHSeeFi86yhkouIwvNlUaEO2c'

client = discord.Client()

@client.event
async def on_ready():
    print('樺地起動')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if client.user != message.author:
        if '落ち着いたか？' in message.content:
            await message.channel.send("ウッス")
            return
        if 'お前の親は誰だ？' in message.content:
            await message.channel.send("……頼月ちゃんッス")
            return
        if '消されたいのか' in message.content:
            await message.channel.send("……イヤッス")
            return
        if 'そうだろ？' in message.content:
            if message.author.name == '𝓡𝓮𝓶𝓲𝓵𝓵𝓮':
                await message.channel.send("……チガウッス")
                return
            if message.author.name == 'こくよう' or message.author.name == '頼月' or message.author.name == '𝓡𝓮𝓶𝓲𝓵𝓵𝓮':
                await message.channel.send("……チガウッス")
                return
            else:
                await message.channel.send("ウス")
                return
        if 'そうなのか？' in message.content or '違うだろ？' in message.content:
            await message.channel.send("……ウス")
            return
        if 'グラブルwikiもってこい' in message.content:
            await message.channel.send("……ウス \n https://gbf-wiki.com/")
            return
        if 'イカ武器リストもってこい' in message.content:
            await message.channel.send("……ウス \n https://game8.jp/splatoon-2/163498")
            return
        if 'カブ予測ツールもってこい' in message.content:
            await message.channel.send("……ウス \n https://hyperwiki.jp/acnh/kabu-tool/")
            return
client.run(TOKEN)