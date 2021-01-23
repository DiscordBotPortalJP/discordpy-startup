import random

def get_bot_reaction(msg) :
    reaction = ""
    #挨拶
    reaction = greetings(msg)
    if reaction != "":
        return reaction
    
    #下ネタは30%の確率で反応
    if random.randint(0, 100) < 100:
        reaction = shimoneta(msg)
    
    return reaction

#挨拶
def greetings(m):
    t = ""
    if m.content == "おはー":
        t = m.author.name + "さんおはー"
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

#下ネタ
def shimoneta(m):
    t = ""
    #コピペ用[100, ""],
    if "おっぱい" in m.content:
        quotes = [
            [100, "おっぱい！"],
            [100, "おっぱいおっぱい"],
            [100, m.author.name + "さんっておっぱい大好きですよね"]
        ]
        t = get_quotes(quotes)
        
    if "まんこ" in m.content:
        quotes = [
            [100, "おまんこ！"],
            [100, "やだなぁエッチなんだから・・・"],
            [100, "おまんこなんて言ってたら引かれちゃいますよ？"]
        ]
        t = get_quotes(quotes)
        
    if "アナル" in m.content:
        quotes = [
            [100, "アナル！"],
            [100, m.author.name + "さんもアナル好きなんですか？"],
            [100, "お尻は繊細ですから、優しく使わないと切れちゃいますよ？"],
        ]
        t = get_quotes(quotes)
    return t

#配列から確率でセリフを取り出す
def get_quotes(q_list):
    total_weight = 0
    for i in q_list:
        total_weight += i[0]
    
    #順番に確率に当てはまるかやっていく
    target = q_list[0]
    for i in q_list:
        if  random.randint(0, total_weight) <= i[0]:
            target = i
            break
        total_weight -= i[0]
    return target[1]
        
