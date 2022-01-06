import discord
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
from quotes.dengeki import get_dengeki
from quotes.yakigote import get_yakigote
from quotes.nadenade import get_nadenade
from quotes.morase import get_morase
from quotes.omikuji import get_omikuji
from quotes.luckyitem import get_lucky
from quotes.syabette import get_syabette
from quotes.momimomi import get_momimomi
from quotes.feint import get_feint

#デフォのintentではmemberにアクセスできないので、ここでTrueに（app画面からのserver members intent設定も必要）
inte = discord.Intents.default()
inte.members = True
#BOTをコンストラクト
bot = commands.Bot(command_prefix='/', intents=inte)
#動かすにはトークンが必要
token = os.environ['DISCORD_BOT_TOKEN']

#BOTクールタイム（秒）
ct = 60
#BOT前回の発言イベント時間（初期ct秒黙るためあらかじめ引く）
prev_time = datetime.datetime.now() - datetime.timedelta(seconds=ct)

#ボットちゃん
bot_chan = RyonageBot()

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
	#botはカスタムステータス使えないらしい
	#await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, state="NAMEOFMYACTIVITY"))
	
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
async def aisatsu(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		name = ctx.message.author.name if ctx.message.author.nick is None else ctx.message.author.nick
		await ctx.send(f"ドーモ、{name}＝サン。リョナゲボットです。")
		
@bot.command()
async def oppai(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("おっぱいおっぱい！")
		
@bot.command()
async def anal(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("アナルの話しました？")
		
@bot.command()
async def anus(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("本当はアヌスでもアナルはもはや名詞になってますよね")
		
@bot.command()
async def sex(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send("せっくす！")
@bot.command()
async def test(ctx):
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		pass
		await ctx.send("今はテストはないみたいです")
		
@bot.command()
async def harapan(ctx):
	global prev_time
	#殴るとCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
	await ctx.send(get_harapan(bot_chan, ctx.message))
	
@bot.command()
async def dengeki(ctx):
	global prev_time
	#スタンガンでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
	await ctx.send(get_dengeki(bot_chan, ctx.message))

@bot.command()
async def yakigote(ctx):
	global prev_time
	#焼きごてでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=60)
	await ctx.send(get_yakigote(bot_chan, ctx.message))

@bot.command()
async def feint(ctx):
	global prev_time
	#フェイントでCT延長
	prev_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
	#瀕死じゃないなら喋る
	if bot_chan.dying_hp < bot_chan.get_hp():
		await ctx.send(get_feint(bot_chan, ctx.message))
	
@bot.command()
async def nadenade(ctx):
	bot_chan.heal(15)
	await ctx.send(get_nadenade(bot_chan, ctx.message))
	
@bot.command()
async def momimomi(ctx):
	bot_chan.heal(5)
	await ctx.send(get_momimomi(bot_chan, ctx.message))

@bot.command()
async def morase(ctx):
	await ctx.send(get_morase(bot_chan, ctx.message))
	
@bot.command()
async def omikuji(ctx):
	await ctx.send(get_omikuji(bot_chan, ctx.message))
	
@bot.command()
async def lucky(ctx):
	await ctx.send(get_lucky(bot_chan, ctx.message))
	
@bot.command()
async def rkey(ctx):
	bot_chan.heal(9999)
	
@bot.command()
async def syabette(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)
	await ctx.send(get_syabette(bot_chan, ctx.message))
	
@bot.command()
async def okiro(ctx):
	global prev_time
	#CTを大袈裟な数でリセット
	prev_time = datetime.datetime.now() - datetime.timedelta(days=1)

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

				#セリフの文字列取得["セリフ", flag]で返る　BOTちゃん反応のために仕方なく順序をずらす
				msg = get_bot_reaction(message)
				
				#ct経ってないかつflagがTrue（通常の反応）なら落とす
				if datetime.datetime.now() < t + datetime.timedelta(seconds=ct) and msg[1]:
					return
				
				if msg[0] != "":
					await message.channel.send(msg[0])
					prev_time = datetime.datetime.now()
	await bot.process_commands(message)


#メンバー加入
@bot.event
async def on_member_join(member):
	#何故か加入メッセージより先に流れるのでスリープでごまかす
	await asyncio.sleep(0.5)
	#玄関チャンネルで発言　多分ニックネームは入った瞬間は付いていないからnameだけでいい
	await bot.get_channel(928650405246824488).send(f"{member.name}さんはじめまして！お暇なときに<#798192857327992882>を一読しておいてくださいね！")
	
	
#アンケートゾーン*************************************************************************************************************
@bot.command()
async def vote(ctx, *args):
	if bot_chan.get_hp() <= bot_chan.dying_hp:
		await ctx.send("いま・・・そんな状態じゃ・・・ないです・・・")
		return
	# 前文句
	name = ctx.message.author.name if ctx.message.author.nick is None else ctx.message.author.nick
	vote_text_prefix = name + "さんのアンケートです！\n:regional_indicator_q:"
	# 選択肢未指定の場合の絵文字
	vote_emoji_on_no_choice = ["⭕","❌"]
	# 選択肢指定の場合の絵文字
	vote_emoji_on_some_choice = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
	# 選択肢の数が↑のやつより多かった場合のメッセージ
	vote_text_choice_overflow_message = "選択肢はしよーじょー10個までです！"
	
	commands = list(args)
	
	if len(commands) <= 0:
		await ctx.send("あの、本文がないとアンケート出来ませんケド・・・")
		return

	text = vote_text_prefix + commands.pop(0)
	if len(commands) <= 0:
		#マルバツ
		vote = await ctx.send(text)
		for emoji in vote_emoji_on_no_choice:
			await vote.add_reaction(emoji)
	else:
		for index in range(len(commands)):
			if index < len(vote_emoji_on_some_choice):
				text += "\n" + vote_emoji_on_some_choice[index] + ":" + commands[index]
			else:
				text += "\n" + vote_text_choice_overflow_message
				break
		vote = await ctx.send(text)
		for index in range(len(commands)):
			if index < len(vote_emoji_on_some_choice):
				await vote.add_reaction(vote_emoji_on_some_choice[index])
#アンケート終わり*************************************************************************************************************
	
#起動
bot.run(token)
