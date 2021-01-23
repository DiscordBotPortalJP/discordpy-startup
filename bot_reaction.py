import random

def get_bot_reaction(msg) :
    reaction = ""
    #挨拶
    reaction = greetings(msg)
    if reaction != "":
        return reaction
    
    #下ネタは30%の確率で反応
    if random.randint(0, 100) < 30:
        reaction = shimoneta(msg)
    
    return reaction

def greetings(m):
    t = ""
    if m.content == "おはー":
        t = m.author + "さんおはー"
    if "おはよ" in m.content:
        t = "おはようございます！"
    if m.content == "こんー":
        t = "こん～"
    if "こんにち" in m.content:
        t = "こんにちは！"
    if "こんば" in m.content:
        t = "こんばんは！"
    if "おやす" in m.content:
        t = "寝るんですか？私も寝たい！おやすみ！"
    return t

def shimoneta(m):
    t = ""
    if "おっぱい" in m.content:
        t = "おっぱい！"
    if "まんこ" in m.content:
        t = "おまんこ！"
    if "アナル" in m.content:
        t = "アナル！"
    return t
