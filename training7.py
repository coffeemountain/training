import json
import requests
import re

class GithubScraper:

    def __init__(self, url):
        self.url = url  
        self.user = None
    def scrape_user_info(self):
        self.user = json.loads(requests.get(self.url).text)
        
    def scrape_repos(self):
        return(json.loads(requests.get(self.user['repos_url']).text))

    def get_user(self):
        return User(name = self.user['name'], login_id = self.user['login'], email = self.user['email'], location = self.user['location'], repos = self.scrape_repos())


class User:
    def __init__(self, name, login_id, email, location, repos):
        self.name = name
        self.login_id = login_id
        self.email = email
        self.location = location
        self.repos = repos


'''
問題文がちょっと曖昧でしたが、
GithubScraperのuser変数は、Userインスタンスとしてユーザー情報を持ちます。辞書ではありません！

この実装の最大の問題点は、get_userすると それだけUserインスタンスが生成されていってしまうことです。
実質的にその場合違うインスタンスなので、「同じユーザー情報を持った別人」という扱いになってしまいます。

Scraperがユーザーオブジェクトを内部変数として持つことで、スクレイプしたあとに情報をいじったりすることができます。
scraper.user.name = "HIROKI SHIMADA"

というふうに。この実装だとそれができません。

user = scraper.get_user()
user.name = "HIROKI SHIMADA" としても、

もう一度、
scraper.get_user().name
としたら 名前の情報はインスタンスに保存されず、元の情報になってしまいます。


あと、scrape_user_infoは
「scrape_user_info というメソッドを実行することでユーザー情報をスクレイプし、紐付いているuser （Userインスタンス）に保存（インスタンス変数に代入）する。」
なので、若干仕様と違います。
scrape_repos は レポジトリ情報を「返す」関数ではありません！！

'''
