from discord.ext import commands
import os
import traceback
import discord
    
    
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

# テキストチャンネルの先頭につける文字
CHANNEL_PREFIX = "private_"
# botたちのロール名 (botはテキストチャンネルに参加していてほしい)
BOT_ROLE_NAME = "bot"



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

  bot.run(token)
    



# 接続できたときに実行される
@client.event
async def on_ready():
    # 初期化処理などが行えるよ
    print("On ready")


# ボイスチャンネル内の状態が変化したときに実行される
@client.event
async def on_voice_state_update(member, before, after):
    # チャンネルを移動していない場合処理をしない
    if before.channel == after.channel:
        return

    # チャンネルから退出してきた場合
    if before.channel is not None:
        # ボイスチャンネルに誰もいなくなった場合
        if len(before.channel.members) == 0:
            # テキストチャンネルを削除する
            await _channel_delete(member, before.channel)
        else:
            # テキストチャンネルから退出させる
            await _channel_exit(member, before.channel)

    # ボイスチャンネルに参加してきた場合
    if after.channel is not None:
        # 参加したチャンネルの1人目だった場合
        if len(after.channel.members) == 1:
            # テキストチャンネルを作成する
            await _channel_create(member, after.channel)
        else:
            # テキストチャンネルに参加させる
            await _channel_join(member, after.channel)

        # 入室時にメンションでチャンネルに案内
        await _channel_send_join(member, after.channel)

    print("fin voice state update event")


# テキストチャンネルを検索する関数
def _channel_find(voiceChannel):
    text_channels = voiceChannel.guild.text_channels
    channel_name = CHANNEL_PREFIX + str(voiceChannel.id)
    # 名前からチャンネルオブジェクトを取得する
    return discord.utils.get(text_channels, name=channel_name)


# チャンネル作成時の権限リストを返す
def _init_overwrites(guild, member):
    overwrites = {
        # デフォルトのユーザーはメッセージを見れないように
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        # 参加したメンバーは見ることができるように
        member: discord.PermissionOverwrite(read_messages=True)
    }

    bots_role = discord.utils.get(guild.roles, name=BOT_ROLE_NAME)
    if bots_role is not None:
        # Botもメッセージを見れるように
        bot_overwrite = {
            bots_role: discord.PermissionOverwrite(read_messages=True)
        }
        overwrites.update(bot_overwrite)

    return overwrites


# テキストチャンネルを作成する関数
async def _channel_create(member, voiceChannel):
    guild = voiceChannel.guild

    channel_name = CHANNEL_PREFIX + str(voiceChannel.id)
    overwrites = _init_overwrites(guild, member)
    category = voiceChannel.category

    # テキストチャンネルを作成
    await guild.create_text_channel(
        channel_name, overwrites=overwrites, category=category)


# テキストチャンネルを削除する関数
async def _channel_delete(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        await target.delete()


# テキストチャンネルに参加させる関数
async def _channel_join(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        overwrites = discord.PermissionOverwrite(read_messages=True)
        # 該当メンバーに読み取り権限を付与
        await target.set_permissions(member, overwrite=overwrites)


# テキストチャンネルから退出させる関数
async def _channel_exit(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        # 該当メンバーの読取権限を取り消し
        await target.set_permissions(member, overwrite=None)


# 入室時にメンションを飛ばして案内したい
async def _channel_send_join(member, voiceChannel):
    target = _channel_find(voiceChannel)
    if target is not None:
        await target.send(member.mention + "通話中のチャットはこちらをお使いください")


if __name__ == "__main__":
    client.run(token)
    
