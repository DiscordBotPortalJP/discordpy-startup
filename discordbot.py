import discord
import os
import traceback
import asyncio
from pydub import AudioSegment

token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()
   
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    server_id = message.author.guild.id
    voice_id = message.author.voice.channel.id
    vc = client.voice_clients
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    
    if message.content.startswith('calc'):
        phrase=message.content.split()
        formula=phrase[1]
        await message.channel.send(eval(formula))
    
    if message.content == 'あああ':
        channel =  client.get_channel(voice_id)
        vc = await channel.connect()
        ffmpeg_audio_source = discord.FFmpegPCMAudio("./SE/aaa.wav")
        sound = AudioSegment.from_file("./SE/aaa.wav", "wav")
        vc.play(ffmpeg_audio_source)
        await asyncio.sleep(sound.duration_seconds+1)
        await vc.disconnect()
        

# Botの起動とDiscordサーバーへの接続
client.run(token)
