from mylib.mymodule import get_quotes
#BOTちゃんに呼びかける
def get_calling_bot(m):
    t = ""
    if "BOTちゃん" in m.content or "ＢＯＴちゃん" in m.content or "botちゃん" in m.content or "ボットちゃん" in m.content:
        quotes = [
            [100, "呼びました？"],
            [100, "私ですか？"],
            [100, "ひょっとして" + m.author.name + "さん、私のこと好きなんですか？"],
            [100, "なんですか？"]
        ]        
        t = get_quotes(quotes)
        
        #更になにか入っていたら反応
        if "かわいい" in m.content or "可愛い":
            quotes = [
                [100, "いやだな照れちゃうじゃないですか！"],
                [100, "かわいいって言われるの・・・嬉しいな・・・"],
                [100, "ほんとにかわいいって思ってくれてます～？ほんとにぃ～？"]
            ]
        
    return t
