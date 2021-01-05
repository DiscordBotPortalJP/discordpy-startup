import random

import discord
from discord.ext import commands
from cerberus import Validator

class MakeTeam:

    def __init__(self):
        self.channel_mem = []
        self.mem_len = 0
        self.vc_state_err = '実行できません。ボイスチャンネルに入ってコマンドを実行してください。'

    def set_mem(self, ctx):
        state = ctx.author.voice # コマンド実行者のVCステータスを取得
        if state is None: 
            return False

        self.channel_mem = [i.name for i in state.channel.members] # VCメンバリスト取得
        self.mem_len = len(self.channel_mem) # 人数取得
        return True

    # チーム数を指定した場合のチーム分け
    def make_party_num(self, ctx, party_num, remainder_flag='false'):
        team = []
        remainder = []
        
        if self.set_mem(ctx) is False:
            return self.vc_state_err

        # 指定数の確認
        if party_num > self.mem_len or party_num <= 0:
            return '実行できません。チーム分けできる数を指定してください。(チーム数を指定しない場合は、デフォルトで2が指定されます)'

        # メンバーリストをシャッフル
        random.shuffle(self.channel_mem)

        # チーム分けで余るメンバーを取得
        if remainder_flag:
            remainder_num = self.mem_len % party_num
            if remainder_num != 0: 
                for r in range(remainder_num):
                    remainder.append(self.channel_mem.pop())
                team.append("=====余り=====")
                team.extend(remainder)

        # チーム分け
        for i in range(party_num): 
            team.append("=====チーム"+str(i+1)+"=====")
            team.extend(self.channel_mem[i:self.mem_len:party_num])

        return ('\n'.join(team))

    # チームのメンバー数を指定した場合のチーム分け
    def make_specified_len(self, ctx, specified_len):
        team = []
        remainder = []

        if self.set_mem(ctx) is False:
            return self.vc_state_err

        # 指定数の確認
        if specified_len > self.mem_len or specified_len <= 0:
            return '実行できません。チーム分けできる数を指定してください。'

        # チーム数を取得
        party_num = self.mem_len // specified_len

        # メンバーリストをシャッフル
        random.shuffle(self.channel_mem)

        # チーム分けで余るメンバーを取得
        remainder_num = self.mem_len % party_num
        if remainder_num != 0: 
            for r in range(remainder_num):
                remainder.append(self.channel_mem.pop())
            team.append("=====余り=====")
            team.extend(remainder)

        # チーム分け
        for i in range(party_num): 
            team.append("=====チーム"+str(i+1)+"=====")
            team.extend(self.channel_mem[i:self.mem_len:party_num])

        return ('\n'.join(team))