from discord.ext import commands
import os
import traceback
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

client = discord.Client()    

@client.command()
async def start():
    asyncio.ensure_future(greeting_gm())
    
async def greeting_gm():
    await client.send_message(channel 'test')
    await asyncio.sleep(10)
    
client.run(token)
bot.run(token)
