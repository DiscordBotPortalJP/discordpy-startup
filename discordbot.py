from discord.ext import commands
import os
import traceback
import discord

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

async def reply(message):
    reply = f'{message.author.mention}呼んだかな？'
    await message.channel.send(reply)

@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)

bot.run(token)
