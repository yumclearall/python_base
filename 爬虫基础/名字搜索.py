import requests, bs4, openpyxl

# 创建工作簿
wb=openpyxl.Workbook()  
# 获取工作簿的活动表
sheet=wb.active 
# 工作表重命名
sheet.title='新闻' 
num=0
count=0
bc=0
sheet['A1'] ='序号'       # 加表头，给A1单元格赋值
sheet['B1'] ='新闻名'     # 加表头，给B1单元格赋值
sheet['C1'] ='推荐语'    # 加表头，给C1单元格赋值
sheet['E1'] ='链接'     # 加表头，给E1单元格赋值
url = "https://www.toutiao.com/api/search/content/"
keyword = input("你想要搜索谁的新闻呢？")
offset=0
while offset<60:
    params = {'aid': '24', 'app_name': 'web_search','offset': offset, 'keyword': keyword, 'count': '20'}
    offset+=20
# 发送请求，并把响应内容赋值到变量res里面
    res = requests.get(url,params=params)

# 定位数据
    articles=res.json()
    data=articles['data']

# 遍历列表，提取出里面的新闻标题与链接
    for i in data:
        num+=1
        try:
            a=i['title'].text
            b=i['abstract'].text
            c=i["article_url"].text
            sheet.append([num, a,'\n',b, c])
        except:
         pass    
wb.save('你搜到的东西.xlsx')