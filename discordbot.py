from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='s>')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

async def syamu(ctx):
    await ctx.send('ウイイイイイイイッッッッスどうも、シャムでーす。まぁ今日はオフ会、当日ですけども。えーとですね、まぁ集合場所の、えーイオンシネマに行ってきたんですけども、ただいまの時刻は1時を回りました。はい、ちょっと遅れて来たんですけどもね。えー11時ちょっとすぎくらいに、えーイオンシネマに行ったんですけども。ほんでーまぁイオンシネマの全体の動画を撮った後に行ったんですけども。スィー。ほんでーかれこれまぁ二時間くらい、えー待ったんですけども参加者は誰一人来ませんでした。ガチャ。誰一人来ることなかったですぅ。残念ながら。はい。一人くらい来るやろうなーと思ってたんですけども、スゥー、結局二時間くらい待っても誰一人来ませんでしたね、えぇ。')
bot.run(token)
