from mylib.mymodule import get_quotes
#挨拶
def get_greetings(m):
	t = ""
if "おやす" in m.content:
quotes = [
[100, "おやすみなさい～"],
[100, "寝るんですか？私も寝たい！おやすみ！"],
[100, "睡眠は大事ですよ！"],
[100, "寝るおやす！"]]
t = get_quotes(quotes)
return t
