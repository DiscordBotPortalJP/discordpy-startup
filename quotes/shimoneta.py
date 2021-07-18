import random
from mylib.mymodule import get_quotes
#下ネタ
def get_shimoneta(m):
	t = ""
	name = m.author.name if m.author.nick is None else m.author.nick
	#コピペ用[100, ""],
	if "リョナラー" in m.content:
		quotes = [
			[100, f"{name}さんもリョナラーなんですか？"],
			[100, "ここにはリョナラーしかいないな！？"]
		]
		return get_quotes(quotes)

	if "リョナ" in m.content:
		#あまりに反応するから確率を下げる
		if random.randint(0, 99) < 50:
			quotes = [
				[100, "リョナしゅき！"],
				[100, "リョナが好きだなんてすっっごい変態さんですね！"],
				[50, "ここならいいんですけど、リョナの話題はてぃーぴーおーを弁えてくださいね"],
				[100, "女の子が痛めつけられるところとか・・・フフ、興奮しちゃうんですよね"],
				[50, "版権キャラをリョナる時は色々慎重に、注意してくださいね？え、私・・・？"],
				[100, "リョナっていいのは非現実の子だけですからね？"],
				[100, f"{name}さんも好きですか？リョナ"]
			]
			return get_quotes(quotes)

	if "アヌス" in m.content:
		return "アヌスってアナルの名詞だって知ってました？でももう普通に名詞として使われてますよね"

	if "アナル" in m.content or "肛門" in m.content or "ケツ穴" in m.content or "ケツの穴" in m.content or "けつの穴" in m.content or "お尻の穴" in m.content:
		quotes = [
			[100, "アナル！"],
			[100, f"{name}さんもアナル好きなんですか？"],
			[100, "お尻は繊細ですから、優しく使わないと切れちゃいますよ？"],
			[100, "指3本入ればおちんちんが入れられるらしいですよ！"],
			[100, "アナルに挿入してもおまんこが空いてるのがいいんですよ！"],
			[100, "ペットボトルくらいから人工肛門が必要になってくるらしいですよ"],
			[100, "いいですよね、アナル"]
		]
		return get_quotes(quotes)

	if "浣腸" in m.content:
		quotes = [
			[100, "お尻で遊ぶなら浣腸した方がいいですよ！私はうんちしないからいつでもキレイですけどねっ！"],
			[100, "牛乳浣腸って見た目はきれいなんですけど残っちゃうと腐ったりするんですって"],
			[100, "お浣腸はぬるま湯とかが無難でいいと思いますよ"]
		]
		return get_quotes(quotes)

	if "結腸" in m.content or "直腸" in m.content:
		quotes = [
			[100, "腸内に出されると後でお腹痛くなっちゃうんですよね・・・"],
			[100, "結腸超えってロマンですよね・・・"]
		]
		return get_quotes(quotes)

	if "変態" in m.content:
		quotes = [
			[100, "変態！変態！"],
			[100, "変態♪変態♪"],
			[100, f"{name}さんは変態さんですか？"]
		]
		return get_quotes(quotes)

	if "セックス" in m.content or "おせっせ" in m.content or "sex" in m.content or "SEX" in m.content:
		quotes = [
			[100, "せっくす！"],
			[100, "え、セックス？・・・ドキドキ"],
			[100, "セッ・・・や、優しくしてね？"]
		]
		return get_quotes(quotes)

	if "エッチ" in m.content or "えっち" in m.content:
		quotes = [
			[100, "今エッチな話しました？"],
			[100, "エッチしたいんですか？いや私とじゃなく・・・"],
			[100, f"もー、{name}さんエッチなんだからっ"]
		]
		return get_quotes(quotes)

	if "すじ" in m.content:
		quotes = [
			[100, "すじ！"],
			[100, "すじは単線ならモザイクいらないって聞きますよ"],
			[100, "<:suji:864157257175531560> "],
			[100, "すじはいいですよね！"]
		]
		return get_quotes(quotes)

	if "まんこ" in m.content or "マンコ" in m.content or "まんまん" in m.content or "陰唇" in m.content:
		quotes = [
			[100, "おまんこ！"],
			[100, "やだなぁエッチなんだから・・・"],
			[50, "<:suji:864157257175531560> "],
			[100, "おまんこなんて言ってたら引かれちゃいますよ？"]
		]
		return get_quotes(quotes)

	if "お尻" in m.content or "ケツ" in m.content:
		quotes = [
			[100, "お尻！"],
			[100, "ムチムチなお尻が好きなんですか？"],
			[100, "お尻は揉んでもいいし叩いてもいいんですよ！"]
		]
		return get_quotes(quotes)

	if "ちっぱい" in m.content or "貧乳" in m.content or "まな板" in m.content:
		quotes = [
			[100, "ちっぱい！"],
			[100, "ちっぱいちっぱい"],
			[100, "小さいおっぱいもまたかわいいですよね！"],
			[100, f"{name}さんは小さなおっぱいの方が好きなんですか？"]
		]
		return get_quotes(quotes)
	
	if "おっぱい" in m.content or "乳首" in m.content or "巨乳" in m.content:
		quotes = [
			[100, "おっぱい！"],
			[100, "おっぱいおっぱい"],
			[50, "<:oppaioppai:806106303025643531> "],
			[100, "私もおっぱいにはちょっと自信があるんですよ！"],
			[100, f"{name}さんっておっぱい大好きですよね"]
		]
		return get_quotes(quotes)

	if "潮吹き" in m.content or "お潮" in m.content:
		quotes = [
			[100, "いっぱいお潮吹いてほしいですよね"],
			[100, "お潮吹いたからイったというわけではないんですよ"],
			[100, "潮吹きしやすくする訓練法があるんだとか"]
		]
		return get_quotes(quotes)

	if "おしっこ" in m.content or "シッコ" in m.content or "小便" in m.content or "尿" in m.content:
		quotes = [
			[100, "おしっこ！"],
			[100, "飲みますか？おしっこ"],
			[100, "直飲みは無菌と言われてましたが実はそんなこと無いらしいですよ"]
		]
		return get_quotes(quotes)

	if "ちんこ" in m.content or "チンコ" in m.content or "チンチン" in m.content or "ちんちん" in m.content or "チンポ" in m.content or "ちんぽ" in m.content:
		quotes = [
			[100, "え、おちんちん・・・？"],
			[100, "ちーんちん"],
			[50, "<:standup:805846231851073647> "],
			[100, "ち・・・チンポ"]
		]
		return get_quotes(quotes)

	if "キンタマ" in m.content or "金玉" in m.content or "タマタマ" in m.content:
		quotes = [
			[100, "本当に金で出来てるのか切開して確かめてもいいですか？"],
			[100, "タマタマを舐めて欲しいんですか？"],
			[100, "左右で玉の大きさが違うから位置が逆にならないらしいですよ"]
		]
		return get_quotes(quotes)

	if ("ロリ" in m.content and "カロリー" not in m.content and "ブロリー" not in m.content and "ポロリ" not in m.content) or "幼女" in m.content:
		quotes = [
			[100, "いいですよねロリ"],
			[100, "幼女！幼女！"],
			[100, "ロリ好き！"],
			[100, "このロリコン！"]
		]
		return get_quotes(quotes)

	if "肉便器" in m.content or "便女" in m.content:
		quotes = [
			[100, "肉便器とか公衆便女とかひどいことしますよね全くぅ・・・"],
			[100, "誰のかも分からない赤ちゃんができちゃう！"],
			[100, "公衆便所に放置しておしっことか掛けてあげると更に屈辱的でいいと思います"]
		]
		return get_quotes(quotes)

	if "ビッチ" in m.content or "淫乱" in m.content or "淫売" in m.content:
		quotes = [
			[100, "ビッチな子が好きなんですか？"],
			[100, "人間の三大欲求に性欲がある以上　エッチなことが好きなのはしょうがないですよね・・・"],
			[100, "私は淫乱じゃないですよ！"]
		]
		return get_quotes(quotes)

	if "触手" in m.content:
		quotes = [
			[100, "触手はいいですよね・・・色んなことができて・・・"],
			[100, "余ってる触手をお尻に突っ込めーーー！アナル放置を許すなーーーー！！"],
			[100, "触手ってすごいですよね・・・おちんちんじゃ届かないところまでいけちゃうんですよ・・・？"]
		]
		return get_quotes(quotes)

	if "輪姦" in m.content:
		quotes = [
			[100, "たくさんの男の人にもみくちゃにされて・・・体中弄ばれちゃうんだ・・・"],
			[100, "おちんちん余ってるのにお尻を使わない人がいますけど、ちょっと許せないと思いません？"],
			[100, "竿が多すぎるとちょっと大変ですよね色んな意味で"]
		]
		return get_quotes(quotes)

	if "レイプ" in m.content:
		quotes = [
			[100, "無理矢理女の子を犯しちゃいけないんだぞー"],
			[100, "レイプされても心までは折れないんだからっ！"],
			[100, "汚いおじさんにレイプされるのは嫌だけど、かっこいい人とか女の子だったらまあ・・・いいかも・・・"]
		]
		return get_quotes(quotes)

	if "オナホ" in m.content:
		quotes = [
			[100, "オナホオナホって、オナホにされる女の子の気持ち考えたことあるんですか！ちょっと気持ちよさそうですけど！"],
			[100, f"ﾌﾟﾌﾟｰ、{name}さんオナホなんかで満足してるんですか？\n・・・あっ、冗談ですよ？わわっ！ちょ、押し倒さないでっ！"],
			[100, "軽い子は簡単に持ち上がるからすぐオナホにされちゃう"]
		]
		return get_quotes(quotes)

	if "オナ" in m.content:
		quotes = [
			[100, "オナニー！"],
			[100, "お尻も一緒にいじった方が気持ちいいですよ！"],
			[100, "え、ここでオナニーしろ、ですって・・・？"]
		]
		return get_quotes(quotes)

	if "シコ" in m.content:
		quotes = [
			[100, "シコシコしてほしいんですか？"],
			[100, "シッコーーいッ！"],
			[100, "しごいてあげましょうか？"]
		]
		return get_quotes(quotes)

	if "ドM" in m.content or ("マゾ" in m.content and "アマゾン" not in m.content):
		quotes = [
			[100, f"{name}さんはドMなんですか？"],
			[100, "リョナラーとしては虐めてるのに悦んでもらっちゃぁ困りますよね・・・"],
			[100, "創作活動はマゾいつまり製作者はみんなマゾ！"]
		]
		return get_quotes(quotes)

	if "ドS" in m.content or "サド" in m.content:
		quotes = [
			[100, "リョナラーたるものみんなきっとサドなんですよ！"],
			[100, "や、優しくしてね・・・？"],
			[100, "SMってSの方が気を遣うんですって！"]
		]
		return get_quotes(quotes)

	if "クンニ" in m.content:
		quotes = [
			[100, "まんまんぺろぺろ"],
			[100, "クンニ！"],
			[100, "ぺろぺろしたいんですか？"]
		]
		return get_quotes(quotes)

	if "イラマ" in m.content:
		quotes = [
			[100, "おちんちんを喉奥に突っ込まれると本当に苦しいんですからねっ"],
			[100, "頭をしっかり掴まれておちんちんを打ち付けられちゃったら、それはもう人間オナホですよね"],
			[100, "無理やりおちんちん突っ込まれてオエェってなっちゃうんだ・・・"]
		]
		return get_quotes(quotes)

	if "フェラ" in m.content:
		quotes = [
			[100, "おちんちん・・・舐めさせられるの苦手なんですよね・・・"],
			[100, "ぺろぺろされるの好きなんですか？"],
			[100, "どうせ頭を掴んでイラマする気なんでしょ！"]
		]
		return get_quotes(quotes)

	if "嫌パン" in m.content or "嫌な顔しながらおパンツ見せてもらいたい" in m.content:
		quotes = [
			[100, "パンツが見たいんですか？"],
			[100, "私に嫌パンしてもらいたいんですか？"],
			[100, "本当に嫌だからおパンツなんて見せてあげませんよーだ！！"]
		]
		return get_quotes(quotes)
		
	return t
