from discord.ext import commands
import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    
    if message.content.startswith('ねこ'):
        await message.channel.send('にゃーん')

bot.run(token)
