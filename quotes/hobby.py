from mylib.mymodule import get_quotes
#趣味
def get_hobby(m):
    t = ""
    if "ドーモ" in m.content or "ニンジャ" in m.content or "アイサツ" in m.content or "アイエ" in m.content:
        quotes = [
            [100, "ドーモ、" + m.author.name + "＝サン。リョナゲボットです。"],
            [100, "ワッザ！？"],
            [100, "アイエッ！？"],
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
        
    if "尻尾" in m.content or "しっぽ" in m.content:
        quotes = [
            [100, "尻尾があると走る時結構便利なんですよ"],
            [100, "尻尾は背骨の延長なので、強く引っ張らないでくださいね？死んじゃうから"],
            [100, "ほら尻尾ありますよ？もふもふですよ？"]
        ]
        t = get_quotes(quotes)
        
    if "ネコミミ" in m.content or "猫耳" in m.content or "ネコ耳" in m.content or "獣耳" in m.content or "ケモミミ" in m.content or "ケモノミミ" in m.content:
        quotes = [
            [100, "私にも猫耳生えてますよ！ほらほら、触りますか？"],
            [100, "ケモミミとか好きなんですか？"],
            [100, "猫耳生えてる分脳みそ少ないんじゃないの？とか言う人がいるんですよね！失礼しちゃう！"]
        ]
        
    if "ネコ" in m.content or "猫" in m.content or "にゃー" in m.content or "にゃん" in m.content:
        quotes = [
            [100, "にゃー！"],
            [100, "にゃんにゃん！"]
        ]
        t = get_quotes(quotes)
    return t
