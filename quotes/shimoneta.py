from mylib.mymodule import get_quotes
#下ネタ
def get_shimoneta(m):
    t = ""
    #コピペ用[100, ""],
    if "ロリ" in m.content:
        quotes = [
            [100, "いいですよねロリ"],
            [100, "ロリ好き！"],
            [100, "このロリコン！"]
        ]
        t = get_quotes(quotes)
        
    if "ちんこ" in m.content or "チンチン" in m.content or "ちんちん" in m.content or "チンポ" in m.content:
        quotes = [
            [100, "え、おちんちん・・・？"],
            [100, "ちーんちん"],
            [100, "ち・・・チンポ"]
        ]
        t = get_quotes(quotes)
        
    if "おしっこ" in m.content or "シッコ" in m.content or "小便" in m.content:
        quotes = [
            [100, "おしっこ！"],
            [100, "飲みますか？"],
            [100, "直飲みは無菌と言われてましたが実はそんなこと無いらしいですよ"]
        ]
        t = get_quotes(quotes)
        
    if "潮吹き" in m.content or "お潮" in m.content:
        quotes = [
            [100, "潮吹きはえっち！"],
            [100, "ぷしゃああって出てるの好き！"],
            [100, "潮吹きしやすくする訓練法があるんだとか"]
        ]
        t = get_quotes(quotes)
        
    if "おっぱい" in m.content or "乳首" in m.content:
        quotes = [
            [100, "おっぱい！"],
            [100, "おっぱいおっぱい"],
            [100, "私もおっぱいにはちょっと自信があるんですよ！"],
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
        
    if "セックス" in m.content or "おせっせ" in m.content:
        quotes = [
            [100, "せっくす！"],
            [100, "え、セックス？・・・ドキドキ"],
            [100, "セッ・・・や、優しくしてね？"]
        ]
        t = get_quotes(quotes)
        
    if "アナル" in m.content:
        quotes = [
            [100, "アナル！"],
            [100, m.author.name + "さんもアナル好きなんですか？"],
            [100, "お尻は繊細ですから、優しく使わないと切れちゃいますよ？"],
            [100, "指3本入ればおちんちんが入れられるらしいですよ！"],
            [100, "いいですよね、アナル"]
        ]
        t = get_quotes(quotes)
        
    if "アヌス" in m.content:
        t = "アヌスってアナルの名詞だって知ってました？でももう普通に名詞として使われてますよね"
        
    if "リョナ" in m.content:
        quotes = [
            [100, "リョナしゅき！"],
            [100, "リョナが好きだなんてすっっごい変態さんですね！"],
            [100, "ここならいいんですけど、リョナの話題はてぃーぴーおーを弁えてくださいね"],
            [100, "女の子が痛めつけられるところとか・・・フフ、興奮しちゃうんですよね"],
            [100, "版権キャラをリョナる時は色々慎重に、注意してくださいね？え、私・・・？"],
            [100, "リョナっていいのは非現実の子だけですからね？"],
            [100, m.author.name + "さんも好きですか？リョナ"]
        ]
        t = get_quotes(quotes)
        
    if "リョナラー" in m.content:
        quotes = [
            [100, m.author.name + "さんもリョナラーなんですか？"],
            [100, "ここにはリョナラーしかいないな！？"]
        ]        
        t = get_quotes(quotes)
        
    return t
