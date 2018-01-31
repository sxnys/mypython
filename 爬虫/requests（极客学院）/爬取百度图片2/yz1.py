#coding:utf-8

import re
import requests

pic_url = 'http://easyread.ph.126.net/k2qbPeo-X6VN0rrB2NjfIQ==/7916642049663431685.jpg'

pic = requests.get(pic_url)
fp = open('0.jpg', 'wb')
fp.write(pic.content)
fp.close()