import random
def get_bot_reaction(msg) :
    reaction = ""
    #挨拶
    reaction = greetings(msg)
    if reaction != "":
        return reaction
    
    #下ネタは30%の確率で反応
    if random.randint(0, 100) < 30:
        return shimoneta(msg)
    
    return reaction

def greetings(m):
    if m.content == "おはー":
        return "おはー"
    if "おはよ" in m.content:
        return "おはようございます！"
    if m.content == "こんー":
        return "こん～"
    if "こんにち" in m.content:
        return "こんにちは！"
    if "こんば" in m.content:
        return "こんばんは！"
    return ""

def shimoneta(m):
    if "おっぱい" in m.content:
        return "おっぱい！"
    if "まんこ" in m.content:
        return "おまんこ！"
    if "アナル" in m.content:
        return "アナル！"
    return ""
