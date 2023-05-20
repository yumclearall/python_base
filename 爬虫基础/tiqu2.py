import requests
from bs4 import BeautifulSoup
res=requests.get('http://books.toscrape.com/')
soup=BeautifulSoup(res.text,'html.parser')
items=soup.find('aside').find('ul',class_='nav nav-list').find('ul').find_all('li')
for item in items:
    item=item.find('a')
    print(item.text.strip())