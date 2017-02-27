from bs4 import BeautifulSoup
import requests
import re

#requestsを使って、任意のURLを取って、そのページのHTMLソースを返す get_html_content を定義せよ。
def get_html_content(url):
    return requests.get(url).text.encode('utf-8')

#get_html_content を使って、任意のURLを取って、そのページのBeautifulSoupオブジェクトを返す get_soup を定義せよ
def get_soup(url):
    return BeautifulSoup(get_html_content(url), "lxml")

#get_soup を使って、任意のURLのを取って、そのページのタイトル（<title>ここに入っている文字のこと</title>）を取る get_title を定義せよ
def get_title(url):
    return get_soup(url).title.string

#任意のURLを取って、そのページに含まれるすべてのリンク先のURLのリストを返す get_all_links を定義せよ
def get_all_links(url):
    a_tags = get_soup(url).find_all("a")
    return [tag.get("href") for tag in a_tags]
