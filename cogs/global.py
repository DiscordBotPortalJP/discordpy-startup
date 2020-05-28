import discord
from discord.ext import commands
import json

class global(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    async def all_ban(self, uid, *, reason):
        user = await self.bot.fetch_user(int(uid))
        
        if reason == None:
            reason = None
        else:
            reason = reason
        
        for g in self.bot.guilds:
            try:
                await g.ban(user, reason=reason)
            except:
                pass
    
    #globalban
    @commands.command(aliases=["gban"])
    async def globalban(self, ctx, uid, bool, *, reason):
        e = discord.Embed(title="GlobalBan", description="処理中...", color=0x2ecc71)
        msg = await ctx.send(embed=e)
        
        if ctx.author.id in self.bot.teams or ctx.author.id in self.bot.gbans:
            pass
        else:
            e.description = None
            e.add_field(name="エラー", value="このコマンドは使用できません。")
            await msg.edit(embed=e)
            return
        
        with open("globalban.json", 'r', encoding="utf-8") as f:
            gb = json.load(f)
        
        if uid == None:
            e.description = None
            e.add_field(name="エラー", value="ユーザーIDを入力してください。")
            await msg.edit(embed=e)
            return
        else:
            uid = int(uid)
        
        if reason == None:
            e.description = None
            e.add_field(name="エラー", value="reasonを入力してください。")
            await msg.edit(embed=e)
            return
        else:
            reason = reason
        
        if bool == None:
            e.description = None
            e.add_field(name="エラー", value="TrueかFalseを入力してください。")
            await msg.edit(embed=e)
            return
        elif bool == "True":
            bool = True
        elif bool == "False":
            bool = False
        else:
            e.description = None
            e.add_field(name="エラー", value="TrueかFalseを入力してください。")
            await msg.edit(embed=e)
            return
        
        if gb.get(str(uid)) == None:
            try:
                u = await self.bot.fetch_user(uid)
                e.description = None
                e.add_field(name="新規グローバルBan", value=f"{u} ({u.id}) をグローバルBanしました。")
                gb[uid] = {'name':u, 'ban':True, 'reason':reason}
                await msg.edit(embed=e)
                with open("globalban.json", 'w', encoding="utf-8") as fr:
                    json.dump(gb, fr)
            except:
                e.description = None
                e.add_field(name="エラー", value="グローバルBanできませんでした。")
                e.add_field(name="詳細", value=f"```{traceback.format_exc(3)}```", inline=False)
                await msg.edit(embed=e)
        else:
            try:
                u = self.bot.fetch_user(uid)
                e.description = None
                e.add_field(name="新規グローバルBan", value=f"{u} ({u.id}) をグローバルBanしました。")
                await msg.edit(embed=e)
                gb[uid]['name'] = u
                gb[uid]['ban'] = bool
                gb[uid]['reason'] = reason
                with open("globalban.json", 'w', encoding="utf-8") as fr:
                    json.dump(gb ,fr)
            except:
                e.description = None
                e.add_field(name="エラー", value="グローバルBanできませんでした。)
                await msg.edit(embed=e)

def setup(bot):
    bot.add_cog(global(bot))
