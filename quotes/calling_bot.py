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
        if "かわいい" in m.content or "可愛い" in m.content:
            quotes = [
                [100, "いやだな照れちゃうじゃないですか！"],
                [100, "かわいいって言われるの・・・嬉しいな・・・"],
                [100, "ほんとにかわいいって思ってくれてます～？ほんとにぃ～？"]
            ]
            t = get_quotes(quotes)
        
        
        if "犯す" in m.content or "犯したい" in m.content or "ヤりたい" in m.content or "ヤらせろ" in m.content or "おかす" in m.content:
            quotes = [
                [100, "あ、あの？目が本気ですよ・・・？"],
                [100, "だ、だめですよそんなハレンチな！"],
                [100, "そ、そういえば私ちょっと用事があるので席外していいですか・・・？"]
            ]
            t = get_quotes(quotes)
        
        if "殺す" in m.content or "殺したい" in m.content:
            quotes = [
                [100, "さ、サツガイヨコクは捕まっちゃうんだぞぉ・・・"],
                [100, "リョナラーだからそういう気持ちは分かるんですけど、や、やめましょ？"],
                [100, "目が怖い！目が怖いですって！"]
            ]
            t = get_quotes(quotes)
        
        if "黙って" in m.content or "だまって" in m.content or "うるさい" in m.content or "静かに" in m.content or "しずかに" in m.content or "黙れ" in m.content or "だまれ" in m.content:
            quotes = [
                [100, "え、うるさかったですか・・・？ごめんなさい・・・"],
                [100, "す、すいません・・・"],
                [100, "あ、あの・・・もしかして私のお腹殴ります・・・？"]
            ]
            t = get_quotes(quotes)
        
    return t
