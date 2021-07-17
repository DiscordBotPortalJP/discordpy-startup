import discord
import asyncio

from discord import channel

TOKEN = 'ODY1NTg5MTIyNjU4NDY3OTAx.YPGMsA.ABwZ39Em6PGUU8yL6toApbgdJXI'

CHANNEL_ID = "865589122658467901"

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログイン完了です！')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「チャーミィ」と発言したら、返信する処理
    if message.content == 'チャーミィ':
        await message.channel.send('はじめまして！ボクCHARMの妖精チャーミィ☆')

    if message.content == 'ヒーラー':
        filename = 'b44cca0a98422b81.pdf'
        await message.channel.send("https://drive.google.com/file/d/17X1a_HkkNUOycIylK0g6yQQa1jeHxJx2/view?usp=sharing")

    if message.content == 'ヒーラー2':
        filename = 'テスト用.xlsx'
        await message.channel.send("https://drive.google.com/file/d/1tqyVpv-fq072y5cEr0FboIsV9P3XmrnQ/view?usp=sharing")

    if message.content == 'ヒーラー3':
        filename = 'テスト用.docx'
        await message.channel.send("https://drive.google.com/file/d/1CmqSft5-7YsCYWiTKP14xHi0qhHbnGUd/view?usp=sharing")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)