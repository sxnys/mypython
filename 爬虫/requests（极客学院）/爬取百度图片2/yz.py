#coding:utf-8

import re
import requests

f = open('yz.txt', 'r')
html = f.read()
f.close()

pic_url = re.findall('"objURL":"(.*?)",', html, re.S);
# pic_name = re.findall('"fromPageTitle":"(.*?)     ",', html, re.S)
del pic_url[11]
i = 0
for each in pic_url:
	if each[0] != 'h':
		continue
	print 'now downloading: ' + each
	pic = requests.get(each)
	fp = open('yz\\' + str(i) + '.jpg', 'wb')
	fp.write(pic.content)
	fp.close()
	i += 1
print u'下载完成'