from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
from quotes.omorashi import get_omorashi
def get_kubishime(bot, m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	l = []
	sikko = ""
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			]
	else:
		#瀕死の時
		quotes = [
			]

	
	return 
