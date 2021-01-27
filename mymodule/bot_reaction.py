#汎用モジュール
import random
#セリフモジュール
from quotes.greetings import get_greetings
from quotes.shimoneta import get_shimoneta
from quotes.cheer import get_cheer
from quotes.ryona import get_ryona
from quotes.hobby import get_hobby
from quotes.calling_bot import get_calling_bot

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
    reaction = get_ryona(msg)
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
    reaction = get_hobby(msg)
    #中身入ったら終了
    if reaction != "":
        return reaction

    reaction = get_calling_bot(msg)
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
