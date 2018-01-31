# -*- coding: utf-8 -*-
import scrapy
from todayMovie.items import TodaymovieItem

class NanjingmoviespiderSpider(scrapy.Spider):
    name = "NanJingMovieSpider"
    allowed_domains = ["jycinema.com"]
    start_urls = ['http://www.jycinema.com/html/default/index.html']

    # 由于网页是异步加载的，所以直接访问链接与浏览器访问的结果不一样，
    # 这里所有加载的内容全部空，只能在它js中找到加载json数据，所以这里什么都爬取不到
    def parse(self, response):
        subSelector = response.xpath('//span[@id="hotfilmlist"]')
        print 'subSelector: ', subSelector
        items = []
        for sub in subSelector:
        	item = TodaymovieItem()
        	item['movieName'] = sub.xpath('./text()').extract()[0]
        	items.append(item)
        return items