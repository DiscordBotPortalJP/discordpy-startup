import random

def get_bot_reaction(msg) :
    reaction = ""
    #挨拶
    reaction = greetings(msg)
    if reaction != "":
        return reaction
    
    #下ネタは30%の確率で反応あるいは１００％でも別にいいか
    if random.randint(0, 100) < 100:
        reaction = shimoneta(msg)
    
    return reaction

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
        
    if "ロリ" in m.content:
        quotes = [
            [100, "いいですよねロリ"],
            [100, "ロリ好き！"],
            [100, "このロリコン！"]
        ]
        t = get_quotes(quotes)
        
    if "ちんこ" in m.content or "チンチン" in m.content or "ちんちん" in m.content or "おちんちん" in m.content or "チンポ" in m.content:
        quotes = [
            [100, "え、おちんちん・・・？],
            [100, "ちーんちん"],
            [100, "ち・・・チンポ"]
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
        
