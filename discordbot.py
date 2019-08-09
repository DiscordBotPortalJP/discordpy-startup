from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def otupi(ctx):
    await ctx.send('ドラゴンフラッグ')
    
async def bakunetu(ctx):
    await ctx.send('おちんぽ大好き')


bot.run(token)
