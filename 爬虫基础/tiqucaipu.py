import requests
from bs4 import BeautifulSoup
rea=requests.get('http://www.xiachufang.com/explore/')
html=BeautifulSoup(rea.text,'html.parser')
a=html.find_all(class_='info pure-u')
for i in a:
    print(i.find(class_='name').find('a').text)
    print(i.find(class_='ing ellipsis').find_all('a').text)
    print(i.find(class_='name').find('a')['href'])