import random

#配列から確率でセリフを取り出す
#構造は[[重み, "セリフ"], ]
def get_quotes(q_list):
    total_weight = 0
    for i in q_list:
        total_weight += i[0]
    
    #順番に確率に当てはまるかやっていく
    target = q_list[0]
    for i in q_list:
        if  random.randint(0, total_weight) <= i[0]:
            target = i
            break
        total_weight -= i[0]
    return target[1]

#配列から確率でセリフを取り出す
#構造は[[重み, "セリフ", ダメージ], ]
def get_quotes_with_damage(q_list):
    total_weight = 0
    for i in q_list:
        total_weight += i[0]
    
    #順番に確率に当てはまるかやっていく
    target = q_list[0]
    for i in q_list:
        if  random.randint(0, total_weight) <= i[0]:
            target = i
            break
        total_weight -= i[0]
    l = [target[1], target[2]]
    return l
