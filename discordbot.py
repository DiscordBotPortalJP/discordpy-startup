from discord.ext import commands
import os
import traceback

#汎用モジュール
import random
import datetime
import asyncio

#自作モジュール
from mymodule.bot_reaction import get_bot_reaction
from mymodule.ryonage_bot import RyonageBot
from quotes.harapan import get_harapan
from quotes.yakigote import get_yakigote
from quotes.nadenade import get_nadenade
from quotes.morase import get_morase

#BOTをコンストラクト
bot = commands.Bot(command_prefix='/')
#動かすにはトークンが必要
token = os.environ['DISCORD_BOT_TOKEN']

#BOTクールタイム（秒）
ct = 60
#BOT前回の発言イベント時間（初期ct秒黙るためあらかじめ引く）
prev_time = datetime.datetime.now() - datetime.timedelta(seconds=ct)

#ボットちゃん
bot_chan = RyonageBot()

"""
#エラーだけど吐かせないでコメントで終わり
@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("そんなの知らないです・・・")
#await ctx.send(error_msg)

#自分でコマンドを作れる helpなどはオーバライドできない
#@commands.cooldown(1, 30, commands.BucketType.user（とかchannelとかserver）)でクールダウン仕込める
@bot.command()
async def ping(ctx):
    await ctx.send("_chinpong_")
	
@bot.command()
async def omanko(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("おまんこ！")

@bot.command()
async def syabutte(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("私に喋って欲しい時は/syabetteですよ？\nえ？本当にしゃぶれ・・・？")

@bot.command()
async def harapan(ctx):
	global prev_time
	#殴るとCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
	await ctx.send(get_harapan(bot_chan, ctx.message))

@bot.command()
async def yakigote(ctx):
	global prev_time
	#焼きごてはさらにCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=60)
	await ctx.send(get_yakigote(bot_chan, ctx.message))
	
@bot.command()
async def nadenade(ctx):
	bot_chan.heal(15)
	await ctx.send(get_nadenade(bot_chan, ctx.message))

@bot.command()
async def morase(ctx):
	await ctx.send(get_morase(bot_chan, ctx.message))
	
@bot.command()
async def rkey(ctx):
	bot_chan.heal(9999)
	
@bot.command()
async def syabette(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)
	
@bot.command()
async def okiro(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)

"""
"""
#発言に反応する
@bot.event
async def on_message(message):
	#botならスルー
	if message.author.bot:
		pass
	else:
		bot_chan.heal(1)
		#瀕死じゃないなら喋る
		if bot_chan.dying_hp < bot_chan.get_hp():
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

"""	
#メンバー加入
@bot.event
async def on_member_join(member):
	print("member")
	#雑談チャンネルで発言
	#await bot.get_channel(798189252080435231).send(member.name + "さんはじめまして！お暇なときに<#798192857327992882>を一読しておいてくださいね！")

#メンバー加入
@bot.event
async def on_guild_join(guild):
	print("guild")
	#雑談チャンネルで発言
	#await bot.get_channel(798189252080435231).send(member.name + "さんはじめまして！お暇なときに<#798192857327992882>を一読しておいてくださいね！")

#メンバー加入
@bot.event
async def on_group_join(channel, user):
	print("group")
	
#起動
bot.run(token)
