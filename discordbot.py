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
    
@bot.event
async def on_message(message):
    #メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    #「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/gollira':
        await message.channel.send('うほうほ')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
