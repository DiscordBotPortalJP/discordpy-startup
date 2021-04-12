from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

if not discord.opus.is_loaded(): 
    #もし未ロードだったら
    discord.opus.load_opus("heroku-buildpack-libopus")
    
@bot.command() 
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        #もし送信者がどこのチャンネルにも入っていないなら
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel #送信者のチャンネル

    await channel.connect() #VoiceChannel.connect()を使用

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def pi(ctx):
    await ctx.send('p')


bot.run(token)
