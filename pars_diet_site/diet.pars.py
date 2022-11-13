import requests
from bs4 import BeautifulSoup
import json

categories = {}

headers = {
    "accept" : "*/*",
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
r = requests.get(url,headers = headers)
result = r.content

soup = BeautifulSoup(result,"lxml")
pages = soup.find(class_ = "uk-grid uk-grid-medium").find_all(class_ = 'mzr-tc-group-item-href')

for page in pages:
    name = page.text
    some_url = page.get("href")
    categories[name] = "https://health-diet.ru" + some_url


with open("file_with_urls.json", "w") as file:
    json.dump(categories,file,indent = 4, ensure_ascii = False)
