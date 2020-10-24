
# load modules
from discord.ext import commands
import os
import traceback
import cmd.download as dl


# init settings
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


# set command
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def download(ctx):
    await dl.reply(ctx)


# run
bot.run(token)
