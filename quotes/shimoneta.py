import random
from mylib.mymodule import get_quotes
#下ネタ
def get_shimoneta(m):
    t = ""
    #コピペ用[100, ""],
    if "フェラ" in m.content:
        quotes = [
            [100, "おちんちん・・・舐めさせられるの苦手なんですよね・・・"],
            [100, "ぺろぺろされるの好きなんですか？"],
            [100, "どうせ頭を掴んでイラマする気なんでしょ！"]
        ]
        t = get_quotes(quotes)
        
    if "イラマ" in m.content:
        quotes = [
            [100, "おちんちんを喉奥に突っ込まれると本当に苦しいんですからねっ"],
            [100, "頭をしっかり掴まれておちんちんを打ち付けられちゃったら、それはもう人間オナホですよね"],
            [100, "無理やりおちんちん突っ込まれてオエェってなっちゃうんだ・・・"]
        ]
        t = get_quotes(quotes)
    
    if "クンニ" in m.content:
        quotes = [
            [100, "まんまんぺろぺろ"],
            [100, "クンニ！"],
            [100, "ぺろぺろしたいんですか？"]
        ]
        t = get_quotes(quotes)
    
    if "ドS" in m.content or "サド" in m.content:
        quotes = [
            [100, "リョナラーたるものみんなきっとサドなんですよ！"],
            [100, "や、優しくしてね・・・？"],
            [100, "SMってSの方が気を遣うんですって！"]
        ]
        t = get_quotes(quotes)
    
    if "ドM" in m.content or "マゾ" in m.content:
        quotes = [
            [100, m.author.name + "さんはドMなんですか？"],
            [100, "リョナラーとしては虐めてるのに悦んでもらっちゃぁ困りますよね・・・"],
            [100, "創作活動はマゾいつまり製作者はみんなマゾ！"]
        ]
        t = get_quotes(quotes)
        
    if "シコ" in m.content:
        quotes = [
            [100, "シコシコしてほしいんですか？"],
            [100, "シッコーーいッ！"],
            [100, "しごいてあげましょうか？"]
        ]
        t = get_quotes(quotes)
        
    if "オナ" in m.content:
        quotes = [
            [100, "オナニー！"],
            [100, "お尻も一緒にいじった方が気持ちいいですよ！"],
            [100, "え、ここでオナニーしろ、ですって・・・？"]
        ]
        t = get_quotes(quotes)
        
    if "オナホ" in m.content:
        quotes = [
            [100, "オナホオナホって、オナホにされる女の子の気持ち考えたことあるんですか！ちょっと気持ちよさそうですけど！"],
            [100, "ﾌﾟﾌﾟｰ、" + m.author.name +"さんオナホなんかで満足してるんですか？\n・・・あっ、冗談ですよ？わわっ！ちょ、押し倒さないでっ！"],
            [100, "軽い子は簡単に持ち上がるからすぐオナホにされちゃう"]
        ]
        t = get_quotes(quotes)
        
    if "肉便器" in m.content or "便女" in m.content:
        quotes = [
            [100, "肉便器とか公衆便女とかひどいことしますよね全くぅ・・・"],
            [100, "誰のかも分からない赤ちゃんができちゃう！"],
            [100, "公衆便所に放置しておしっことか掛けてあげると更に屈辱的でいいと思います"]
        ]
        t = get_quotes(quotes)
        
    if "ロリ" in m.content or "幼女" in m.content:
        quotes = [
            [100, "いいですよねロリ"],
            [100, "幼女！幼女！"],
            [100, "ロリ好き！"],
            [100, "このロリコン！"]
        ]
        t = get_quotes(quotes)
    
    if "キンタマ" in m.content or "金玉" in m.content or "タマタマ" in m.content:
        quotes = [
            [100, "本当に金で出来てるのか切開して確かめてもいいですか？"],
            [100, "タマタマを舐めて欲しいんですか？"],
            [100, "左右で玉の大きさが違うから位置が逆にならないらしいですよ"]
        ]
        t = get_quotes(quotes)
    
    if "ちんこ" in m.content or "チンチン" in m.content or "ちんちん" in m.content or "チンポ" in m.content or "ちんぽ" in m.content:
        quotes = [
            [100, "え、おちんちん・・・？"],
            [100, "ちーんちん"],
            [50, "<:standup:805846231851073647> "],
            [100, "ち・・・チンポ"]
        ]
        t = get_quotes(quotes)
        
    if "おしっこ" in m.content or "シッコ" in m.content or "小便" in m.content:
        quotes = [
            [100, "おしっこ！"],
            [100, "飲みますか？おしっこ"],
            [100, "直飲みは無菌と言われてましたが実はそんなこと無いらしいですよ"]
        ]
        t = get_quotes(quotes)
        
    if "潮吹き" in m.content or "お潮" in m.content:
        quotes = [
            [100, "いっぱいお潮吹いてほしいですよね"],
            [100, "お潮吹いたからイったというわけではないんですよ"],
            [100, "潮吹きしやすくする訓練法があるんだとか"]
        ]
        t = get_quotes(quotes)
        
    if "おっぱい" in m.content or "乳首" in m.content:
        quotes = [
            [100, "おっぱい！"],
            [100, "おっぱいおっぱい"],
            [50, "<:oppaioppai:806106303025643531> "],
            [100, "私もおっぱいにはちょっと自信があるんですよ！"],
            [100, m.author.name + "さんっておっぱい大好きですよね"]
        ]
        t = get_quotes(quotes)
        
    if "お尻" in m.content or "ケツ" in m.content:
        quotes = [
            [100, "お尻！"],
            [100, "ムチムチなお尻が好きなんですか？"],
            [100, "お尻は揉んでもいいし叩いてもいいんですよ！"]
        ]
        t = get_quotes(quotes)
        
    if "まんこ" in m.content or "マンコ" in m.content or "まんまん" in m.content or "陰唇" in m.content:
        quotes = [
            [100, "おまんこ！"],
            [100, "やだなぁエッチなんだから・・・"],
            [100, "おまんこなんて言ってたら引かれちゃいますよ？"]
        ]
        t = get_quotes(quotes)
        
    if "セックス" in m.content or "おせっせ" in m.content or "sex" in m.content:
        quotes = [
            [100, "せっくす！"],
            [100, "え、セックス？・・・ドキドキ"],
            [100, "セッ・・・や、優しくしてね？"]
        ]
        t = get_quotes(quotes)
        
    if "変態" in m.content:
        quotes = [
            [100, "変態！変態！"],
            [100, "変態♪変態♪"],
            [100, m.author.name + "さんは変態さんですか？"]
        ]
        t = get_quotes(quotes)
        
    if "結腸" in m.content or "直腸" in m.content:
        quotes = [
            [100, "腸内に出されると後でお腹痛くなっちゃうんですよね・・・"],
            [100, "結腸超えってロマンですよね・・・"]
        ]
        t = get_quotes(quotes)
        
    if "浣腸" in m.content:
        quotes = [
            [100, "お尻で遊ぶなら浣腸した方がいいですよ！私はうんちしないからいつでもキレイですけどねっ！"],
            [100, "牛乳浣腸って見た目はきれいなんですけど残っちゃうと腐ったりするんですって"],
            [100, "お浣腸はぬるま湯とかが無難でいいと思いますよ"]
        ]
        t = get_quotes(quotes)
        
    if "アナル" in m.content:
        quotes = [
            [100, "アナル！"],
            [100, m.author.name + "さんもアナル好きなんですか？"],
            [100, "お尻は繊細ですから、優しく使わないと切れちゃいますよ？"],
            [100, "指3本入ればおちんちんが入れられるらしいですよ！"],
            [100, "アナルに挿入してもおまんこが空いてるのがいいんですよ！"],
            [100, "ペットボトルくらいから人工肛門が必要になってくるらしいですよ"],
            [100, "いいですよね、アナル"]
        ]
        t = get_quotes(quotes)
        
    if "アヌス" in m.content:
        t = "アヌスってアナルの名詞だって知ってました？でももう普通に名詞として使われてますよね"
        
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
                [100, m.author.name + "さんも好きですか？リョナ"]
            ]
            t = get_quotes(quotes)
        
    if "リョナラー" in m.content:
        quotes = [
            [100, m.author.name + "さんもリョナラーなんですか？"],
            [100, "ここにはリョナラーしかいないな！？"]
        ]        
        t = get_quotes(quotes)
        
    return t
