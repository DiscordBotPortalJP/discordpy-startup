# discordpy-startup
# -*- coding: utf-8 -*-

import discord
import random
import asyncio
import time
import datetime
import urllib.request
import json
import re
import os
import traceback

from discord.ext import tasks

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 623154510662991883
client = discord.Client()
dateTime = datetime.datetime.now()
server_number = len(client.guilds)
client.global_list = [] #グローバルチャット参加チャンネルのリスト
atk_ch_id = 642279311352791061

citycodes = {
    "北海道": '016010',"青森県": '020010',
    "岩手県": '030010',"宮城県": '040010',
    "秋田県": '050010',"山形県": '060010',
    "福島県": '070010',"東京都": '130010',
    "神奈川県": '140010',"埼玉県": '110010',
    "千葉県": '120010',"茨城県": '080010',
    "栃木県": '090010',"群馬県": '100010',
    "山梨県": '190010',"新潟県": '150010',
    "長野県": '200010',"富山県": '160010',
    "石川県": '170010',"福井県": '180010',
    "愛知県": '230010',"岐阜県": '200010',
    "静岡県": '220010',"三重県": '240010',
    "大阪府": '270000',"兵庫県": '280010',
    "京都府": '260010',"滋賀県": '250010',
    "奈良県": '190010',"和歌山県": '300010',
    "鳥取県": '310010',"島根県": '320010',
    "岡山県": '330010',"広島県": '340010',
    "山口県": '350010',"徳島県": '360010',
    "香川県": '370000',"愛媛県": '380010',
    "高知県": '390010',"福岡県": '400010',
    "大分県": '440010',"長崎県": '420010',
    "佐賀県": '410010',"熊本県": '430010',
    "宮崎県": '450010',"鹿児島県": '460010',
    "沖縄県": '471010',"北海": '016010',
    "青森": '020010',"岩手": '030010',
    "宮城": '040010',"秋田": '050010',
    "山形": '060010',"福島": '070010',
    "東京": '130010',"神奈川": '140010',
    "埼玉": '110010',"千葉": '120010',
    "茨城": '080010',"栃木": '090010',
    "群馬": '100010',"山梨": '190010',
    "新潟": '150010',"長野": '200010',
    "富山": '160010',"石川": '170010',
    "福井": '180010',"愛知": '230010',
    "岐阜": '200010',"静岡": '220010',
    "三重": '240010',"大阪": '270000',
    "兵庫": '280010',"京都": '260010',
    "滋賀": '250010',"奈良": '190010',
    "和歌山": '300010',"鳥取": '310010',
    "島根": '320010',"岡山": '330010',
    "広島": '340010',"山口": '350010',
    "徳島": '360010',"香川": '370000',
    "愛媛": '380010',"高知": '390010',
    "福岡": '400010',"大分": '440010',
    "長崎": '420010',"佐賀": '410010',
    "熊本": '430010',"宮崎": '450010',
    "鹿児島": '460010',"沖縄": '471010',
}

help_embed_0 = discord.Embed(title="⚠️YUI注意事項一覧⚠️",description = '🔷**[]は不要です**\n```y![example]→y!example```\n🔷**スペースの有無を確認して下さい**\n```y!example []→有り\ny!example[]→無し```\n🔷**管理者権限必須です**```YUIのコマンドにはYUIに管理者を持たせないと正常に作動しないものが多々御座います。ご注意ください```\n🔷**ニックネーム変更非推奨**```第２項TAO系コマンドは、YUIのニックネームが変わるとオートアタックのみ正常に動作しません。\nTAOに関連性を持たせないつもりであれば、ニックネームの変更は構いません```',color=discord.Colour.green())


help_embed = discord.Embed(title="TAOコマンド系ヘルプ━第２項",description="TAOで使うコマンドを使うヘルプだよ",color=discord.Colour.green())
#help_embed.add_field(name="```y!ch [channel ID]```",value='このコマンドを使った後に**ゆいがんばれ**って言ってくれたら指定したチャンネルでアタックをするから\n後でスイーツおごってもらうからね\n止めてほしいときは**ゆいおつかれ**って言って')
help_embed.add_field(
name='y!login'
,value='`ログインする`'
,inline=True)
help_embed.add_field(
name='y!st'
,value='`::st\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!i'
,value='`::item\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!i [f,e]'
,value='`::i [f,e]\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!re',value='`::ren\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!atk',value='`::atk\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!nekoshima',value='`超激レア枠が出るまでTAOさなきゃいけない\nモンスターの数を占う`'
,inline=False)


help_two_embed = discord.Embed(title="ゆいの機能ヘルプ━第３項"
        ,description="その多機能"
        ,color=discord.Colour.green())
#サーバーの情報を開示するよ\nコード基礎提供者:_toni
help_two_embed.add_field(name='y!dice [下限] [上限]'
        ,value ='```下限~上限の数の間でサイコロをふる```'
        ,inline=False)
help_two_embed.add_field(name='y!sinfo'
        ,value ='```サーバーの情報を開示```'
        ,inline=False)
help_two_embed.add_field(name='y!kuji'
        ,value ='```おみくじ```'
        ,inline=False)
help_two_embed.add_field(name='y!myicon'
        ,value ='```コマンド使用者のアイコン表示```'
        ,inline=False)
help_two_embed.add_field(name='y!poll [タイトル] [内容] '
        ,value ='```👍👎リアクションつきembedメッセージ送信```'
        ,inline=False)
help_two_embed.add_field(name='y!say',value ='```y!say1 [内容]│オウム返し\ny!say2 [題名] [内容]│embed形式送信\ny!say3 [題名] [内容]│embed+送信者メンション+時刻```',inline=False)
help_two_embed.add_field(name='y!clean [数]'
        ,value ='```鯖管理者権限持ちで使用可、指定数のメッセージ消去```'
        ,inline=False)
help_two_embed.add_field(name='y!report [内容]'
        ,value ='```開発者へのレポート＆リクエスト```'
        ,inline=False)
help_two_embed.add_field(name='y!wt [都道府県名]',value='```今日、明日の天気予報「YUI WEATHER」```',inline=True)

embed_special = discord.Embed(
    title='特殊チャンネル系━第４項',
    description='```‣チャンネル内容│チャンネル名\nチャンネル作成コマンド```',color=discord.Colour.green())
embed_special.add_field(name='‣グローバルチャット│global_yui'
        ,value='```y!yui global```',inline=True)
embed_special.add_field(name='‣YUIの起動ログ│yui起動ログ'
        ,value ='```y!yui log```'
        ,inline=True)
embed_special.add_field(name='‣日付変更ログ│yui時報ログ'
        ,value ='```y!yui timelog```')


gacha = discord.Embed(title="ガチャ機能だよ🎯 ━第５頁"
,description="コマンドはy!gacha [ガチャ番号]"
,color=discord.Colour.green()
,inline=False)
gacha.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
gacha.add_field(name="ガチャ種類＋番号一覧",value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\ny!gacha 1\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！\ny!gacha 2")

slot_embed = discord.Embed(title="スロット機能だよ🎰━第６頁",description="コマンドはy!slot [s,c]",color=discord.Colour.green())
slot_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635993816297504809/642579874816720916/money_slot_machine.png")
slot_embed.add_field(name="スロット説明",value="絵文字を利用したスロットだよ\n表示が崩れるから、スマホとパソコンPCでコマンドを分けてるよ\n`y!slot s`がスマホ\n`y!slot c`がPCだよ\nちなみに開発者のスマホ（泥）を基準にしてるからIOS勢は表記が崩れるかも！\n泥勢もテキストサイズ変えちゃったら崩れるからね")

url_embed = discord.Embed(title='YUI関連URL━第７頁')
url_embed.add_field(name ='‣招待URL' ,value ='[ここをクリック🔘](https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=0&scope=bot)')
url_embed.add_field(name ='‣YUIサポートサーバー(仮)',value ='[ここをクリック🔘](https://discord.gg/SHxgnu)')


@client.event
async def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(dateTime)
    print("今入ってる鯖の数"+str(server_number))


    loop.start()
    looop.start()

    channel_id_report = 629327961132236800
    print('We have logged in as {0.user}'.format(client))

    client.global_list = [] #グローバルチャット参加チャンネルのリスト
    for guild in client.guilds:
        tmp = discord.utils.get(guild.text_channels,name="global_yui")
        if tmp: client.global_list.append(tmp)


    embed = discord.Embed(title="YUI起動ログ",description="起動したよ",color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="起動時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=False)
    embed.add_field(name="YUI news", value="大幅に改良！\n詳しくはヘルプの第６項から公式鯖へ", inline=True)

#    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))

flag = False

yt_channel_id = CHANNEL_ID # 最初のチャンネルの


@tasks.loop(seconds=30)
async def loop():
    global yt_channel_id
    if flag:
        channel = client.get_channel(yt_channel_id)
        await channel.send('::atk loop')

    await client.change_presence(activity=discord.Game(name="y!help│"+str(len(client.guilds) )+'の鯖に所属中'))


@tasks.loop(seconds=60)
async def looop():
    now = datetime.datetime.now().strftime('%H:%M')
    if now == '14:59':

        print("時刻判定おｋ")

        em = discord.Embed(title="24:00の時報をお伝えします\nなんちゃって",description=random.choice((
'日付変わったから寝ようね！？',
'まだ起きてるとかみんな狂乱なの？',
'夜更かしは体に悪いよ……え、私？\nBOTだから支障ZEROですｗｗ',
'ねろ（辛辣\nさっさと寝ろ',
'別にいいけどさ……\n夜更かしは体壊さない程度にね',
'えーと、これ読めばいいの？ \n(台本ﾊﾟﾗﾊﾟﾗ)\nねえこの「お兄ちゃんもう寝ないと！」ってなに？\n殺されたいの？',
'私だって君が体壊したら悲しまないわけじゃないんだからさ\nちゃんと寝てね？\n私の事BOTだからってなめてるでしょ\nたとえプログラムされたコードで動いてるだけの義骸でも\n私は私なの')), inline=False)
        em.set_thumbnail(url="https://yahoo.jp/box/roWwt8")
        for c in client.get_all_channels():
            if c.name == 'yui時報ログ':
                client.loop.create_task(c.send(embed=em))
        print("チャンネル判定終了")

@client.event
async def on_disconnect():
    print("YUI was death")
    embed = discord.Embed(title="YUIが切断されあぁ！",description="原因は知らんけど切断されちゃった(灬ºωº灬)てへっ♡",color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="切断時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=True)
#    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))


@client.event
async def on_message(message):

#🔷test運用➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷

    if message.content == "y!help":
        help_embed_one = discord.Embed(title="YUIヘルプ目次━第１項",color=discord.Colour.green())
        help_embed_one.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))

        help_embed_one.add_field(name="‣ヘルプ目次",value='━第１項',inline = True)
        help_embed_one.add_field(name="‣TAOコマンド",value='━第２項',inline = True)
        help_embed_one.add_field(name="‣メイン機能",value='━第３項',inline = True)
        help_embed_one.add_field(name="‣特殊チャンネル",value='━第４項',inline = True)
        help_embed_one.add_field(name="‣ガチャ",value='━第５頁',inline = True)
        help_embed_one.add_field(name="‣スロット",value='━第６頁',inline = True)
        help_embed_one.add_field(name="‣YUI関連URL",value='━第７頁',inline = True)
        help_embed_one.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}")


        print('help was opened')
        page_count = 0 #ヘルプの現在表示しているページ数
        page_content_list = [
help_embed_0,
help_embed_one,
help_embed,
help_two_embed,
embed_special,
gacha,
slot_embed,
url_embed] #ヘルプの各ページ内容

        send_message = await message.channel.send(embed=page_content_list[0]) #最初のページ投稿
        await send_message.add_reaction("➡")

        def help_react_check(reaction,user):
            '''
            ヘルプに対する、ヘルプリクエスト者本人からのリアクションかをチェックする
            '''
            if reaction.message.id != send_message.id:
                return 0
            if reaction.emoji == "➡" or reaction.emoji == "⬅":
                if user != message.author:
                    return 0
                else:
                    return reaction,user

        while not client.is_closed():

            try:
                reaction,user = await client.wait_for('reaction_add',check=help_react_check,timeout=40.0)
            except:

                return #時間制限が来たら、それ以降は処理しない

            else:

                if reaction.emoji == "➡" and page_count < 8:
                    page_count += 1

                if reaction.emoji == "⬅" and page_count > 0:
                    page_count -= 1


                await send_message.clear_reactions() #事前に消去する
                await send_message.edit(embed=page_content_list[page_count])

                if page_count == 0:
                    await send_message.add_reaction("➡")
                elif page_count == 1:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 2:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 3:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 4:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 5:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 6:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 7:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 8:
                    await send_message.add_reaction("⬅")                    #各ページごとに必要なリアクション



    if message.content.startswith('y!kill'):
        if message.author.id == 446610711230152706:
            await client.logout()
            await sys.exit()
        else:
            embed = discord.Embed(title='権限がありません!!',description='これは開発者専用コマンドです')
            await message.channel.send(embed=embed)

#🔷➖➖➖➖➖➖➖➖➖➖オートアタック➖➖➖➖➖➖➖➖➖➖➖➖🔷

    global yt_channel_id
    if message.content.startswith('y!ch'):
        try:
            channel_id = int(message.content.split()[1])
        except ValueError:
            await message.channel.send('……そんなチャンネル無いんだけど（）')
            return

        channel = client.get_channel(channel_id)
        if not channel:
            await message.channel.send('……そんなチャンネル無いんだけど（）')
            return

        yt_channel_id = channel.id

    global flag
    # メッセージ送信者がBotだった場合は無視だぜ

    if message.content == "ゆいおつかれ":
        flag = False
        await message.channel.send("ん......おつかれ.見返りくらいは欲しいかなって")
    if message.content == "ゆいがんばれ":
        flag = True
        await message.channel.send("あとでご飯の一つでもおごってね")


#🔷➖➖➖➖➖➖➖➖➖➖➖➖オートアタック改➖➖➖➖➖➖➖➖➖➖➖➖🔷


    global atk_ch_id

    if message.content.startswith("y!atkch "):
        print('got the commond')
        atk_ch_id = message.content.split('y!atkch ')[1]
        print('ch='+atk_ch_id)
        atk_ch = client.get_channel(int(atk_ch_id))
        await atk_ch.send('check channel')

        if message.channel.id == atk_ch_id:
            if "攻撃失敗" in message.content:
                await asyncio.sleep(2)
                await atk_ch.send('::atk 失敗失敗(;^ω^)')


    if f'{client.user.display_name}' in message.content:
        if "やられてしまった" in message.content:#🔷YUIの自動復活条件
            def  hellocheck(m):
                return m.content == "の攻撃" and m.author == message.author  and message.channel == m.channel#ここにメッセージが送られてきたチャンネル=最初のメッセージが送られてきたチャンネルという条件
            try:
                reply = await client.wait_for( "message" , check = hellocheck , timeout = 5.0 )
            except asyncio.TimeoutError:
                await message.channel.send( "::i e refill" )
            else:
                await message.channel.send( "::i e refill" )



     
    if message.author.id == 526620171658330112 or message.author.id == 642271360667877386:
        
        if len(message.embeds) != 0:
            
            for embed in message.embeds:
                description = embed.description
                title = embed.title
                if not embed.description:
                    pass
    # descriptionは自身が_EmptyEmbedの時Falseを返すのでここの処理
                else:
                    pass
                    if description.find(f"{client.user.mention}はレベルアップした！"):
                        print("level up")
                        lv = description.split("レベルアップした！")[1]
                        embed = discord.Embed(title="**━↑Lv UP↑━**",description = str(lv),color=discord.Color.green())
                        embed.set_thumbnail(
url='https://cdn.discordapp.com/attachments/635993816297504809/643091559142916109/videotogif_2019.11.10_23.14.46.gif')
                        embed.add_field(name="LVup時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"/"+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=False)
#                        embed.add_field(name="YUI news", value="大幅に改良！\n詳しくはヘルプの第６項から公式鯖へ", inline=True)
                        embed.set_footer(icon_url=client.user.avatar_url, text=f"{client.user}")
                        await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui_lvupログ'))
                        await message.channel.send('```わーい\(* ॑꒳ ॑* \三/ * ॑꒳ ॑*)/レベルが上がったよ!!\n```'+str(lv))                       
                    else:
                        pass

    if message.author.id == 526620171658330112 or message.author.id == 642271360667877386:
        
        if len(message.embeds) != 0:


            for embed in message.embeds:
                description = embed.description
                title = embed.title
                name = embed.name
                value = embed.value
                if not embed.title:
                    pass
    # descriptionは自身が_EmptyEmbedの時Falseを返すのでここの処理
                else:
                    pass
                    if title.find("が待ち構えている"):
                        await message.channel.send('::atk')
                    else:
                        pass

#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.author != client.user:
        reg_res = re.compile(u"y!wt (.+)").search(message.content)
        if reg_res:

          if reg_res.group(1) in citycodes.keys():

            citycode = citycodes[reg_res.group(1)]
            resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
            resp = json.loads(resp.decode('utf-8'))

            msg = "🔹地域\n"
            msg += '　' + resp['location']['city']
            msg += '\n🔹天気\n'
            for f in resp['forecasts']:
              msg += '　' + f['dateLabel'] + ":" + f['telop'] + "\n"

            embed = discord.Embed(title=msg,color = discord.Colour.blue())
            embed.set_thumbnail(url='https://yahoo.jp/box/J3FhL6')
            embed.set_author(name="🌐YUI WEATHER🌐")
            await message.channel.send(embed=embed)

          else:
            await message.channel.send( '・ω・)ggrks')

#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.content.startswith("y!clean "):

        reply = message.content.split('y!clean ')[1]


        if message.author.guild_permissions.administrator:
            await message.channel.purge(limit=int(reply))
            embed = discord.Embed(title="お掃除完了！！",description=(reply)+"のメッセージを消去したよ‪\n(꜆꜄꜆˙꒳˙)꜆꜄꜆ ｵﾗｵﾗ\n遅くなっちゃってごめんね\n(´・ω・`;)",
                                  color=0x2ECC69)
            embed.set_thumbnail(url="https://yahoo.jp/box/N0OpiM")
            await message.channel.send(embed=embed)

        else:
            embed = discord.Embed(title="権限エラー！！",description="管理者権限無しでチャンネル内のログ全部消せたら相当やばいよ私",
                                  color=0x2ECC69)
            embed.set_thumbnail(url="https://yahoo.jp/box/JAzR8X")
            await message.channel.send(embed=embed)

#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.content.startswith("y!poll "):
        await message.delete()
        x = message.content.split(" ",2)
        r = x[1]
        re2 = x[2]
        embed = discord.Embed(title=(r),description=(re2),color=0x2ECC69)#https://i.pximg.net/img-original/img/2015/11/06/00/03/01/53402632_p0.png
        embed.add_field(name = "発言者",value = f"{message.author.mention}")
        embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
        embed.set_author(name="ReYUI ver1.12.2",url="https://discord.gg/nzS5GKM",icon_url="https://yahoo.jp/box/roWwt8")
        s = await message.channel.send(embed=embed)
        [await s.add_reaction(i) for i in ('👍', '👎')]  # for文の内包表記


    if message.content.startswith("y!say3 "):
        await message.delete()
        x = message.content.split(" ",2)
        e = x[1]
        re2 = x[2]
        embed = discord.Embed(title=(e)
        ,description=(re2)
        ,color=0x2ECC69)
        embed.add_field(name = "発言者",value = f"{message.author.mention}\n"+str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒")
        await message.channel.send(embed=embed)

    if message.content.startswith("y!say2 "):
        await message.delete()
        x = message.content.split(" ",2)
        e = x[1]
        re2 = x[2]
        embed = discord.Embed(title=(e)
        ,description=(re2)
        ,color=0x2ECC69)
        await message.channel.send(embed=embed)

    if message.content.startswith("y!say1 "):
        await message.delete()
        reply_one = message.content.split('y!say1 ')[1]
        await message.channel.send(reply_one)


#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.content.startswith("y!report "):

        await message.delete()

        embed = discord.Embed(title='レポート提出完了！',description=f"{message.author.mention}さん\nレポート提出有り難う！\n君のレポートは無事研究所に届けられたよ！",color=0x2ECC69)
        embed.add_field(name="レポート提出時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("y!report "):
        channel_id_report = 629327961132236800
        reply = message.content.split('y!report ')[1]
        embed = discord.Embed(title='レポート内容\n'+(reply),description=f"発言者{message.author.mention}",color=0x2ECC69)
        embed.add_field(name="レポート提出時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=True)
        await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == '【地下室】yuiレポート'))




    # 「すて」と発言したら「::st」が返る処理
    if message.content == 'y!st':
        await message.channel.send('::status window　私のステータスが見たいなんて、君もエッチだな')

    # 「りせ」と発言したら「::re」が返る処理
    if message.content == 'y!re':
        await message.channel.send('::reset')

    if message.content == 'y!atk':
#レスポンスされる運勢のリストを作成
        unsei = ["::atk　てい", "::atk　うりゃ", "::atk　とう", "::atk　はい", "::atk　ほい", "::atk　むん",]
        choice = random.choice(unsei) #randomモジュールでunseiリストからランダムに一つを選出
        await message.channel.send(choice)

    if message.content == 'y!i e':
        await message.channel.send('::i e')

    if message.content == 'y!i i':
        await message.channel.send('::i i \nまあこれもuser指定するのめんどくて作ってないから意味ないけどね')

    if message.content == 'y!i f':
        await message.channel.send('::i f')

    if message.content == 'よしよし':
        value=random.choice(('**………？**',
        '**そう何回もよしよしされたら私勘違いするよ……？**',
        '**セクハラ？**','**……君以外がやってたら殺してるよ**',
        '**なに急に……びっくりするじゃん。いやじゃないけどさ……**',
        '**ちょっと、やめてよ恥ずかしい**',
        '**……素直にありがとうって言えばいいの？**',
        '**？　よくわからないけど、お礼だけ言っておくわ。ありがとう**'))
        await message.channel.send(value)


    if message.content == 'よしよしヾ(・ω・｀)':
        await message.channel.send('''？　よくわからないけど、お礼だけ言っておくわ。ありがとう''')

   # 「まっぷ」と発言したら「::rmap」が返る処理
    if message.content == 'y!rmap':
        await message.channel.send('::rmap')

    # 「ろーる」と発言したら「::role」が返る処理
    if message.content == 'y!role':
        await message.channel.send('::role \nこれ一応作ったけどリアクションで役職選択させるのは\nめんどくさくてつくってないからほぼ意味ないんだよね……')

    # 「あいてむ」と発言したら「::i」が返る処理
    if message.content == 'y!i':
        await message.channel.send('::i')

    # 「ろぐいん」と発言したら「::login」が返る処理
    if message.content == 'y!login':
        await message.channel.send('::login')

    if message.content == 'y!join':
        role = discord.utils.get(message.guild.roles, name='裏寄生隊')#YUI通知
        await message.author.add_roles(role)
        reply = f'{message.author.mention} これで隊員の一人ね'
        await message.channel.send(reply)

    if message.content == 'y!announce':
        role = discord.utils.get(message.guild.roles, name='YUI通知')#YUI通知
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 何か更新あったら呼ぶね'
        await message.channel.send(reply)




    if message.content == "y!kuji":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        num_random = random.randrange(1,5)
        url1 = 'https://cdn.discordapp.com/attachments/635993816297504809/641195024033251328/29_20191105173957.png'
        url2 = 'https://cdn.discordapp.com/attachments/635993816297504809/641196128137904128/29_20191105174422.png'
        url3 = 'https://cdn.discordapp.com/attachments/635993816297504809/641197802436952065/29_20191105174815.png'
        url4 = 'https://cdn.discordapp.com/attachments/635993816297504809/641198139537227776/29_20191105175219.png'
        url5 = 'https://cdn.discordapp.com/attachments/635993816297504809/641200232826142730/29_20191105180042.png'
        await message.channel.send('くじ引いてく？')
        await asyncio.sleep(3)
        embed = discord.Embed(title="**ディスコ神社│御籤コーナー\n( 厂˙ω˙ )厂うぇーい**",description='''がさ
　がさ
　　がさ''',color=0x2ECC69)
        embed.add_field(name='**紙切れがでてきた…！！**',value='さあさあ今日の運勢は……!?')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/635993816297504809/641207863506632715/28_20191105183055.png')
        embed.set_footer(icon_url=message.author.avatar_url, text=f"御籤使用者│{message.author.name}")
        if num_random == 1:
            embed.set_image(url = url1)
            await message.channel.send(embed=embed)
            await message.channel.send('お、大吉!!\nいいねいいね!!')

        elif num_random == 2:
            embed.set_image(url = url2)
            await message.channel.send(embed=embed)
            await message.channel.send('ん、小吉\nまあ凶とかよりはね…?')

        elif num_random == 3:
            embed.set_image(url = url3)
            await message.channel.send(embed=embed)
            await message.channel.send('ん...んん、末吉\nまぁまぁまぁ…ね?')

        elif num_random == 4:
            embed.set_image(url = url4)
            await message.channel.send(embed=embed)
            await message.channel.send('大凶!?\nえ、死ぬの!?')

        elif num_random == 5:
            embed.set_image(url = url5)
            await message.channel.send(embed=embed)
            await message.channel.send('すみませぇえええん\nこの御籤呪われてまあああああああす!!')


    if message.content == 'y!gacha':
        await message.channel.send('gachaばんごうをしていしてね......?')
        embed = discord.Embed(title="ガチャ機能だよ",description="コマンドはy!gacha [ガチャ番号]",color=0x2ECC69)
        embed.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        embed.add_field(name="ガチャ種類＋番号一覧",value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！")
        await message.channel.send(embed=embed)


    if message.content == "y!gacha 1":
        embed = discord.Embed(title="あ、ガチャガチャじゃんまわしてみる？", description=f"""　　ﾁｬﾘｰﾝ
ｶﾞﾁｬｶﾞﾁｬｶﾞﾁｬ
　　　ﾎﾟﾝ！""",
                              color=0x2ECC69)
        embed.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        embed.set_image(url=random.choice(("https://yahoo.jp/box/tpeHgW",
        "https://yahoo.jp/box/roWwt8",
        "https://yahoo.jp/box/M8DDfm",
        "https://yahoo.jp/box/5yaQwS",
        "https://yahoo.jp/box/snmtCk",
        "https://yahoo.jp/box/WI0bCW",
        "https://yahoo.jp/box/2DeZEI",
        "https://yahoo.jp/box/seZwkN",
        "https://yahoo.jp/box/UHhqck",
        "https://yahoo.jp/box/ZdKwTS",
        "https://yahoo.jp/box/coBg_L",
        "https://yahoo.jp/box/D8lFL8",
        "https://yahoo.jp/box/LU1JLi",
        "https://yahoo.jp/box/xfDFnC",
        "https://yahoo.jp/box/2tGQPm",
        "https://yahoo.jp/box/2tGQPm",
        "https://yahoo.jp/box/W6sq6m",
        "https://yahoo.jp/box/o8_WCa",
        "https://yahoo.jp/box/bnadWl",
        "https://yahoo.jp/box/wvFtaX",
        "https://yahoo.jp/box/t6DACy",
        "https://yahoo.jp/box/Iz8VoJ",
        "https://yahoo.jp/box/QqiwDa",
        "https://yahoo.jp/box/XMZ_-6",
        "https://yahoo.jp/box/HYqbOS",
        "https://media.discordapp.net/attachments/635993816297504809/636080181991178250/20_20191022145513.png",
        "https://media.discordapp.net/attachments/635993816297504809/636080191499927552/20_20191022145257.png")))
        embed.add_field(name=random.choice(('最高に需要無いんだけど……', 'うわ何これ……いる？', '……こんなのガチャガチャから出てこないよね普通', 'ごめんちょっと意味わからないんだけどナニコレ', "これもらって喜ぶ人いるのかな", '………ノーコメント')), value='YUIは出てきたものをそっとポッケに入れた', inline=False)
        await message.channel.send(embed=embed)

    if message.content == "y!gacha 2":
        embed = discord.Embed(title="おにゃ……のこ…ガチャ？　取り合えずまわしてみる？", description=f"""　　ﾁｬﾘｰﾝ

　ｶﾞﾁｬｶﾞﾁｬｶﾞﾁｬ

　　　　ﾎﾟﾝ！""",
                              color=discord.Colour.from_rgb(255,133,214))
        embed.set_thumbnail(url="https://yahoo.jp/box/lc5-cP")
        embed.set_image(url=random.choice(("https://yahoo.jp/box/C5OhZ6",
        "https://yahoo.jp/box/7wCPzz",
        "https://yahoo.jp/box/NTtrKt",
        "https://yahoo.jp/box/1lR9DJ",
        "https://yahoo.jp/box/uIdpqC",
        "https://yahoo.jp/box/YQlvC2",
        "https://yahoo.jp/box/sxklm2",
        "https://yahoo.jp/box/LpiAUS",
        "https://yahoo.jp/box/xkG1WU",
        "https://yahoo.jp/box/4T6wmr",
        "https://yahoo.jp/box/WEgd7D",
        "https://yahoo.jp/box/6VLJXh",
        "https://yahoo.jp/box/yDuiFh",
        "https://yahoo.jp/box/gtay8J",
        "https://yahoo.jp/box/-zJbpA",
        "https://yahoo.jp/box/xH_xpw",
        "https://yahoo.jp/box/KQDNjd",
        "https://yahoo.jp/box/XT5J4M",
        "https://yahoo.jp/box/AoWqBP",
        "https://yahoo.jp/box/3CKNvk",
        "https://yahoo.jp/box/pFKU2Z",
        "https://yahoo.jp/box/nH4vvY",
        "https://yahoo.jp/box/cqTkgv",
        "https://yahoo.jp/box/kvCkil",
        "https://yahoo.jp/box/rvDbkR",
        "https://yahoo.jp/box/znUdy5",
        "https://yahoo.jp/box/wmzu-Z",
        "https://yahoo.jp/box/kXnYQf",
        "https://yahoo.jp/box/0cRE1S",
        "https://yahoo.jp/box/Mz2rPI",
        "https://yahoo.jp/box/JzZEBY",
        "https://yahoo.jp/box/o1Uma1",
        "https://yahoo.jp/box/YPaIEe",
        "https://yahoo.jp/box/MANLfg",
        "https://yahoo.jp/box/e09Dte",
        "https://yahoo.jp/box/iFQl2O",
        "https://yahoo.jp/box/EjWQbT",
        'https://yahoo.jp/box/3faN7k',
        'https://yahoo.jp/box/c9L236',
        'https://yahoo.jp/box/Jxj1Jd')))
        embed.add_field(name=random.choice(('いや可愛いけどコメントに困る', 'あ、かわいい', 'ちょくちょくエッチなのは入ってるよねこれ（）', '可愛いというより萌えのほうが正しいのかなこれ', "普通にかわいいこれ", 'あー悪くないかも')), value='YUIは出てきたおにゃのこカードをそっとポケットに仕舞った', inline=False)
        await message.channel.send(embed=embed)





#🔷アイコン表示系コード➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷



    if message.content == "y!myicon":
        embed = discord.Embed(title="**アイコン表示**\n",description = '`アイコンを表示したよ`',color=discord.Color(random.randint(0, 0xFFFFFF)))
        embed.set_image(url=message.author.avatar_url_as(size=1024))
        embed.set_footer(icon_url=message.author.avatar_url, text=f"表示者│{message.author}")
        await message.delete()
        await message.channel.send(embed=embed)

#🔷サイコロ系コード➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷



    if message.content.startswith("y!dice "): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            x = message.content.split(" ",2)
            dice = x[1]
            dice2 = x[2]
            num_random = random.randrange(int(dice),int(dice2))
            embed = discord.Embed(title="ゆいがサイコロ振るだけ",description='''指定範囲は'''+(dice)+'から'+(dice2)+'!!\n'+'''なにがでるかなー

**__　'''+str(num_random)+''' __**٩( 'ω' )و!!''',color=0x2ECC69)
            await message.channel.send(embed=embed)


    if message.content.startswith("y!nekoshima"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,10000)
            embed = discord.Embed(title="YUIの超激レア占い",description='''次の超激レア枠は～!!
**'''+str(num_random)+'''**体後!!　がんばー٩( 'ω' )و''',color=0x2ECC69)
            embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k',
        'https://yahoo.jp/box/c9L236',
        'https://yahoo.jp/box/Jxj1Jd')))
            await message.channel.send(embed=embed)


    if 'おつ' in message.content or '乙' in message.content or 'ｵﾂ' in message.content or 'オツ' in message.content:
        if message.author.bot:
           pass

        else:
            channel = message.channel
            oha = random.choice(('(\*´ω｀*)ｵﾂｶﾚｻﾏー','‪(꜆꜄꜆˙꒳˙)꜆꜄꜆ ｵﾂｵﾂｵﾂ‬','( 厂˙ω˙ )厂うぇーい','おつかれさまぁ～  (\*ˊ˘ˋ*)♪','おつおつ( ´꒳`)','おつ(　ˆᴘˆ　)'))

            await channel.send(oha)



    if 'オハ' in message.content or 'ｵﾊ' in message.content or 'oha' in message.content or 'おは' in message.content:
        if message.author.bot:

             return

        else:
            channel = message.channel
            oha = random.choice(('おはー(((o(\*ﾟ▽ﾟ*)o)))','(ฅ・ω・ฅ)おはよう♪','⸜(\* ॑꒳ ॑*  )⸝⋆*オハ','おは(　ˆᴘˆ　)'))

            await channel.send(oha)



    if 'おやす' in message.content or 'スヤァ' in message.content or 'oyas' in message.content or 'ｽﾔｧ' in message.content or 'ねる' in message.content or '寝る' in message.content:
        if message.author.bot:

             return

        else:
            channel = message.channel
            oha = random.choice(('( ˘ω˘ ) ｽﾔｧ…','( ˘꒳​˘ )ｵﾔｽﾔｧ…','_([▓▓] ˘ω˘ )_ｽﾔｧ…','=͟͟͞( ˘ω˘)˘ω˘)˘ω˘)ｼﾞｪｯﾄｽﾄﾘｰﾑｽﾔｧ…','ｽﾔｧ…(　ˆᴘˆ　)'))

            await channel.send(oha)




#🔷ログ系コード➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷

    if message.content.startswith("y!yui"):
        if message.content.split()[1] == "log":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='yui起動ログ')
            reply = f'{new_channel.mention} をつくったよ。私が起きたら此処で挨拶するから'
            return await message.channel.send(reply)

        elif message.content.split()[1] == "timelog":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='yui時報ログ')
            reply = f'{new_channel.mention} をつくったよ。日付が変わるタイミングでここでお知らせするから'
            
        
        elif message.content.split()[1] == "global":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='global_yui')
            reply = f'{new_channel.mention} をつくったよ。globalチャットに登録完了'
            return await message.channel.send(reply)
#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷

    if message.content == "y!timer":
        await message.delete()
        tmp = await message.channel.send("10") # 編集するメッセージを保持
        await asyncio.sleep(1)
        await tmp.edit( content = "9" )
        await asyncio.sleep(1)
        await tmp.edit( content = "8" )
        await asyncio.sleep(1)
        await tmp.edit( content = "7" )
        await asyncio.sleep(1)
        await tmp.edit( content = "6" )
        await asyncio.sleep(1)
        await tmp.edit( content = "5" )
        await asyncio.sleep(1)
        await tmp.edit( content = "4" )
        await asyncio.sleep(1)
        await tmp.edit( content = "3" )
        await asyncio.sleep(1)
        await tmp.edit( content = "2" )
        await asyncio.sleep(1)
        await tmp.edit( content = "1" )
        await asyncio.sleep(1)
        await tmp.edit( content = "0" )

    if message.content == "y!gorogoro":
        await message.delete()
        tmp = await message.channel.send("(:3\_ヽ)_......") # 編集するメッセージを保持
        await asyncio.sleep(1)
        await tmp.edit( content = "(:3\_ヽ)_......ねむいい......" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　( ε: )" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　(.ω.)" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　　　( :3 )" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　　  　('ω')" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　　 　　　(:3\_ヽ)_...." )
        await asyncio.sleep(3)
        await tmp.edit( content = ".　　　　　　　　 　(:3\_ヽ)_....なにがしたかったんだろ" )



    if message.content == "y!amanohashi":
        await message.delete()
        await message.channel.send("私の生みの親だね。まあどうでもいいけどね！")



    if message.content == "y!slot s":
        kakuritu = random.randint(1, 50)
        slot_list = [':eggplant:', ':cherries:', ':large_orange_diamond:', ':large_blue_diamond:', ':seven:',':gem:',':bell:',':eggplant:',':eggplant:',':eggplant:']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(kakuritu) == int(1): #確率は1/50に設定（出来てるはず）
            await message.channel.send("これは何かが起こる予感…Σ(ﾟ□ﾟ；)\n\n\n")
            A = slot_list[4]
            B = slot_list[4]
            C = slot_list[4]
            await asyncio.sleep(3) #3秒間待ってやる
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':seven:':
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー\nなかなかすごいよ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':eggplant:':
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="very KI☆TA☆NA☆I！！",value="汚らわしいねーｗ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':bell:':
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="三連ベル！！",value="いいねー")
            await message.channel.send(embed = embed)

        elif A == ':cherries:' and B != ":cherries:" and C != ":cherries:":
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単チェリー！！",value="ヨキヨキ")
            await message.channel.send(embed = embed)

        elif A == ':bell:' and B != ":bell:" and C != ":bell:":
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単ベル！！",value="(ノ・ω・)ノオオオォォォ-")
            await message.channel.send(embed = embed)


        elif A == B and B == C :
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="BINGO！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        else:
            tmp = await message.channel.send("10") #    　


            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="残念……",value="もっかいやる？")
            await message.channel.send(embed = embed)


    if message.content == "y!slot c":
        kakuritu = random.randint(1, 50)
        slot_list = [':eggplant:', ':cherries:', ':large_orange_diamond:', ':large_blue_diamond:', ':seven:',':gem:',':bell:',':eggplant:',':eggplant:',':eggplant:']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(kakuritu) == int(1): #確率は1/50に設定（出来てるはず）
            await message.channel.send("これは何かが起こる予感…Σ(ﾟ□ﾟ；)\n\n\n")
            A = slot_list[4]
            B = slot_list[4]
            C = slot_list[4]
            await asyncio.sleep(3) #3秒間待ってやる
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':seven:':
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー\nなかなかすごいよ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':eggplant:':
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="very KI☆TA☆NA☆I！！",value="汚らわしいねーｗ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':bell:':
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="三連ベル！！",value="いいねー")
            await message.channel.send(embed = embed)

        elif A == ':cherries:' and B != ":cherries:" and C != ":cherries:":
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単チェリー！！",value="ヨキヨキ")
            await message.channel.send(embed = embed)

        elif A == ':bell:' and B != ":bell:" and C != ":bell:":
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単ベル！！",value="(ノ・ω・)ノオオオォォォ-")
            await message.channel.send(embed = embed)


        elif A == B and B == C :
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="BINGO！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        else:
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="残念……",value="もっかいやる？")
            await message.channel.send(embed = embed)


    if message.content == 'y!sinfo':

        guild = message.guild
        role = next(c for c in guild.roles if c.name == '@everyone')
        t_locked = 0
        v_locked = 0
        online = 0
        offline = 0
        idle = 0
        dnd = 0
        pin = 0
        if guild.mfa_level == 0:
            mfamsg = "メンバーに2要素認証を必要としていません"
        else:
            mfamsg = "メンバーに2要素認証を必要としています"
        if guild.premium_subscription_count == None:
            pmmc = "0"
        else:
            pmmc = guild.premium_subscription_count
        for member in guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.status == discord.Status.dnd:
                dnd += 1
        for channel in guild.text_channels:
            if channel.overwrites_for(role).read_messages is False:
                t_locked += 1
        for channel in guild.voice_channels:
            if channel.overwrites_for(role).connect is False:
                v_locked += 1
        total = online+offline+idle+dnd
        if total > 499:
            large = "大"
        elif total > 249:
            large = "中"
        else:
            large = "小"
        embed = discord.Embed(title=f"サーバー情報", color=0x2ECC69)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="‣サーバー名", value=f"**{guild.name}**",inline=False)
        embed.add_field(name="‣サーバーの説明", value=f"**{guild.description}**",inline=False)
        embed.add_field(name="‣サーバーID", value=f"**{guild.id}**")

        embed.add_field(name="‣サーバーの大きさ", value=f"**{large}**")
        embed.add_field(name="‣サーバー地域", value=f"**{guild.region}**")
        embed.add_field(name="‣サーバーの旗", value=f"**{guild.banner}**")
        embed.add_field(name="‣オーナー", value=f"**{guild.owner.mention}**",inline=False)
        embed.add_field(name="‣チャンネル数", value=f"総合チャンネル数　:**{len(guild.text_channels)+len(guild.voice_channels)}個**(🔒×**{t_locked+v_locked}**)\nテキストチャンネル:**{len(guild.text_channels)}個**(🔒×**{t_locked}**)\nボイスチャンネル　:**{len(guild.voice_channels)}個**(🔒×**{v_locked}**)")
        embed.add_field(name="‣カテゴリー数", value=f"**全て:{len(guild.categories)}**")
        embed.add_field(name="‣役職数", value=f"**{len(guild.roles)}職**",inline=False)
        embed.add_field(name="‣メンバー数", value=f"総メンバー:**{total}人**\nオンライン:**{online}人**\nオフライン:**{offline}人**\n退席中　　:**{idle}人**\n取り込み中:**{dnd}人**",inline=False)
        embed.add_field(name="‣サーバーのブースト状態", value=f"サーバーブーストレベル　:**Lv.{guild.premium_tier}**\nサーバーブーストユーザー:**{pmmc}人**",inline=False)
        embed.add_field(name="‣二段階認証", value=f"**{mfamsg}**",inline=False)
        await message.channel.send(embed=embed)

#🔷➖➖➖➖➖➖➖➖global chat space➖➖➖➖➖➖➖➖🔷




    if client.user != message.author and message.channel.name == "global_yui" and not "discord.gg" in message.author.name:
        content = ""
        for msg in message.content.split():
            if "http://" in message.content or"https://" in message.content or"discord.gg" in message.content:
                re.sub(r"(https://discord.gg/)([a-zA-Z]*)",r"||\1\2||",message.content)
                content = f"{message.content} ||{msg}||"
            else:
                content = f"{message.content} {msg}"
        embed = discord.Embed(title=f'送信者│{message.author}',description=f"{message.content}",color=discord.Color(random.randint(0, 0xFFFFFF)))
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.set_author(icon_url=message.guild.icon_url, name=f"{message.guild.name}")
        embed.set_footer(icon_url=client.user.avatar_url, text=f"YUI global chat system")
        await message.delete()
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == "global_yui":
                    await channel.send(embed=embed)

    if message.content.startswith("y!mkch "):
        await message.delete()
        reply_one = message.content.split('y!mkch ')[1]
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name=reply_one)
        reply = f'{new_channel.mention} を作成したよ!'

        await message.channel.send(reply)

    if message.content.startswith('y!send '):

        await message.delete()
        x = message.content.split(" ",2)
        riptext2 = int(x[2])
        channel = client.get_channel(riptext2)
        riptext = x[1]
#        riptext3 = x[3]
#        riptext4 = x[4]
#        riptext5 = x[5]
 #       embed = discord.Embed(title = riptext,description = riptext2,color=random.randint(0x000000, 0xFFFFFF))
#        embed.add_field(name = riptext2 , value = riptext3)
#        embed.add_field(name = riptext4 , value = riptext5)

        await channel.send(riptext)




#        kakuritu = random.randint(1, 50)
     #   slot_list = [':eggplant:', ':cherries:', ':large_orange_diamond:', ':large_blue_diamond:', ':seven:',':gem:',':bell:',':eggplant:',':eggplant:',':eggplant:']
   #     A = random.choice(slot_list)
#        B = random.choice(slot_list)
      #  C = random.choice(slot_list)



    if client.user != message.author:
        kakuritu = random.randint(1, 20)
        if int(kakuritu)== 1:
            Z = ['あんぱん','メロンパン','フランスパン','チョコパイ']
            A = random.choice(Z)
            AZ = ['チョコ','粒あん','バター','しゃけ','ケチャップ']
            B = random.choice(AZ)
            C = ["知り合い","友達","マックで見かけた人","モスで見かけた人","たまたま電車で乗り合わせた人"]
            CC = random.choice(C)
            random_dana = ['お腹すいたなぁ…','ねえ\nだいぶ前に'+(CC)+'がやってたんだけど…'+(A)+'って'+(B)+'とあうの?','**プリン**に**醤油**をかけると**うにの味**って言うけど\nこれ式で表すと\n__**プリン味＋醤油味=うに味**__\nだよね\nじゃあさ、この式から\n__**うに味－醤油味=プリン味**__\nってことになるよね。\nつまりうにから醤油系の味成分を抽出しまくればいつかプリン味になるのかな!....?','フランスにはtaoという名前のペットボトル飲料がある','( 厂˙ω˙ )厂うぇーい','''＿人人人人人人人人＿\n＞ 突　然　の　死 ＜\n￣^Y^Y^Y^Y^Y^Y^Y￣''','(((((((((((っ･ω･)っ ｳｪｰｲ♪','| ε:)   にゅ','(^ω^≡^ω^).','( ˙꒳​˙  )ﾌｧｯ','|ω・)ﾐﾃﾏｽﾖ','(  ﾟཫ ﾟ)ｺﾞﾌｯ']
            text_random = random.choice(random_dana)
            await message.channel.send(text_random)
            print('selected')

    if client.user != message.author:
    	if 'だよ' in message.content:
            aaa = ["そうなの？","そうだよ(便乗)"]
            AAA = random.choice(aaa)
            await message.channel.send(AAA)
    	if 'した' in message.content:
    	    await message.channel.send('そうなんだ...(困惑)')
    	if 'なの' in message.content and '？' in message.content:
    		await message.channel.send('そうだよ(便乗)')

    if client.user != message.author:
    	if 'くえー' in message.content:
    		y1 = ['……結構恥ずかしいからねこれ','…ごめん自分で反応しといてあれだけど、結構恥ずい','……はずいわ!','\nいやぁぁこれ言うの恥ずかしいからいやぁぁぁ','……それ言われたら反応しないといけないからやめて','\nなんでこんな恥ずいのに私が反応しなきゃ行けないの…']
    		y2 = random.choice(y1)
    		await message.channel.send('く、くえー…'+(y2))

    if client.user != message.author:
    	if 'ねこ' in message.content:
    		y1 = ['ねこですよろしくおねがいします','ねこはいましたよろしくおねがいします','ねこはいます','ねこはいました','ねこはどこにでもいます','ねこはここにいます']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))
    if client.user != message.author:
    	if 'せやな' in message.content:
    		y1 = ['そやな']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))

    if client.user != message.author:
    	if 'うぃ' in message.content or 'うぇ' in message.content:
    		y1 = ['( 厂˙ω˙ )厂うぇーい']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))
    if client.user != message.author:
    	if 'くさ' in message.content or '草' in message.content:
    		y1 = ['w','www','草','𐤔𐤔𐤔','ʬ﻿ʬʬ﻿','෴෴']
    		y2 = random.choice(y1)#(　＾ω＾)おっおっおっ
    		await message.channel.send((y2))
    	if 'おっ' in message.content:
    		y1 = ['(　＾ω＾)おっおっおっ','( ˙꒳​˙    ≡   ˙꒳​˙  )おっおっおっ','(　＾ω＾)ｵｯw']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))

    if client.user != message.author:
    	if 'ぽ' in message.content or 'ポ' in message.content:
    		y1 = ['㌼㌨㌥㌑㌝㌈㌏㌐　㌞㌞㌞㌞㌑㌆']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))

    if client.user in message.mentions: # 話しかけられたかの判定
        embed = discord.Embed(title = 'YUI Information',description = f'{client.user}\nID 627052576810074112')
        embed.set_author(name=client.user,url="https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=8&scope=bot",icon_url=client.user.avatar_url)
        embed.set_footer(icon_url=message.author.avatar_url, text=f"表示者｜{message.author}")
        await message.channel.send(embed = embed)








client.run(TOKEN)

