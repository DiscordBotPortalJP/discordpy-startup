from mylib.mymodule import get_quotes
from mymodule.ryonage_bot import RyonageBot
def get_feint(bot, m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100 , "ひっ！ごめんなさいぃ・・・"],
			[100 , "やだ、殴らないでっ！"],
			[100 , "あ、怒りましたか？ごめんなさいごめんなさいって！"],
			[100 , "やめて！怖いよぉ・・・"],
			[100 , "そ、そんな腕を振りかぶってなにを・・・ひゃんっ！"],
			[100 , "ぼ、暴力反対ーーっ！！"],
			[100 , "いじめないでっ！やだやだ！"],
			[100 , "そ、それで何をするつもりですか！？いや！！"]
			]
		suf = [
			[100, "BOTちゃんはうずくまった！"],
			[100, "ボットちゃんはビビって少し漏らしてしまった！"],
			[100, "BOTちゃんは腰が抜けてしまった！"],
			[100, "BOTちゃんは逃げ出そうとしたが転んでしまった！"],
			[100, "しかしあなたは何もしなかった"],
			[100, "数秒の間防御態勢だったボットちゃんだったが、フェイントと分かるとどことなく残念そうな表情をした"]
		]
		t = get_quotes(quotes) + "\n・・・・・・**" + get_quotes(suf) + "**"

	#瀕死の時はなにもしない

	return t
