#coding:utf-8

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# type = sys.getfilesystemencoding()

# requests获取网页源代码

# 直接获取源代码
html1 = requests.get('http://tieba.baidu.com/f?kw=python&fr=index')

# 修改http头获取源代码（反爬虫）
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'}
html2 = requests.get('http://jp.tingroom.com/yuedu/yd300p/', headers = head)
html2.encoding = 'utf-8'

# print html2.text
Japanese = re.findall('color:#666666;">(.*?)</span>',html2.text,re.S)
for each in Japanese:
    print each


chinese = re.findall('color: #039;">(.*?)</a>',html2.text,re.S)
for each in chinese:
    print each