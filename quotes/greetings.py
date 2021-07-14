from mylib.mymodule import get_quotes
#挨拶
def get_greetings(m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	if "おやす" in m.content:
		quotes = [
			[100, "おやすみなさい～"],
			[100, "寝るんですか？私も寝たい！おやすみ！"],
			[100, "睡眠は大事ですよ！"],
			[100, "寝るおやす！"]
		]
		return get_quotes(quotes)

	if "落ちます" in m.content or "おちます" in m.content:
		quotes = [
			[100, "落ちるんですか？おつかれー"],
			[100, "お疲れ様です"],
			[100, "おつー"]
		]
		return get_quotes(quotes)

	if "こんば" in m.content:
		quotes = [
			[100, "こんばんは！"],
			[100, "こんばんはー"],
			[100, "こん～"]
		]
		return get_quotes(quotes)

	if "こんにち" in m.content:
		quotes = [
			[100, "こんにちは！"],
			[100, "こんにちー"]
		]
		return get_quotes(quotes)

	if m.content == "こんー":
		quotes = [
			[100, "こんー"],
			[100, "こんこん"],
			[100, "こん～"]
		]
		return get_quotes(quotes)

	if m.content == "おはー" or "おはよ" in m.content:
		quotes = [
			[100, "おはー"],
			[100, f"{name}さんおはー"],
			[100, "おはよ～"]
		]
		return get_quotes(quotes)

	return t
