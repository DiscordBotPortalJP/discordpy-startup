from discord.ext import commands
import os
import traceback

#汎用モジュール
import asyncio

#BOTをコンストラクト
bot = commands.Bot(command_prefix='/')
#動かすにはトークンが必要
token = os.environ['DISCORD_BOT_TOKEN']

locked = false

#発言に反応する
@bot.event
async def on_message(message):
        global locked
        if locked:
            return

        locked = True
        await ctx.send("テスト中")
        await asyncio.sleep(100)
        locked = False
        return

#起動
bot.run(token)
