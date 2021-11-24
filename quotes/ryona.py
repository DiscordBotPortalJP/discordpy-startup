from mylib.mymodule import get_quotes
#リョナ
def get_ryona(m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick

	if "腹パン" in m.content:
		quotes = [
			[100, "腹パンいいですよね・・・ん、その手は何ですか"],
			[100, "お腹といっても鳩尾や下腹などありますが、どこ殴られても痛いんですよ"],
			[100, "腹パンはライトだから初心者にもオススメですよね！"],
			[100, "つ[http://sumalog.blog.jp/archives/1002478778.html]"],
			[100, "また殴るつもりですか！私を！"]
		]
		return get_quotes(quotes)

	if "性器破壊" in m.content:
		quotes = [
			[100, "性器破壊いいですよね！！"],
			[100, "おまんこもアナルも血塗れになっちゃう！"],
			[100, "性器破壊なんてされたらもうオナホにも出来ずに死んじゃうんですよ！"]
		]
		return get_quotes(quotes)

	if "顔面破壊" in m.content:
		quotes = [
			[100, "顔がぐちゃぐちゃに破壊されるのも好き！"],
			[100, "顔面破壊とはいい趣味をしていますね！"],
			[100, "顔への攻撃は上級者向けですよね"]
		]
		return get_quotes(quotes)

	if "拷問" in m.content:
		quotes = [
			[100, "拷問だったらえっちいのが好きですか？ガチなのが好きですか？"],
			[100, "とにかく拷問だ　拷問にかけろ！"],
			[100, "拷問にも長年の経験と熟練した技術が必要なんですって！"]
		]
		return get_quotes(quotes)

	if "三角木馬" in m.content:
		quotes = [
			[100, "お股が超痛いんですよあれ！"],
			[100, "割と普通に三角木馬ってエロ拷問に出てきますけど、普通にヤバイ苦痛なんですよ"],
			[100, "重りとか付けずに普通にまたがるだけならちょっと気持ちよさそう・・・"]
		]
		return get_quotes(quotes)

	if "首絞め" in m.content:
		quotes = [
			[100, "首を絞めてエッチするとなんか脳内物質が出て気持ちいいんですって！"],
			[100, "首を絞めるとおまんこを締めちゃう、なんてほんとにあるんですかねぇ～"],
			[100, "首を絞められて半死半生になってるかわいいですよね"]
		]
		return get_quotes(quotes)

	if "処刑" in m.content:
		quotes = [
			[100, "処刑って響きがカッコいいですよね"],
			[100, "電気椅子で水スポンジ無しでやってほしい～"],
			[100, "中世は色んなリョナい処刑があってすごいと思います"]
		]
		return get_quotes(quotes)

	if "ギロチン" in m.content or "クビチョンパ" in m.content or "首チョンパ" in m.content or "斬首" in m.content:
		quotes = [
			[100, "首チョンパいいですよね・・・なんというか「死んだ」って感じで"],
			[100, "まだ使える"],
			[100, "バッサリ落ちるのもいいけど、切れない刃物で何度も切りつけられるのも好き"]
		]
		return get_quotes(quotes)

	if "だるま" in m.content or "ダルマ" in m.content or "達磨" in m.content:
		quotes = [
			[100, "ダルマってあれですか？手足のないオナホみたいなやつですか？"],
			[100, "ダルマさんって座禅しすぎて手足が腐った人がモデルなんですって！セルフリョナだったんですかね？"],
			[100, "手足を落とすならやっぱりナタとかノコギリとかですかね！？"]
		]
		return get_quotes(quotes)

	if "四肢切断" in m.content:
		quotes = [
			[100, "四肢がなければ軽くなりますね！"],
			[100, "指詰めただけでも傷がその後の人生ずっとめっちゃ痛くてつらいらしいのに、四肢なんてどうなっちゃうんでしょうね？"],
			[100, "オナホにでもしますか？"]
		]
		return get_quotes(quotes)

	return t
