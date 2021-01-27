from mylib.mymodule import get_quotes
#リョナ
def get_ryona(m):
    t = ""
    if "四肢切断" in m.content:
        quotes = [
            [100, "四肢がなければ軽くなりますね！"],
            [100, "指詰めただけでも傷がその後の人生ずっとめっちゃ痛くてつらいらしいのに、四肢なんてどうなっちゃうんでしょうね？"],
            [100, "オナホにでもしますか？"]
        ]        
        t = get_quotes(quotes)
        
    if "ギロチン" in m.content or "クビチョンパ" in m.content or "首チョンパ" in m.content or "斬首" in m.content:
        quotes = [
            [100, "首チョンパいいですよね・・・なんというか「死んだ」って感じで"],
            [100, "まだ使える"],
            [100, "バッサリ落ちるのもいいけど、切れない刃物で何度も切りつけられるのも好き"]
        ]        
        t = get_quotes(quotes)
        
    if "首絞め" in m.content:
        quotes = [
            [100, "首を絞めてエッチするとなんか脳内物質が出て気持ちいいんですって！"],
            [100, "首を絞められて半死半生になってるかわいいですよね"]
        ]        
        t = get_quotes(quotes)
        
    if "腹パン" in m.content:
        quotes = [
            [100, "腹パンいいですよね・・・ん、その手は何ですか"],
            [100, "お腹といっても鳩尾や下腹などありますが、どこ殴られても痛いんですよ"],
            [100, "腹パンはライトだから初心者にもオススメですよね！"],
            [100, "また殴るつもりですか！私を！"]
        ]        
        t = get_quotes(quotes)
        
    return t
