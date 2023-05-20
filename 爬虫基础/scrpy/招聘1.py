#导入模块
import scrapy
import bs4
from ..items import JobuiItem

class JobuiSpider(scrapy.Spider):  
#定义一个爬虫类JobuiSpider
    name = 'jobui'                  
    #定义爬虫的名字为jobui
    allowed_domains = ['www.jobui.com']
    #定义允许爬虫爬取网址的域名——职友集网站的域名
    start_urls = ['https://www.jobui.com/rank/company/']
    #定义起始网址——职友集企业排行榜的网址

    def parse(self, response):
    #parse是默认处理response的方法
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        #用BeautifulSoup解析response（企业排行榜的网页源代码）
        ul_list = bs.find_all('ul',class_="textList flsty cfix")
        #用find_all提取<ul class_="textList flsty cfix">标签
        for ul in ul_list:
        #遍历ul_list
            a_list = ul.find_all('a')
            #用find_all提取出<ul class_="textList flsty cfix">元素里的所有<a>元素
            for a in a_list:
            #再遍历a_list
                company_id = a['href']
                #提取出所有<a>元素的href属性的值，也就是公司id标识
                url = 'https://www.jobui.com{id}jobs'
                real_url = url.format(id=company_id)
                #构造出公司招聘信息的网址链接