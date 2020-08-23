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

@client.event
async def on_message(message):
   if message.author.bot:　　　　　　　　　　　　　　　
       return  　　　　　　　
   if message.content == '反応しろ餓鬼煽り隊':　　　　 
       await message.channel.send('ンアーッ！(起床)') 



bot.run(token)
