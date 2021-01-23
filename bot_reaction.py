import random
def get_bot_reaction(msg) :
    reaction = ""
    if 30 < random.randint(0, 100):
        return reaction
    if "おっぱい" in msg:
        reaction = "おっぱい！"
    if "まんこ" in msg:
        reaction = "おまんこ！"
    if "アナル" in msg:
        reaction = "アナル！"
    return reaction
