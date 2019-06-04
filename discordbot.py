#インストールしたdiscord.pyの読み込み
import discord 
import os

#randomモジュールの読み込み
import random

#翠のトークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

#接続に必要なオブジェクトを生成
client = discord.Client()

#起動時に動作する処理
@client.event
async def on_ready():
    print('Hello World,FRONt LINeナビゲーションbotプログラム「Project-SUI-」、起動しました')

#おはよう				
#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return 
    #「おはよう」と発言したら「おはようございます、(送信したユーザーネーム)様！」と返す処理
    if message.content.startswith('おはよ') or message.content == 'ぐっもーにん':
        await message.channel.send('おはようございます、' + message.author.name + '様！( ⑉¯ ꇴ ¯⑉ )')
#おやすみ	
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return		
    #「おやすみ」と発言したら「おやすみなさい！」と返す処理
    if message.content == 'おやすみ':
        await message.channel.send('おやすみなさい、良い夢を見てくださいね！(｡•̀ᴗ-)✧')		
#会話する
 #にゃあ
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return
    #「にゃあ」と言ったら猫の真似をする			
    if message.content == '翠、猫の真似して欲しい！' or message.content == '翠、癒して！':
        await message.channel.send('ฅ(๑>ㅅ<๑)ฅﾆｬｰ')
 
 #起きてる？
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return 
    #「起きてる？」と言ったら返事する
    if message.content == '翠、起きてる？':
        await message.channel.send('私はいつも起きてますよ！何かご用ですか？((っ•ω•⊂))')												
 #褒め
    #メッセージ送信者がbotだった場合の無視処理    
    if message.author.bot:
            return 
    #「可愛い」と言うと照れる
    if message.content == '翠、可愛い！' or message.content == '翠、かわいい！':
        await message.channel.send('( ﻿˶﻿ˆ꒳ˆ˵﻿ )ｴﾍﾍ、ありがとうございます！スイ、頑張りますね！')
 #御籤
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return 
    #「翠、おみくじ引かせて！」って言うとおみくじ引く
    omikuji = ['おめでとうございます！大吉ですよ！(๑>∀<๑)♥', '中吉！あなたの運はそこそこですね！( ᐢ˙꒳​˙ᐢ )♡', '小吉ですけど、吉なだけマシと思いましょう！(｡•̀ᴗ-)✧','凶です…今日は外出を控えることをオススメします(´・ω・｀)','うーむ、今日のあなたの運勢は中凶ですね…気分転換にアイスでもいかがですか？(´ ｡•ω•｡)っ','大凶………最悪の運勢です、何もしないで寝ましょう(   ･᷅ὢ･᷄ )']
    result = random.choice(omikuji)
    
    if message.content == '翠、おみくじ引かせて！' or '翠、今日の運勢は？':
        await message.channel.send(result)
#役職付与
    if message.content == '同意します':
        role = discord.utils.get(message.guild.roles, name='FRONt LINe所属メンバー')
        await message.author.add_roles(role)
        
        reply = f'ゲームクランFRONt LINeへようこそ、{message.author.mention} さん！あなたのご活躍に期待します！'
        await message.channel.send(reply)

#botの起動とdiscordサーバーへの接続
client.run(TOKEN)
			
