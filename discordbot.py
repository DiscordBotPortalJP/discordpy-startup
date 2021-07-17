from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def neko(ctx):
    await ctx.send('にゃん') 

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

bot.run(token)
