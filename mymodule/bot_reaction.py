#汎用モジュール
import random
#セリフモジュール
from quotes.greetings import get_greetings
from quotes.shimoneta import get_shimoneta
from quotes.cheer import get_cheer

def get_bot_reaction(msg):
    reaction = ""
    #挨拶
    reaction = get_greetings(msg)
    #中身入ったら終了
    if reaction != "":
        return reaction

    #慰める
    reaction = get_cheer(msg)
    #中身入ったら終了
    if reaction != "":
        return reaction

    #リョナ
    reaction = ryona(msg)
    #中身入ったら終了
    if reaction != "":
        return reaction

    #下ネタは確率操作して下げることも可能
    if random.randint(0, 100) < 101:
        reaction = get_shimoneta(msg)
    #中身入ったら終了
    if reaction != "":
        return reaction

    #趣味関連
    reaction = hobby(msg)
    #中身入ったら終了
    if reaction != "":
        return reaction

    reaction = call_bot(msg)
    return reaction

def get_harapan(m):
    t = ""
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
        [50 , "痛い・・・痛ぃよぉぉ・・・なんでこんなことされなきゃいけないの！大ッッ嫌い！！\n\n・・・・・・なーんちゃって　冗談ですよ！冗・談！\n" + m.author.name + "さん好きですよ、構ってくれるから"],
        [100 , "赤ちゃん産めなくなっちゃうぅ・・・"]
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
    if m.content == "ぼふんぼふん":
        quotes = [
            [100, "ぼふんぼふん"],
            [30, "ほらもっと啼いてごらんなさい？厚かましいげっ歯類めが！！"],
            [100, "ヴォフンヴォフン"]
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
        
