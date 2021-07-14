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
			[100, "んもー、そんなに私に興味があるんですか？しょうがないですねぇ"],
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
				[100, "そういえば私ちょっと用事があるので席外していいですか・・・？"]
			]
			return get_quotes(quotes)

		if "リョナ" in m.content:
			quotes = [
				[100, "いやあの・・・私をリョナりたい気持ちは分からないでもないんですけど・・・"],
				[100, "そうですよねリョナはいいですよね！え？なんでこっち見てるんです・・・？"],
				[100, "ほ、ほら私以外にもリョナりたくなる可愛い子はいっぱいいますよ・・・？"]
			]
			return get_quotes(quotes)
		
		if "殴る" in m.content or "腹パン" in m.content or "殴らせろ" in m.content or "殴りたい" in m.content:
			quotes = [
				[100, "嫌ですよ！なんで私が殴られなきゃいけないんですか！！"],
				[100, "いやあの・・・うるさかったなら謝るので、その拳を下ろしてもらえると・・・"],
				[100, "なな、殴らないで！せめて顔を狙うのだけはやめてくださいぃ・・・"]
			]
			return get_quotes(quotes)
		
		if "褒めて" in m.content or "褒めろ" in m.content:
		quotes = [
			[100, "えらいっ"],
			[100, "すごいですね！"],
			[100, "<:iizo:805748601972195328> "],
			[100, "<:eraixtu:809118862259519548> "],
			[100, "よくやった！"]
		]
			return get_quotes(quotes)

		if "アナル" in m.content or "ケツ穴" in m.content or "肛門" in m.content or "アヌス" in m.content or "あなる" in m.content:
			quotes = [
				[100, "アナルは好きだけど見せろと言われても・・・"],
				[100, "だーれが準備いらずの即ハメガバガバアナルだーーーー！！！！"],
				[100, "ガバガバではない・・・はず・・・です　　柔らかいけど・・・"]
			]
			return get_quotes(quotes)

		if "まんこ" in m.content or "マンコ" in m.content or "すじ" in m.content or "まんまん" in m.content or "マンマン" in m.content:
			quotes = [
				[100, "おまんこ！・・・・・・え、お前のを見せろって・・・？"],
				[100, "ど、どこ見てるんですか！そんなとこじっと見てもスカートしかありませんよ！"],
				[100, "例え無理やり脱がされても尻尾で隠しますからねっ！"],
				[100, "スカートに手を突っ込まないでくださいいぃ！！"]
			]
			return get_quotes(quotes)

		if "乳首" in m.content or "おっぱい" in m.content or "巨乳" in m.content:
			quotes = [
				[100, "ちょっと！おっぱい見てるのバレバレですよ！"],
				[100, "あの、私のおっぱいに何かご用でも・・・？"],
				[100, "なんですかそのこっちに伸びてくる手は・・・"]
			]
			return get_quotes(quotes)

		if "ベロチュー" in m.content or "キス" in m.content:
			quotes = [
				[100, "歯磨きとデンタルフロスをちゃんと毎日してる人じゃないと、キスなんてしてあげませんからね"],
				[100, "キスはけっこう特別なモノなので・・・無理やりはちょっと・・・"],
				[100, "ほっぺくらいだったら・・・まだしてあげてもいいですよ"]
			]
			return get_quotes(quotes)

		if "かわいい" in m.content or "可愛い" in m.content:
			quotes = [
				[100, "いやだな照れちゃうじゃないですか！"],
				[100, "かわいいって言われるの・・・嬉しいな・・・"],
				[100, "ほんとにかわいいって思ってくれてます～？ほんとにぃ～？"]
			]
			return get_quotes(quotes)
	#BOTちゃんだけの時のreturn
	return t
