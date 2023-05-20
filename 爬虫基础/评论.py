import requests
from bs4 import BeautifulSoup
res =requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/comments/feed/')
html=res.text
soup=BeautifulSoup(html,'html.parser')
items=soup.find_all('description')
for item in items:
    print(item.text)