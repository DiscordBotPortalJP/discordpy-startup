
# load modules
import os


# init settings
dl_path = os.environ['BS_PLAYLIST_DL_PATH']


# definition
async def reply(message):

    # set reply message
    reply_message = "お試しよ！　" + dl_path

    # format reply message
    reply = f'{message.author.mention}' + ' ' + reply_message

    # send
    await message.channel.send(reply)
