# -*- coding: utf-8 -*-
from pytesser import pytesser
from PIL import Image

import re
import requests
import urllib
import urllib2
import cookielib

def urllib2_yzm_cookie():
	url = 'http://202.119.81.112:8080/Logon.do?method=logon'

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
	}

	data = {
		'USERNAME': '913000720238',
		'PASSWORD': '130243',
		'RANDOMCODE': ''
	}

	postdata = urllib.urlencode(data)

	# cookie
	cookie = cookielib.CookieJar()
	handler = urllib2.HTTPCookieProcessor(cookie)
	opener = urllib2.build_opener(handler)

	# 第一次请求网页得到cookie
	request = urllib2.Request(url, postdata, headers=headers)
	response = opener.open(request)

	# 由于验证码识别的误差，不停地获取验证码登陆，直到正确为止
	while True:
		# 获取验证码
		yzm = opener.open('http://202.119.81.112:8080/verifycode.servlet')
		yzmfile = open('yzm.jpg', 'wb')
		yzmfile.write(yzm.read())
		yzmfile.close()

		# 识别验证码
		image = Image.open('yzm.jpg')
		yzmtext = pytesser.image_to_string(image)
		tmp = list(yzmtext)
		while ' ' in tmp:
			tmp.remove(' ')
		while '\n' in tmp:
			tmp.remove('\n')
		yzmtext = ''.join(tmp)[:4]
		print yzmtext
		# return

		# 模拟登陆
		# data['RANDOMCODE'] = raw_input()
		data['RANDOMCODE'] = yzmtext
		postdata = urllib.urlencode(data)
		request = urllib2.Request(url, postdata, headers=headers)
		response = opener.open(request)

		# print response.read().decode('utf-8')

		# 爬取成绩
		grade_url = 'http://202.119.81.112:9080/njlgdx/kscj/cjcx_list'
		response = opener.open(grade_url)
		html = response.read()
		f = open('1.txt', 'w')
		f.write(html)
		f.close()
		# print html
		if re.search('RANDOMCODE', html) == None:
			break


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''' 跳过验证码
shengrang ———— 登录之后再登出，接着再次登录的时候，会使用入口 /njlgdx/xk/Verifyservlet，
抓取请求会发现此处进行帐号、密码、验证码的验证，正确则返回一个 302 跳转，
指向 /njlgdx/xk/LoginToXk?method=verify&USERNAME=用户名&PASSWORD=密码的md5的upper，
然后才 302 跳转到登录后界面。因此只需要直接请求一下第二个 url 就能绕过验证码验证。
'''

url = 'http://202.119.81.112:9080/njlgdx/xk/LoginToXk'
login_info = {
	'method': 'verify',
	'USERNAME': '913000720238',
	'PASSWORD': '130243'
}

# 将密码加密位MD5
import hashlib
MD5 = hashlib.md5()
MD5.update(login_info['PASSWORD'])
login_info['PASSWORD'] = MD5.hexdigest().upper()

url = '?'.join([url, urllib.urlencode(login_info)])

# 使用cookie访问登陆之后的其他页面
def requests_noyzm_cookie():
	response = requests.get(url)
	# print response.content
	cookie = response.request.headers['Cookie'] #['Set-Cookie'].split(';')[0]

	response1 = requests.get('http://202.119.81.112:9080/njlgdx/kscj/cjcx_list', headers={'Cookie': cookie})
	print response1.content

# 可以不使用cookie，使用session
def requests_noyzm_session():
	session = requests.session()
	response2 = session.get(url)
	response3 = session.get('http://202.119.81.112:9080/njlgdx/kscj/cjcx_list')
	print response3.content


if __name__ == '__main__':
	urllib2_yzm_cookie()
	# requests_noyzm_cookie()
	# requests_noyzm_session()