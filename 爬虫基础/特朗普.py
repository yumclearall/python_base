# 导入模块
#https://www.toutiao.com/search/?keyword=%E7%89%B9%E6%9C%97%E6%99%AE%EF%BC%9A
import requests

url = "https://www.toutiao.com/api/search/content/"
# 封装params变量
params ={'aid':'24','app_name': 'web_search','offset': '0','format': 'json','keyword': '特朗普：'}

count: 20


# 发送请求，并把响应内容赋值到变量res里面
res = requests.get(url,params=params)

# 定位数据
articles=res.json()
data=articles['data']

# 遍历列表，提取出里面的新闻标题与链接
for i in data:
    try:
        print(i['title'],'\n',i['abstract'],'\n',i['article_url'])

    except:
        print(200)
