# coding:utf-8

import re
import requests
# get: 从服务器上获取数据，通过构造url中的参数来实现功能
# post: 向服务器传送数据，将数据放在header提交数据

# url = 'http://www.crowdfunder.com/browse/deals'
# html = requests.get(url).text
# print html


# 向网页提交数据  post
url = 'http://www.crowdfunder.com/browse/deals&template=false'
data = {
	'entities_only': 'true',
	'page': '2'
}
html_post = requests.post(url, data = data)
title = re.findall('"card-title">(.*?)</div>', html_post.text, re.S)
for each in title:
	print each
