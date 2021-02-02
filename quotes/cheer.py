from mylib.mymodule import get_quotes

#慰める
def get_cheer(m):
    t = ""
    if m.content == "疲れた" or m.content == "もう疲れた" or "もうやだ" in m.content or "もうだめ" in m.content:
        quotes = [
            [100, "休むのは大事ですよ"],
            [100, "頑張ってください！"],
            [100, "気分転換でもしましょう？"]
        ]        
        t = get_quotes(quotes)
        
    if "褒めて" in m.content or "褒めろ" in m.content:
        quotes = [
            [100, "えらいっ"],
            [100, "すごいですね！"],
            [100, "<:iizo:805748601972195328> "],
            [100, "よくやった！"]
        ]        
        t = get_quotes(quotes)
        
    if m.content == "死にたい" or m.content == "もう死にたい":
        quotes = [
            [100, "そんなこと言わないでください・・・"],
            [100, m.author.name + "さんに死んでほしくない人はきっとたくさんいますよ"],
            [100, "死んじゃだめですよ・・・"]
        ]        
        t = get_quotes(quotes)
        
    return t
