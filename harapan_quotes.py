import random
#asyncだとだめっぽい
#async def get_harapan():
#    await "ごふっぁ！！・・・な、何するんですか・・・！"
    
def get_harapan():
    #確率の重みとセリフリスト
    #コピペ用　[100 , ""],
    msg_list = [
        [100, "いっっ・・・た！！げほっ、ごほっ！"],
        [100, "ごふっぁ！！・・・な、何するんですか・・・！"],
        [50 ,"ひらりと　みをかわした！"],
        [50 , "MISS!!"],
        [100 ,"痛い痛い！殴らないでっ！！"],
        [100 , "ぐあっ！・・・ぐえぇ・・・"],
        [100 , "やあや、やめ・・・うぐううっっ！！"],
        [100 , "女の子のお腹をそうやって殴っちゃだｍがふっっ！！"],
        [100 , "ぐえぇ・・・げほっげほっ、げぼ、おええぇ・・・！"],
        [100 , "赤ちゃん産めなくなっちゃうぅ・・・"]
    ]
    
    #総重み
    total_weight = 0
    for i in msg_list:
        total_weight += i[0]
    
    #順番に確率に当てはまるかやっていく
    target = msg_list[0]
    for i in msg_list:
        if  random.randint(0, total_weight) <= i[0]:
            target = i
            break
        total_weight -= i[0]
     
    #セリフ部分を返す
    return target[1]
