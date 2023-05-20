from gevent import monkey
monkey.patch_all()
import gevent,requests,bs4,csv
from gevent.queue import Queue

headers = {
    'Cookie': 'waf_cookie=7b6e6042-6637-4ec8085f2b4344a464b196e04b542a494ce7; _ydclearance=9890afa8cdfc4b86e70681fb-8447-4278-b218-49371e554654-1584093765; _userCode_=2020313162475291; _userIdentity_=2020313162472010; _tt_=974F2F6DAFDEDC712EF4ABC00C07FEF6; DefaultCity-CookieKey=364; DefaultDistrict-CookieKey=0; Hm_lvt_6dd1e3b818c756974fb222f0eae5512e=1584086568; __utma=196937584.420777653.1584086568.1584086568.1584086568.1; __utmc=196937584; __utmz=196937584.1584086568.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmt_~1=1; __utmb=196937584.4.10.1584086568; Hm_lpvt_6dd1e3b818c756974fb222f0eae5512e=1584086869',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

work = Queue()

url_1 = 'http://www.mtime.com/top/tv/top100/'
work.put_nowait(url_1)

url_2 = 'http://www.mtime.com/top/tv/top100/index-{page}.html'
for x in range(2,11):
    real_url = url_2.format(page=x)
    work.put_nowait(real_url)

def crawler():
    while not work.empty():
        url = work.get_nowait()
        res = requests.get(url,headers=headers)
        bs_res = bs4.BeautifulSoup(res.text,'html.parser')
        datas = bs_res.find_all('div',class_="mov_con")
        for data in datas:
            TV_title = data.find('a').text
            data = data.find_all('p')
            TV_data =''
            for i in data:
                TV_data =TV_data + ''+ i.text
            writer.writerow([TV_title,TV_data])
            print([TV_title,TV_data])

csv_file = open('timetop.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file)

task_list = []
for x in range(3):
    task = gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)