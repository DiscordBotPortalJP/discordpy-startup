import traceback
import re
import discord
import functools
import mojimoji
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

# 本番用
#旧トークン
#token = "NzA4OTg0MDU4Njc1MzMxMTIz.Xrf-3w.L-A8xBGpgCBzdO6TQ9U_BvA4Nvc"
token = os.environ['DISCORD_BOT_TOKEN']

# テスト用
# token = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"

# 予約受付リスト
turn_list = []

# 本番用
channel_id = 709031720678326304

# テスト用
#channel_id = 700285431073472540

# 標準のhelpコマンドを削除
bot.remove_command('help')


def check_if_target_channel():
    def predicate(ctx):
        return ctx.message.channel.id == channel_id

    return commands.check(predicate)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    if message.channel.id != channel_id: return

    # ボットのメッセージを除外
    if message.author.bot:
        return

    # メッセージからのハンドル(予約)
    if re.search(r'(まー|マー|麻)(じゃん|ジャン|雀).*(予約|よやく)', message.content):
        await reserv(message)

    # メッセージからのハンドル(予約処理)
    if re.search(r'(次は誰|次誰)', message.content):
        await next_reserv(message)

    # メッセージからのハンドル(前自発者のお礼)
    if re.search(r'.*ありがと.*', message.content):
        if len(turn_list) == 0:
            return

        if turn_list[0].author.name == message.author.name:
            if len(turn_list) == 1:
                await message.channel.send("お疲れ様:heart:")
                turn_list.clear()
                return

            await next_reserv(message)

    # メッセージからのハンドル(救援ID)
    if re.search(r'^[a-zA-Z0-9\s]+$', mojimoji.zen_to_han(message.content), re.IGNORECASE):
        if len(turn_list) < 2:
            return

        if turn_list[1].author.name == message.author.name:
            await message.channel.send("ふぇぇ……誰にも呼ばれない")
            await next_reserv(message)

    # メンションからのハンドル
    if bot.user in message.mentions:
        # 予約受付
        if re.search(r'.*予約.*', message.content):
            await reserv(message)
        # 予約処理
        elif re.search(r'.*次.*', message.content):
            await next_reserv(message)
        elif message.content == 'help':
            await help(message)
        else:
            await message.channel.send("私の扱い方だわに")
            await help(message)

    await bot.process_commands(message)


# デバッグ用(これがあるとDiscord上にエラーメッセージが出る)
# @bot.event
# async def on_command_error(ctx, error):
#    if isinstance(error, commands.CheckFailure): return
#    orig_error = getattr(error, "original", error)
#    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#    await ctx.send(error_msg)

# 予約受付関数
@bot.command()
@check_if_target_channel()
async def reserv(message):
    n = random.randint(4, 8)

    # 重複チェック
    for item in turn_list:
        if message.author.name in item.author.name:
            await message.channel.send(f"{message.author.name}" + "さん予約済みなのだわ")
            return

    turn_list.append(message)

    if len(turn_list) > 3:
        if len(turn_list) == n:
            await message.channel.send(
                f"いっぱい入ってきてこわれるぅ～！\n({message.author.name}さんの予約はちゃんと受け付けておいたわに。　" + str(len(turn_list)) + "番目だよ)")
            return

    await message.channel.send(f"{message.author.name}さんの予約を受け付けておいたわ。　" + str(len(turn_list)) + "番目だよ")


# 予約処理関数
@bot.command()
@check_if_target_channel()
async def next_reserv(message):
    if not turn_list:
        await message.channel.send("次は誰もいないわに")
        turn_list.clear()
        return
    n = turn_list[0]
    await message.channel.send(f"{n.author.mention}" + "さんの番だわに")
    del turn_list[0]
    return


# 予約受付リストを表示
@bot.command()
@check_if_target_channel()
async def show(ctx):
    if len(turn_list) == 0:
        await ctx.send("誰も予約してないわに")
        return
    for index, item in enumerate(turn_list):
        if index == 0:
            await ctx.send("今は " + item.author.name + "さんの番だわに")
        else:
            await ctx.send(str(index + 1) + "番目： " + item.author.name + "さんだわに")


# 予約受付を初期化
#@bot.command()
@bot.command(name='nuclear')
async def clear(ctx):
        turn_list.clear()
        await ctx.send("あぁ～:heart: 予約中の人に核兵器使うの気持ちいい:heart:")

# 予約処理実行用関数
@bot.command()
@check_if_target_channel()
async def next(ctx):
    await next_reserv(ctx)


# 使い方
@bot.command()
@check_if_target_channel()
async def help(message):
    embed = discord.Embed(title="麻雀がしたいるかさんの取り扱い説明書", description="", color=0xeee657)
    embed.add_field(name="@麻雀がしたいるかさん 予約", value="予約の列に並ばせるわに", inline=False)
    embed.add_field(name="@麻雀がしたいるかさん 次", value="次の順番の人を呼び出すわに", inline=False)
    embed.add_field(name="!next", value="次の順番の人を呼び出すわに", inline=False)
    embed.add_field(name="!show", value="予約の列を確認するわに", inline=False)
    embed.add_field(name="!nuclear", value="予約の列に核兵器打ち込むわに", inline=False)
    await message.channel.send(embed=embed)
bot.run(token)
