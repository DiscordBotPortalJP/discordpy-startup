from discord.ext import commands
import os
import traceback

#汎用モジュール
import random
import datetime
import asyncio

#自作モジュール
from mymodule.bot_reaction import get_bot_reaction
from quotes.harapan import get_harapan

#BOTをコンストラクト
bot = commands.Bot(command_prefix='/')
#動かすにはトークンが必要
token = os.environ['DISCORD_BOT_TOKEN']

#BOTクールタイム（秒）
ct = 30
#BOT前回の発言イベント時間（初期ct秒黙るためあらかじめ引く）
prev_time = datetime.datetime.now() - datetime.timedelta(seconds=ct)

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
"""
@bot.command()
async def help(ctx):
    await ctx.send("へるぷ！")
"""
@bot.command()
async def harapan(ctx):
	global prev_time
	#殴るとCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=3)
	await ctx.send(get_harapan(ctx.message))
	
@bot.command()
async def syabette(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)

#発言に反応する
@bot.event
async def on_message(message):
	#botは即落ち
	if message.author.bot:
		return
	#コマンドなら何もしないためのif
	if message.content[0] != "/":
		global prev_time
		t = prev_time

		#ct経ってなければ落とす
		if datetime.datetime.now() < t + datetime.timedelta(seconds=ct):
			return

		#セリフの文字列取得
		msg = get_bot_reaction(message)

		if msg != "":
			await message.channel.send(msg)
			prev_time = datetime.datetime.now()

	await bot.process_commands(message)

#起動
bot.run(token)
