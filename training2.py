# -*- coding: utf-8 -*-

#数値の入ったリストをとって、その平均を返す関数 get_average を作れ
def get_average(list1):
    return sum(list1)/len(list1) if len(list1) != 0  else 0

#数値の入ったリストを取って、その分散を返す関数 get_variance を作れ
def get_variance(list1):
    sum = 0
    ave = get_average(list1)
    for x in list1:
        sum += (x-ave)**2

    return sum/len(list1)  if len(list1) != 0 else 0

#リストの重複項目を取り除いたリストを返す関数 remove_overlap を作れ　（一行でも書けます）
def remove_overlap(list1):
    return list(set(list1))

#数値の入ったリストを取り、5.0より大きいものだけを残し、かつ四捨五入したリストを返す関数 round_over_5をつくれ
def round_over_5(list1):
    list2 = []
    for x in list1:
        if x >= 5.0:
            list2.append(round(x))
    return list2

#1．制御処理の問題2を１行で書け。★
def count_even_ver2(list1):
    return len([x for x in list1 if x%2 == 0])
