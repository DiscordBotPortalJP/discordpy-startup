import random

def get_bot_reaction(msg) :
    reaction = ""
    #挨拶
    reaction = greetings(msg)
    #合致したら強制終了
    if reaction != "":
        return reaction
    
    #慰める
    reaction = cheer(msg)
    #合致したら終了
    if reaction != "":
        return reaction
    
    #リョナ
    reaction = ryona(msg)
    
    #下ネタは30%の確率で反応あるいは１００％でも別にいいか
    if random.randint(0, 100) < 100:
        reaction = shimoneta(msg)
        if reaction != "":
            return reaction
    
    #趣味関連
    reaction = hobby(msg)
    
    reaction = call_bot(msg)
    
    return reaction

def get_harapan(name):
    t = ""
    """
    quotes = [
        [100, "いっっ・・・た！！げほっ、ごほっ！"],
        [100, "ごふっぁ！！・・・な、何するんですか・・・！"],
        [50 ,"ひらりと　みをかわした！"],
        [50 , "MISS!!"],
        [100 ,"痛い痛い！殴らないでっ！！"],
        [100 , "ぐあっ！・・・ぐえぇ・・・"],
        [100 , "やあや、やめ・・・うぐううっっ！！"],
        [100 , "女の子のお腹をそうやって殴っちゃだｍがふっっ！！"],
        [100 , "ぐえぇ・・・げほっげほっ、げぼ、おええぇ・・・！"],
        [100 , "痛い・・・痛いぃ！なんでこんなことされなきゃいけないの！大嫌い！！・・・・・・なーんちゃって　冗談ですよ！冗・談！" + m.author.name + "さん好きですよ、構ってくれるから"],
        [100 , "赤ちゃん産めなくなっちゃうぅ・・・"]
    ]
    t = get_quotes(quotes)
    return t
    """
    t = name + "さんのテストですよ"
    return t

#挨拶
def greetings(m):
    t = ""
    if m.content == "おはー" or "おはよ" in m.content:
        quotes = [
            [100, "おはー"],
            [100, m.author.name + "さんおはー"],
            [100, "おはよ～"]
        ]
        t = get_quotes(quotes)
        
    if m.content == "こんー":
        quotes = [
            [100, "こんー"],
            [100, "こんこん"],
            [100, "こん～"]
        ]
        t = get_quotes(quotes)
        
    if "こんにち" in m.content:
        quotes = [
            [100, "こんにちは！"],
            [100, "こんにちー"]
        ]
        t = get_quotes(quotes)
        
    if "こんば" in m.content:
        quotes = [
            [100, "こんばんは！"],
            [100, "こんばんはー"],
            [100, "こん～"]
        ]
        t = get_quotes(quotes)
        
    if "おやす" in m.content:
        quotes = [
            [100, "おやすみなさい～"],
            [100, "寝るんですか？私も寝たい！おやすみ！"],
            [100, "睡眠は大事ですよ！"],
            [100, "寝るおやす！"]
        ]
        t = get_quotes(quotes)
    return t

#下ネタ
def shimoneta(m):
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

#慰める
def cheer(m):
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
    
def ryona(m):
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
        
    if "腹パン" in m.content:
        quotes = [
            [100, "腹パンいいですよね・・・ん、その手は何ですか"],
            [100, "お腹といっても鳩尾や下腹などありますが、どこ殴られても痛いんですよ"],
            [100, "また殴るつもりですか！私を！"]
        ]        
        t = get_quotes(quotes)
        
    return t 
    
#趣味
def hobby(m):
    t = ""
    if "ドーモ" in m.content or "ニンジャ" in m.content or "アイサツ" in m.content:
        quotes = [
            [100, "ドーモ、" + m.author.name + "＝サン。リョナゲボットです。"],
            [100, "ニンジャナンデ！？"]
        ]        
        t = get_quotes(quotes)
        
    return t

#呼びかける
def call_bot(m):
    t = ""
    if "BOTちゃん" in m.content or "ＢＯＴちゃん" in m.content or "botちゃん" in m.content or "ボットちゃん" in m.content:
        quotes = [
            [100, "呼びました？"],
            [100, "私ですか？"],
            [100, "なんですか？"]
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
        
