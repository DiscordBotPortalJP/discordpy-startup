import ..mylib.mymodule
#挨拶
def greetings(m):
    t = ""
    if m.content == "おはー" or "おはよ" in m.content:
        quotes = [
            [100, "おはー"],
            [100, m.author.name + "さんおはー"],
            [100, "おはよ～"]
        ]
        t = mymodule.get_quotes(quotes)
        
    if m.content == "こんー":
        quotes = [
            [100, "こんー"],
            [100, "こんこん"],
            [100, "こん～"]
        ]
        t = mymodule.get_quotes(quotes)
        
    if "こんにち" in m.content:
        quotes = [
            [100, "こんにちは！"],
            [100, "こんにちー"]
        ]
        t = mymodule.get_quotes(quotes)
        
    if "こんば" in m.content:
        quotes = [
            [100, "こんばんは！"],
            [100, "こんばんはー"],
            [100, "こん～"]
        ]
        t = mymodule.get_quotes(quotes)
        
    if "はじめまして" in m.content:
        quotes = [
            [100, "はじめまして！よろしくね！"],
            [100, "はじめまして～"]
        ]
        t = mymodule.get_quotes(quotes)
        
    if "おやす" in m.content:
        quotes = [
            [100, "おやすみなさい～"],
            [100, "寝るんですか？私も寝たい！おやすみ！"],
            [100, "睡眠は大事ですよ！"],
            [100, "寝るおやす！"]
        ]
        t = mymodule.get_quotes(quotes)
    return t
