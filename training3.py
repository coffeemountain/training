# -*- coding: utf-8 -*-

#値が数値であるディクショナリと数値nをとって、値をn倍する関数 multiply_dict を作れ　（一行でも書けます）
def multiply_dict(dict1, n):
    return {key: value *n for key, value in dict1.items()}

    
#値が数値である2つのディクショナリを取って、そのディクショナリを合体したディクショナリを返す関数 merge_dict を作れ。同じキーをもっているものに関しては、値を足し算する。(出力のディクショナリの順番は問わない)★
def merge_dict(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key] 
        else:
            dict1[key] = dict2[key]
    return dict1

#値が数値であるディクショナリを取って、値の多いきい順で並べ替えられたキーのリストを返す関数 sort_dict_by_value をつくれ
def sort_dict_by_value(dict):
    sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda x:x[1], reverse = True)}
    return sorted_dict.keys()
