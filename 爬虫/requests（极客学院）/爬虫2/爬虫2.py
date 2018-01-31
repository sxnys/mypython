#coding:utf-8

# 制作文本爬虫
# 目标网站：http://jikexueyuan.com/ (极客学院)
# 目标内容：课程图片

import re
import requests

# 读取源代码文件
f = open('jike.txt', 'r')
html = f.read()
f.close()

# 匹配图片网址
pic_url = re.findall('<img src="(.*?)" class="lessonimg" title="', html, re.S)
i = 0
for each in pic_url:
	print 'now downloading:' + each
	pic = requests.get(each)
	fp = open('pic\\' + str(i) + '.jpg', 'wb')
	fp.write(pic.content)
	fp.close()
	i += 1

