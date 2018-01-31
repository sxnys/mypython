# coding: utf-8

# 抓取网页中的图片到本地
# 抓取网页，获取图片地址，抓取图片内容并保存到本地

import urllib2
import re
import os

# 获取网页源代码
url = 'http://www.imooc.com/course/list'
req = urllib2.urlopen(url)
buf = req.read()

# 获取图片地址
listurl = re.findall(r'http:.+\.jpg', buf)

# 抓取图片内容并保存到本地
os.mkdir(u'抓取的图片')
os.chdir(u'抓取的图片')

i = 0
for u in listurl:
	f = open(str(i) + '.jpg', 'w')
	req = urllib2.urlopen(u)
	buf = req.read()
	f.write(buf)
	i += 1