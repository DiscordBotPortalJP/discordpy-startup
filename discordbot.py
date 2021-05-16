from discord.ext import commands
import os
import traceback

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

#client = discord.Client()    
chnnel_sent = None

@tasks.loop(seconds=10)
async def send_message_every_6hour():
    await channel_sent.send("レイド攻撃準備完了！いざ出陣！")
    
@bot.event
async def start():
    global channel_sent
    channel_sent = bot.get_channel("#general")
    send_message_every_6hour.start() 

bot.run(token)
