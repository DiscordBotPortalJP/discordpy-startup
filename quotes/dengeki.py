from mylib.mymodule import get_quotes_with_damage
from mymodule.ryonage_bot import RyonageBot
from quotes.omorashi import get_omorashi
def get_dengeki(bot, m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	l = []
	sikko = ""
	#元気状態なら
	if bot.dying_hp < bot.get_hp():
		quotes = [
			[100 , "ななな、なにをバチバチさせてるんですか！？スタンガンでしょそれ！？やめて、当てな、ギャん！！！", 20],
      [100 , "や、やめて！スタンガンなんか近づけないでよ！？やだ、やあだ！や　が、ァ゛ァア゛ア！！", 20],
      [100 , "え、急に抱きついてきてどうし・・・ひ゛！？イギイィィア゛ア゛ァァア゛ア゛ア゛！！！！離゛し゛でえ゛え゛え゛え゛！！ギイィィィア゛ア゛ア゛ア！！！！", 40],
      [100 , "それすっごく痛いんですよ！？たくさんの針で貫かれたような痛みが走るんですから！だからお願いやメ゛ン゛！！！", 20],
      [100 , "せ、せめて手とか足とかにしてください！お腹はシャレになってないんですって！やだ！やだやだや　ア゛グン゛ッ゛！！！", 20],
      [100 , "やだっ押さえつけないで！やだやあだっ！スタンガン当て続けるのだけは　ギッッ！！痛゛いイダいイダイイ痛゛イ゛ィィイ！！！ギャア゛アア゛ァ゛ア！！！", 40],
      [100 , "どうしました？何かご用でも　ア゛ガッ！？", 20]
			]
	else:
		#瀕死の時
		quotes = [
			[100 , "", 20],
      [100 , "", 20],
      [100 , "", 20],
      [100 , "", 20],
      [100 , "", 20],
      [100 , "", 20],
      [100 , "", 20]
			]
		
	l = get_quotes_with_damage(quotes)
	#回避があるのでダメージで場合分け
	if 0 < l[1]:
		sikko = get_omorashi(bot, 20)
	#おしっこ判定後にダメージ
	hp = bot.damage(l[1])
	
	#if hp < 0:
	
	return l[0] + sikko
