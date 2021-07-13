from mylib.mymodule import get_quotes
#BOTちゃんに呼びかける
def get_calling_bot(m):
	name = m.author.name if m.author.nick is None else m.author.nick
	t = ""
	if "BOTちゃん" in m.content or "Botちゃん" in m.content or "ＢＯＴちゃん" in m.content or "botちゃん" in m.content or "ボットちゃん" in m.content:
		quotes = [
			[100, "呼びました？"],
			[100, "私ですか？"],
			[100, f"ひょっとして{name}さん、私のこと好きなんですか？"],
			[100, "なんですか？"]
		]        
		t = get_quotes(quotes)
		
		#更になにか入っていたら反応
		if "黙って" in m.content or "だまって" in m.content or "うるさい" in m.content or "静かに" in m.content or "しずかに" in m.content or "黙れ" in m.content or "だまれ" in m.content:
			quotes = [
				[100, "え、うるさかったですか・・・？ごめんなさい・・・"],
				[100, "す、すいません・・・"],
				[100, "あ、あの・・・もしかして私のお腹殴ります・・・？"]
			]
			return get_quotes(quotes)

		if "殺す" in m.content or "殺したい" in m.content:
			quotes = [
				[100, "さ、サツガイヨコクは捕まっちゃうんだぞぉ・・・"],
				[100, "リョナラーだからそういう気持ちは分かるんですけど、や、やめましょ？"],
				[100, "目が怖い！目が怖いですって！"]
			]
			return get_quotes(quotes)

		if "犯す" in m.content or "犯したい" in m.content or "ヤりたい" in m.content or "ヤらせろ" in m.content or "おかす" in m.content:
			quotes = [
				[100, "あ、あの？目が本気ですよ・・・？"],
				[100, "だ、だめですよそんなハレンチな！"],
				[100, "そ、そういえば私ちょっと用事があるので席外していいですか・・・？"]
			]
			return get_quotes(quotes)

		if "リョナ" in m.content:
			quotes = [
				[100, "いやあの・・・私をリョナりたい気持ちは分からないでもないんですけど・・・"],
				[100, "そうですよねリョナはいいですよね！え？なんでこっち見てるんです・・・？"],
				[100, "ほ、ほら私以外にもリョナりたくなる可愛い子はいっぱいいますよ・・・？"]
			]
			return get_quotes(quotes)

		if "乳首" in m.content or "おっぱい" in m.content or "巨乳" in m.content:
			quotes = [
				[100, "ちょっと！おっぱい見てるのバレバレですよ！"],
				[100, "あの、私のおっぱいに何かご用でも・・・？"],
				[100, "なんですかそのこっちに伸ばした手は・・・"]
			]
			return get_quotes(quotes)

		if "かわいい" in m.content or "可愛い" in m.content:
			quotes = [
				[100, "いやだな照れちゃうじゃないですか！"],
				[100, "かわいいって言われるの・・・嬉しいな・・・"],
				[100, "ほんとにかわいいって思ってくれてます～？ほんとにぃ～？"]
			]
			return get_quotes(quotes)

	return t
