from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
def get_harapan(bot, m):
    t = ""
    l = []
    #元気状態なら
    if bot.dying_hp < bot.get_hp():
        quotes = [
            [100 , "いっっ・・・た！！げほっ、ごほっ！", 30],
            [100 , "ごふっぁ！！・・・な、何するんですか・・・！", 30],
            [50 ,"ひらりと　みをかわした！", 0],
            [50 , "MISS!!", 0],
            [100 ,"痛い痛い！殴らないでっ！！", 30],
            [100 , "ぐあっ！・・・ぐえぇ・・・", 30],
            [100 , "やあや、やめ・・・うぐううっっ！！", 30],
            [100 , "女の子のお腹をそうやって殴っちゃだｍがふっっ！！", 30],
            [100 , "ぐえぇ・・・げほっげほっ、げぼ、おええぇ・・・！", 30],
            [100 , "あっ、うるさかったですか？いやごめんなさい！ちょっと黙るんで殴らないｄうぐうううぅ！！", 30],
            [100 , "ひっ、殴らないで！・・・・・・あれ？やらないんｄがっっ！ああぁぁ！！", 50],
            [50 , "痛い・・・痛ぃよぉぉ・・・なんでこんなことされなきゃいけないの！大ッッ嫌い！！\n\n・・・・・・なーんちゃって　冗談ですよ！冗・談！\n" + m.author.name + "さん好きですよ、構ってくれるから", 30],
            [100 , "赤ちゃん産めなくなっちゃうぅ・・・", 40]
            ]
    else:
        #瀕死の時
        quotes = [
            [100 , "ほ、本当に死んじゃ・・・ぐげぇ・・・", 30],
            [100 , "もうやめ・・・やめてぇ！ああ゛あ゛ぁ゛！！", 30],
            [100 ,"お願い・・・です・・・ほん、とに痛いの、うぐうぅ！！゛", 30],
            [100 , "これ、これ以上はもう・・・やめ、助けてぇ！", 30],
            [100 , "なんで・・・ぐすん・・・ここまで殴られなきゃ、うぐうぅぅ！！", 30],
            [100 , "なんでも、します、から・・・殺さない・・・で・・・", 30],
            [100 , "ほんと、に・・・ごめんなさい・・・もう、黙ってるからぁ・・・", 30],
            [100 , m.author.name + "さん、そんなに・・・私、のこと、嫌いだった、の・・・？", 30]
            ]
    l = get_quotes_with_damage(quotes)
    hp = bot.damage()
    #if hp < 0:
    
    return l[0]
