import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res_foods = requests.get('http://www.xiachufang.com/explore/',headers=headers)
bs_foods = BeautifulSoup(res_foods.text,'html.parser')
list_foods = bs_foods.find_all('div',class_='info pure-u')

list_all = []

for food in list_foods:
    tag_a = food.find('a')
    name = tag_a.text[17:-13]
    URL = 'http://www.xiachufang.com'+tag_a['href']
    tag_p = food.find('p',class_='ing ellipsis')
    ingredients = tag_p.text[1:-1]
    list_all.append([name,URL,ingredients])
print(list_all)
import smtplib 
from email.mime.text import MIMEText
from email.header import Header
#引入smtplib、MIMEText和Header

mailhost='smtp.qq.com'
#把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
qqmail = smtplib.SMTP()
#实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
qqmail.connect(mailhost,25)