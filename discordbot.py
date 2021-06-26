from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='s>')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client() 

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def syamu(ctx):
    await ctx.send('ウイイイイイイイッッッッスどうも、シャムでーす。')
@client.event
async def on_message(message):
 if message.content == ('hello'):
    message.channel.send('hello')
    
bot.run(token)
