#coding:utf-8

import re

old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('text.txt', 'r')
html = f.read()
f.close()

# 爬取标题 
title = re.search('<title>(.*?)</title>', html, re.S).group(1)
print title

# 爬取链接
links = re.findall('a href="(.*?)"', html, re.S)
for each in links:
	print each

# 抓取部分文字，先大后小
text_feld = re.findall('<ul>(.*?)</ul>', html, re.S)[0]
text = re.findall('">(.*?)</a>', text_feld, re.S)
for each in text:
	print each


# sub实现翻页
for i in range(2, total_page + 1):
	new_link = re.sub('pageNum=\d+', 'pageNum=%d'%i, old_url, re.S)
	print new_link	