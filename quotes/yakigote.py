from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
from quotes.omorashi import get_omorashi
def get_yakigote(bot, m):
    t = ""
    l = []
    sikko = ""
    #元気状態なら
    if bot.dying_hp < bot.get_hp():
        quotes = [
            [100 , "な、なんですかそれ！？まさかそれ当てるの！？や、やめ・・・ぎいいあああ゛あああ゛あ゛あ゛あ゛！！！", 80],
            [100 , "やだああぁぁそれやあぁあだあああ！！やめ、があぁぁぎ゛あああああ゛あ゛ああ゛ああ゛！！！", 80],
            [100 , "や、焼けた鉄なんかで何するの！？近づけないでよ！や、ややや、い゛ッッがぁああ゛あ゛あ！！！", 80],
            [100 , "あ゛ッッづ゛あ！！？痛ああァァああ゛あ゛あ゛い゛ぃぃィィッッ！！！！", 80]
            ]
    else:
        #瀕死の時
        quotes = [
            [100 , "もう・・・殺し、て・・・ぐうぅッッ！！", 80],
            [100 , "熱くて痛いの・・・やだ・・・よ・・・うう゛ぅッッ！！", 80],
            [100 , "楽し・・・ですか・・・？えへへ・・・なら、よかった", 80],
            [100 , "私・・・ここまでされるほど・・・嫌われてた、んだ・・・ごめ・・・なさ・・・", 80]
            ]
        sikko = get_omorashi(30)
    l = get_quotes_with_damage(quotes)
    hp = bot.damage(l[1])
    #if hp < 0:
    
    return l[0] + sikko
