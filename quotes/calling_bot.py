from mylib.mymodule import get_quotes
#呼びかける
def calling_bot(m):
    t = ""
    if "BOTちゃん" in m.content or "ＢＯＴちゃん" in m.content or "botちゃん" in m.content or "ボットちゃん" in m.content:
        quotes = [
            [100, "呼びました？"],
            [100, "私ですか？"],
            [100, "なんですか？"]
        ]        
        t = get_quotes(quotes)
        
    return t
