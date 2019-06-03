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
	
#起動したらターミナルに表示されるメッセージ
		print('Hello World,FRONt LINeナビゲーションbotプログラム「翠ｰスイｰ」、起動しました')

#おはよう				
#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
	#メッセージ送信者がbotだった場合の無視処理
	if message.author.bot:
			return 
	#「おはよう」と発言したら「おはようございます、(送信したユーザーネーム)様！」と返す処理
	if message.content == 'おはよう':
			await message.channel.send('おはようございます、' + message.author.name + '様！( ⑉¯ ꇴ ¯⑉ )')			
#おやすみ		
	#「おやすみ」と発言したら「おやすみなさい！」と返す処理
	if message.content == 'おやすみ':
			await message.channel.send('おやすみなさい、良い夢を見てくださいね！(｡•̀ᴗ-)✧')										
															
#botの起動とdiscordサーバーへの接続
client.run(TOKEN)
			
