import requests
from bs4 import BeautifulSoup

bugs_url_list = []

for i in range(1,2):
    url = f'https://ghtoys.ru/shop/page{i}/'
    q = requests.get(url)
    result = q.content
    soup = BeautifulSoup(result,'lxml')
    bugs = soup.find_all(class_='shop-item-title')

    for bug in bugs:
        bug_page_url = bug.get('href')
        bugs_url_list.append(bug_page_url)


with open('bugs_url_list.txt', 'w') as file:
    for line in bugs_url_list:
        file.write(f'{line}\n')


