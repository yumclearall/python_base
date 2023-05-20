import requests
from bs4 import BeautifulSoup
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html=res.text
soup=BeautifulSoup(html,'html.parser')
items=soup.find_all(class_='books')
for item in items:
    a=item.find('h2')
    b=item.find(class_='title')
    c=item.find(class_='info')
    d=item.find(class_='img')
print(a.text,'\n',b.text,'\n' ,c.text,'\n',d.text)
print(type(a),type(b),type(c),type(d))