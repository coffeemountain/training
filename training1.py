# -*- coding: utf-8 -*-

#数字を入力として、その数字が偶数だったら文字列”even”, 奇数なら文字列”odd”を返す関数 judge_odd_even を作れ
def judge_odd_even(x):
    if x%2 == 0:
        return "even"
    else:
        return "odd"

#配列(リスト）list について、偶数の数字の数を返す関数 count_even を作れ
def count_even(list):
    count = 0
    for x in list:
        if x%2 == 0:
            count += 1
    return count

#第一引数に文字列、第二引数に文字列のリストをとって、リストの要素のいずれかに第一引数の文字が入っていたらTrue, そうでなければFalse を返す関数list_contains を作れ
def list_contains(string, list):
    if string in list:
        return True
    else:
        return False
