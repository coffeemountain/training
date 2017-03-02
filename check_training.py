from training1 import *
from training2 import *
from training3 import *
from training4 import *
from training5 import *
from training6 import *
from training7 import *

#training1
print("training1")
print(judge_odd_even(43))
print(judge_odd_even(0))
print(count_even([1, 3, 4, 2, 10, 7]))
print(count_even([]))
print(list_contains('Tom', ['Tom', 'Mike', 'Michel', 'Jim']))
#training2
print("training2")
print(get_average([1.3, 2.2, 10.3, 4.3]))
print(get_average([]))
print(get_variance([1, 3, 2.2, 10.3, 4.3]))
print(remove_overlap([1, 2, 4, 2, 4, 9, 4, 8]))
print(remove_overlap(['hoge','foo','hoge','bar','foo']))
print(round_over_5([4.7, 5.6, 9.82, 3.43, 9.10, 4.99]))
print(count_even_ver2([1, 3, 4, 2, 10, 7]))
#training3
print("training3")
print(multiply_dict({'Tom':90, 'Jane':43, 'Mike':32,}, 10))
print(merge_dict({'Tom': 90, 'Jane':43, 'Mike': 32}, {'Michael': 32, 'Alice': 32, 'Tom': 32, 'Mike': 44}))
print(sort_dict_by_value({'Michael': 23, 'Alice': 54, 'Tom': 39, 'Mike': 44}))

#training4
print("training4")

print(eliminate_parameters("http://scouty.co.jp/search?location=Tokyo&escore=3.0"))
print(eliminate_parameters("https://scouty.co.jp/search"))
print(create_parameter_dict("http://scouty.co.jp/search?location=Tokyo&escore=3.0"))
print(create_parameter_dict("https://scouty.me/search?keyword=python"))
print(correct_email_address("showwin[at]gmail.com"))
print(correct_email_address("showwin at gmail.com"))
print(correct_email_address("showwin@gmail dot com"))
print(correct_email_address("showwin [at] gmail dot com"))
print(correct_email_address("showwin _at_ gmail [dot] com"))
print(correct_email_address("showwin _atmk_ gmail.com"))

#training5
print("training5")

scout1 = Scout(name="Python Engineer", worker_type="Intern", skills=["Python", "Django"])
print(scout1.skills[0])
print(scout1.name)
scout1.add_skill("Flask")
print(scout1.skills)
scout1.add_skill("Django")
print(scout1.skills)
person1 = Person(name="Hiroki Shimada", skills=["Python", "Artificial Intelligence"])
person2 = Person(name="Shogo Ito", skills=["Ruby", "AWS"])
print(person1.name)
scout1.add_candidate(person1)
scout1.add_candidate(person2)
print(scout1.candidates[0].name)
print(scout1.get_candidate_name_list())
print(scout1.search_candidate_or())
print(scout1.search_candidate_and())

#training6
print("training6")
print(get_html_content("https://scouty.co.jp"))
soup = get_soup("https://scouty.co.jp")
print(type(soup))
title = get_title("https://scouty.co.jp")
print(title)
links = get_all_links("http://qiita.com/sqrtxx/items/49beaa3795925e7de666")
print(links)

#training7
print("===============================training7=============================")
scraper = GithubScraper("https://api.github.com/users/functionp")
scraper.scrape_user_info()
scraper.scrape_repos()
user = scraper.get_user()
print(user.login_id)
print(user.name)
print(type(user.repos))
print(type(user.repos[0]))
