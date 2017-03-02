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

    
    



