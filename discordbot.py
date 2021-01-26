from discord.ext import commands
import os
import traceback
#heroku ポスグレのためのライブラリ
#import psycopg2
import sqlalchemy

#汎用モジュール
import random
import datetime

#自作モジュール
import bot_reaction

#BOTをコンストラクト
bot = commands.Bot(command_prefix='/')
#動かすにはトークンが必要
token = os.environ['DISCORD_BOT_TOKEN']

mes_time = {}

#エラーだけど吐かせないでコメントで終わり
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    msg = "そんなの知らないです・・・"
    await ctx.send(msg)
    #await ctx.send(error_msg)

#自分でコマンドを作れる
#@commands.cooldown(1, 30, commands.BucketType.user（とかchannelとかserver）)でクールダウン仕込める
@bot.command()
async def ping(ctx):
    await ctx.send("chinpong")
	
@bot.command()
async def omanko(ctx):
    await ctx.send("おまんこ！")

@bot.command()
async def harapan(ctx):
    await ctx.send(bot_reaction.get_harapan(ctx.message))

#発言に反応する
@bot.event
async def on_message(message):
	#発言者がBOTなら即終了
	if message.author.bot:
        	return

	msg = bot_reaction.get_bot_reaction(message)
	
	if msg != "":
		await message.channel.send(msg)
	await bot.process_commands(message)	

#起動
bot.run(token)
