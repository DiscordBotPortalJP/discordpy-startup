from discord.ext import commands
import os
import traceback

import random

import harapan_quotes
import bot_reaction

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    msg = "そんなの知らないです・・・"
    await ctx.send(msg)
#await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send("chinpong")

@bot.command()
async def omanko(ctx):
    await ctx.send("おまんこ！")

@bot.command()
async def harapan(ctx):
    await ctx.send(harapan_quotes.get_harapan())

#発言に反応する
@bot.event
async def on_message(message):
	if message.author.bot:
        	return
	await msg = bot_reaction.get_greetings(message)
	if msg == "":
		msg = bot_reaction.get_shimoneta(message)
	if msg != "":
		await message.channel.send(msg)
	await bot.process_commands(message)
	

bot.run(token)
