from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='s>')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client() 

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")

@bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)


@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command()
async def play(ctx):
    """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    if not ctx.message.attachments:
        await ctx.send("ファイルが添付されていません。")
        return

    await ctx.message.attachments[0].save("tmp.mp3")

    ffmpeg_audio_source = discord.FFmpegPCMAudio("tmp.mp3")
    voice_client.play(ffmpeg_audio_source)

    await ctx.send("再生しました。")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command()
async def test(ctx):
    await ctx.send('テストだと思ったか？残念普通のコマンドだ')
@bot.command()
async def syamu(ctx):
    await ctx.send('　ウイイイイイイイッッッッスどうも、シャムでーす。')
@client.event
async def on_message(message):
 if message.content == ('hello'):
    message.channel.send('hello')
    
bot.run(token)
