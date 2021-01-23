from discord.ext import commands
import os
import traceback
import harapan

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    msg = "そんなの知らないです"
    await ctx.send(msg)
#await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send("chinpong")

@bot.command()
async def omanko(ctx):
    await ctx.send("おまんこ！")

@bot.command()
async def harapan(ctx):
    await ctx.send(get_harapan())
"""
@bot.event
async def on_message(message):
	# CHECK IF THE MESSAGE SENT TO THE CHANNEL IS "HELLO".
	if message.content == "hello":
		# SENDS A MESSAGE TO THE CHANNEL.
		await message.channel.send("pies are better than cakes. change my mind.")

	# INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
	await bot.process_commands(message)
    """
"""
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == "アナル":
        await message.channel.send("アナル！")
#    if "アナル" in message.content
    """

    
bot.run(token)
