import discord
from discord.ext import commands
import asyncio
import traceback
import inspect
import textwrap
import io

class evals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #eval
    @commands.command()
    async def eval(self,ctx,*,cmd):
        if ctx.author.id in self.bot.teams:
            kg="\n"
            txt=f'async def evdf(ctx,bot):{kg}{kg.join([f" {i}" for i in cmd.replace("```py","").replace("```","").split(kg)])}'
            try:
                exec(txt)
                await eval("evdf(ctx,self.bot)")
                await ctx.message.add_reaction("✅")
            except:
                await ctx.message.add_reaction("❌")
                await ctx.author.send(embed=discord.Embed(title="Eval Command Error",description=f"```{traceback.format_exc(3)}```"))
        else:
            await ctx.send("> このコマンドは使用できません。")

def setup(bot):
    bot.add_cog(evals(bot))
