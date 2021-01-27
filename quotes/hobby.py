from mylib.mymodule import get_quotes
#趣味
def get_hobby(m):
    t = ""
    if "ドーモ" in m.content or "ニンジャ" in m.content or "アイサツ" in m.content:
        quotes = [
            [100, "ドーモ、" + m.author.name + "＝サン。リョナゲボットです。"],
            [100, "ニンジャナンデ！？"]
        ]        
        t = get_quotes(quotes)
    if m.content == "ぼふんぼふん":
        quotes = [
            [100, "ぼふんぼふん"],
            [30, "ほらもっと啼いてごらんなさい？厚かましいげっ歯類めが！！"],
            [100, "ヴォフンヴォフン"]
        ]
        t = get_quotes(quotes)
    return t
