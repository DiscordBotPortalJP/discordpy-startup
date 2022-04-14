from mylib.mymodule import get_quotes
#趣味
def get_hobby(m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick

	if m.content.endswith("っふん") and "ぼっふん" not in m.content:
		quotes = [
		[100, "は？"],
		[100, "なんですかその語尾"],
		[100, "そんな語尾流行りませんよ！"]
		]
		return get_quotes(quotes)

	if "ネコミミ" in m.content or "猫耳" in m.content or "ネコ耳" in m.content or "獣耳" in m.content or "ケモミミ" in m.content or "ケモノミミ" in m.content:
		quotes = [
		[100, "私にも猫耳生えてますよ！ほらほら、触りますか？"],
		[100, "ケモミミとか好きなんですか？"],
		[100, "猫耳生えてる分脳みそ少ないんじゃないの？とか言う人がいるんですよね！失礼しちゃう！"]
		]
		return get_quotes(quotes)

	if "ネコ" in m.content or "猫" in m.content or "にゃー" in m.content or ("にゃん" in m.content and "まどにゃん" not in m.content) or "ニャー" in m.content or "ニャン" in m.content:
		quotes = [
		[100, "にゃー！"],
		[100, f"{name}さんもネコちゃん好きですか？だったら嬉しいなぁ"],
		[100, "にゃんにゃん！"]
		]
		return get_quotes(quotes)

	if "犬" in m.content or "イヌ" in m.content or "わんわん" in m.content or "ワンワン" in m.content:
		quotes = [
		[100, "わんわんお！"],
		[100, "わんこも好きですよ！"]
		]
		return get_quotes(quotes)

	if "尻尾" in m.content or "しっぽ" in m.content or "シッポ" in m.content:
		quotes = [
		[100, "尻尾があると走る時結構便利なんですよ"],
		[100, "尻尾は背骨の延長なので、強く引っ張らないでくださいね？死んじゃうから"],
		[100, "ほら尻尾ありますよ？もふもふですよ？"]
		]
		return get_quotes(quotes)

	if m.content == "ぼふんぼふん":
		quotes = [
		[100, "ぼふんぼふん"],
		[30, "ほらもっと啼いてごらんなさい？厚かましいげっ歯類めが！！"],
		[100, "ヴォフンヴォフン"],
		[100, "うまい度：うまい！:laughing: "],
		[100, "それなんの音なんですか？"],
		[100, "鼻の穴に指突っ込みますよ！"]
		]
		return get_quotes(quotes)

	if "ドーモ" in m.content or "ニンジャ" in m.content or "アイサツ" in m.content or "アイエ" in m.content:
		quotes = [
		[100, f"ドーモ、{name}＝サン。リョナゲボットです。"],
		[100, "ワッザ！？"],
		[100, "アイエッ！？"],
		[100, "ニンジャナンデ！？"]
		]
		return get_quotes(quotes)

	if "暑い" in m.content or "暑くない？" in m.content or "あつい" in m.content or "あつくない？" in m.content:
		quotes = [
		[100, "暑いのきらーい"],
		[100, "暑い時はエアコンに限りますよ！"]
		]
		return get_quotes(quotes)
	

	if "寒い" in m.content or "寒くない？" in m.content or "さむい" in m.content or "さむくない？" in m.content:
		quotes = [
		[100, "寒いなら一緒にくっつき合ってみますか・・・？なんちゃって"],
		[100, "私も寒いからこたつで丸くなりたいです・・・"]
		]
		return get_quotes(quotes)
		
	return t
