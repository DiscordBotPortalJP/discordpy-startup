#インストールしたdiscord.pyの読み込み
import discord 
import os

#翠のトークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

#接続に必要なオブジェクトを生成
client = discord.Client()

#起動時に動作する処理
@client.event
async def on_ready():
    print('Hello World,FRONt LINeナビゲーションbotプログラム「翠ｰスイｰ」、起動しました')

#おはよう				
#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return 
    #「おはよう」と発言したら「おはようございます、(送信したユーザーネーム)様！」と返す処理
    if message.content.startswith('おは') or message.content == 'ぐっもーにん':
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

#botの起動とdiscordサーバーへの接続
client.run(TOKEN)
			
