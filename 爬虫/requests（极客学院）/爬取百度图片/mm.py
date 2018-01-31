#coding:utf-8

import re
import requests

f = open('baidumm.txt', 'r')
html = f.read()
f.close()

pic_url = re.findall('"hoverURL":"(.*?)",', html, re.S);
# pic_name = re.findall('"fromPageTitle":"(.*?)     ",', html, re.S)
# del pic_url[60]
i = 0
for each in pic_url:
	print 'now downloading: ' + each
	pic = requests.get(each)
	fp = open('mm\\' + str(i) + '.jpg', 'wb')
	fp.write(pic.content)
	fp.close()
	i += 1
print u'下载完成'