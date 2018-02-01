# coding: utf-8
# 具体uri看api，此处是参照developer.github.com中的api

# 带参数的请求：
# 1、URL参数	requests.get(url, params={'key1':'value1'})
# 2、表单参数提交	requests.post(url, data={'key1':'value1'})
# 3、json参数提交	requests.post(url, json={'key1':'value1'})

import requests
import json
from requests import exceptions

URL = 'https://api.github.com'

def build_uri(endpoint):
	return '/'.join([URL, endpoint])

def better_print(json_str):
	return json.dumps(json.loads(json_str), indent=4)

def request_method():
	response = requests.get(build_uri('users/sxnhys'))
	print better_print(response.text)

	# 需要登陆认证，此处是不安全的作法
	response = requests.get(build_uri('user/emails'), 
		auth=('sxnhys', 'xxxxxxxxxx'))
	print better_print(response.text)


def params_request():
	response = requests.get(build_uri('users'), params={'since': 11})
	print better_print(response.text)
	print response.request.headers
	print response.url

def json_request():
	# 通过传递json把name改掉
	# response = requests.patch(build_uri('user'), 
	# 	auth=('sxnhys', 'xxxxxxxxxx'), json={'name': 'sxn'})

	# 增加一条email
	response = requests.post(build_uri('user/emails'),
		auth=('sxnhys', 'xxxxxxxxxx'), json=['sxnhys@163.com'])
	print better_print(response.text)
	print response.request.headers
	print response.request.body
	print response.status_code

# 处理请求异常
def exception_request():
	try:
		response = requests.get(build_uri('user/emails'),
			timeout=10)
		response.raise_for_status()
	except exceptions.Timeout as e:
		print e.message
	except exceptions.HTTPError as e:
		print e.message
	else:
		print response.text
		print response.status_code

# 自定义Request
def hard_requset():
	from requests import Request, Session
	s = Session()
	headers = {'User-Agent': 'fake1.3.5'}

	req = Request('GET', build_uri('user/emails'), 
		auth=('sxnhys', 'xxxxxxxxxx'), headers=headers)
	prepped = req.prepare()
	print prepped.body
	print prepped.headers

	resp = s.send(prepped, timeout=5)
	print resp.status_code
	print resp.request.headers
	print resp.text


if __name__ == '__main__':
	# request_method()
	# params_request()
	# json_request()
	# exception_request()
	hard_requset()