# -*- coding: utf-8 -*-
import re

#URL 文字列を受取、そのパラメータ（?から始まる文字列部分）を排除する 関数 eliminate_parameters をつくれ
def eliminate_parameters(url):
    return re.sub("\?.*$", "", url)

#パラメータつきのURLを受取、パラメータの辞書を作る関数 create_parameter_dict をつくれ★
def create_parameter_dict(url):
    dict = {}
    para_whole_str = re.findall("(?<=\?).*$", url)
    para_str_list = re.split("&", para_whole_str[0])
    for x in para_str_list:
        key_value_pair = re.split("=", x)
        dict[key_value_pair[0]] = key_value_pair[1]
    return dict

#次のような意地悪メールアドレスを正しいメールアドレスになおして返す関数 correct_email_addres を作れ★★
def correct_email_address(email):
    replace_at = re.sub("(\[|_| | _)(at|atmk|atmark|AT|ATMARK)(\]|_| |_ )", "@", email)
    replace_dot = re.sub("(\[|_| | _)(dot|DOT|Dot|dt)(\]|_| |_ )", ".", replace_at)

    return replace_dot
