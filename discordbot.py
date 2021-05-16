from discord.ext import commands, tasks
import os
import traceback


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@tasks.loop(seconds=5.0, count=5)
async def slow_count():
    print(slow_count.current_loop)

@slow_count.after_loop
async def after_slow_count():
    print('done!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    await slow_count.start()

bot.run(token)
