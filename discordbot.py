from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # メッセージが相談と情報交換カテゴリだったら上げる
    if message.channel.category_id == 630802817522728960:
        await message.channel.edit(position=0)

    
@bot.command()
    # 「／neko」と発言したら「にゃーん」が返る処理
    async def neko(ctx):
    await ctx.send('にゃーん')



bot.run(token)
