
import requests
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

headers = {
    'origin':'https://y.qq.com',
    # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 标记了请求从什么设备，什么浏览器上发出
    }
# 伪装请求头

params = {
'ct':'24',
'qqmusic_ver': '1298',
'new_json':'1',
'remoteplace':'sizer.yqq.song_next',
'searchid':'64405487069162918',
't':'0',
'aggr':'1',
'cr':'1',
'catZhida':'1',
'lossless':'0',
'flag_qc':'0',
'p':'1',
'n':'20',
'w':'周杰伦',
'g_tk':'5381',
'loginUin':'0',
'hostUin':'0',
'format':'json',
'inCharset':'utf8',
'outCharset':'utf-8',
'notice':'0',
'platform':'yqq.json',
'needNewCode':'0'    
}
# 将参数封装为字典
res_music = requests.get(url,headers=headers,params=params)
# 发起请求，填入请求头和参数