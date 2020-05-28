import discord
from discord.ext import commands
import os
import traceback
import time
from cogs import evals

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
bot.teams = [546682137240403984]

bot.globalc = True

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    if bot.globalc == True:
        try:
            if message.author.bot:
            # もし、送信者がbotなら無視する
                return
            GLOBAL_CH_NAME = "mikan-global" # グローバルチャットのチャンネル名

            if isinstance(message.channel,discord.TextChannel) and message.channel.name == GLOBAL_CH_NAME:
            # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

                await message.delete() # 元のメッセージは削除しておく

                channels = bot.get_all_channels()
                global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
            # channelsはbotの取得できるチャンネルのイテレーター
            # global_channelsは hoge-global の名前を持つチャンネルのリスト

                embed = discord.Embed(title=GLOBAL_CH_NAME, description=message.content, color=0x00bfff)

                embed.set_author(name=message.author.display_name, icon_url=message.author.avatar_url_as(format="png"))
                embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",icon_url=message.guild.icon_url_as(format="png"))
            # Embedインスタンスを生成、投稿者、投稿場所などの設定

                for channel in global_channels:
                # メッセージを埋め込み形式で転送
                    await channel.send(embed=embed)
            else:
                await bot.process_commands(message)
        except Exception as error:
            await on_command_error(message.channel,error)
    else:
        return

@bot.command(pass_context=True)
async def ping2(ctx):  # 処理時間を返す
    startt = time.time()
    tmp = await ctx.send("計測中……!")
    await tmp.edit(content="pong！\n結果:**" + str(round(time.time()-startt, 3))+"**秒だ！")

evals.setup(bot)
bot.run(token)
