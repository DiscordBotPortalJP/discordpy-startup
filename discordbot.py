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

#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return 
#会話
 #おはよう
    #「おはよう」と発言したら「おはようございます、(送信したユーザーネーム)様！」と返す処理
    if message.content.startswith('おはよ') or message.content == 'ぐっもーにん':
        await message.channel.send('おはようございます、' + message.author.name + '様！( ⑉¯ ꇴ ¯⑉ )')
 #おやすみ
    #「おやすみ」と発言したら「おやすみなさい！」と返す処理
    if message.content.startswith('おやすみ'):
        await message.channel.send('おやすみなさい、良い夢を見てくださいね！(｡•̀ᴗ-)✧')	
 #おわ
    #「おわ」でメッセージが終わった場合労う
    if message.content.endswith('おわ'):
        await message.channel.send('お疲れ様です！∠(｀･ω･´)')	
 #にゃあ
    #「にゃあ」と言ったら猫の真似をする			
    if message.content == '翠、猫の真似して欲しい！' or message.content == '翠、癒して！':
        await message.channel.send('ฅ(๑>ㅅ<๑)ฅﾆｬｰ')
 #起きてる？ 
    #「起きてる？」と言ったら返事する
    if message.content == '翠、起きてる？':
        await message.channel.send('私はいつも起きてますよ！何かご用ですか？((っ•ω•⊂))')
 #褒め
    #「可愛い」と言うと照れる
    if message.content == '翠、可愛い！' or message.content == '翠、かわいい！':
        await message.channel.send('( ﻿˶﻿ˆ꒳ˆ˵﻿ )ｴﾍﾍ、ありがとうございます！スイ、頑張りますね！')
 
 #御籤 
    #「翠、おみくじ引かせて！」って言うとおみくじ引く
    prob = random.random()

    if (message.content == '今日の運勢' and 0.0 <= prob < 0.3):
        await message.channel.send('凶')

    elif (message.content == '今日の運勢' and 0.3 <= prob < 0.65):
        await message.channel.send('吉')
    
    elif (message.content == '今日の運勢' and 0.65 <= prob < 0.71):
        await message.channel.send('末吉')

    elif (message.content == '今日の運勢' and 0.71 <= prob < 0.76):
        await message.channel.send('半吉')
    
    elif (message.content == '今日の運勢' and 0.76 <= prob < 0.80):
        await message.channel.send('小吉')
    
    elif (message.content == '今日の運勢' and 0.80 <= prob < 0.83):
        await message.channel.send('末小吉')
    
    elif (message.content == '今日の運勢' and 0.83 <= prob < 1.0):
        await message.channel.send('大吉')

 #忍殺語
    if message.content == '変わり身のジツ！':
        await message.channel.send('イヤーッ！(｢･ω･)｣ｱﾁｮ')

#自動会話
 #笑
    lis = ['笑うのは体にいいことですよ！','ꉂꉂ(>ᗜ<*)','何か楽しいことでもありましたか？|*･ω･)']
    res = random.choice(lis)
    
    if (message.content.endswith('笑') or message.content.endswith('w') and random.uniform(0,1) > 0.75):
        await message.channel.send(res)
        
#役職付与
    if message.content.startswith('同意します'):
        role = discord.utils.get(message.guild.roles, name='FRONt LINe所属メンバー')
        await message.author.add_roles(role)
        
        reply = f'ゲームクランFRONt LINeへようこそ、{message.author.mention} さん！あなたのご活躍に期待します！'
        await message.channel.send(reply)

#ウェルカムメッセージ
@client.event
async def on_member_join(member):
   await client.get_channel(553825840866131989).send(f'ようこそ、**{member.mention} **さん！あなたの訪問を歓迎させていただきます、FLナビゲーションbotの翠と申します！ まずは #サーバー説明・ルール を見ることをオススメしますよ！楽しんでくださいね！')

#リムーブメッセージ
@client.event
async def on_member_remove(member):
    await    client.get_channel(553825840866131989).send(f'**{member.name}が前線を離れました。またの訪問をお待ちしております！**')

#botの起動とdiscordサーバーへの接続
client.run(TOKEN)
			
