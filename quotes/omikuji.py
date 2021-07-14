
from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
import random
def get_omikuji(bot, m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		pre = "おみくじはーっと・・・・・・"
		quotes = [
			[100 , "超大吉！めっちゃすごそう！"],
			[100 , "大大吉！はっぴーかむかむ！"],
			[100 , "大吉！よかったですね！"],
			[100 , "中吉！小吉より上みたい"],            
			[100 , "小吉！うちでは吉より上ということになっております"],
			[100 , "吉！そこそこ運がいいみたい"],
			[100 , "半吉！ほんのちょっとだけいいみたい"],
			[100 , "末吉！普通よりほんのちょっっっっぴりだけマシみたい"],
			[100 , "末小吉！よくもわるくもない境目かな？"],
			[100 , "凶！凶シリーズで一番マシなやつ"],
			[100 , "小凶！凶より悪いみたい"],
			[100 , "半凶！だいぶ悪い凶みたい"],
			[100 , "末凶！大凶より少しマシみたい"],
			[100 , "大凶！ひええ！かわいそ！"],
			[100 , "超大凶！もう終わりだあ！！！！"]
			]
		if random.randint(0,100) < 5:
			pre = ""
			quotes = [[1, "いやでプー！"]]
	else:
		#瀕死の時
		pre = ""
		quotes = [
			[100 , "そこに、あるの、で・・・勝手に引いてください・・・"],
			[100 , "今無理で、す・・・"],
			[100 , "動けなくて・・・ごめん・・・なさい"]
			]
		
	return pre + get_quotes(quotes)
