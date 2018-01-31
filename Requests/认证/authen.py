# coding: utf-8

import requests
import json

BASE_URL = 'http://api.github.com'

def construct_url(end_point):
	return '/'.join([BASE_URL, end_point])

def better_print(s):
	return json.dumps(json.loads(s), indent=4)

def basic_auth():
	'''基本认证
	'''
	response = requests.get(construct_url('user'), auth=('sxnhys', 'lxlsxn13579'))
	print better_print(response.text)
	print response.request.headers	# headers里面包含base64码的认证信息，使用base64模块中的b64decode()方法解码

# OAuth认证
def basic_oauth():
	# 在github个人信息setting中创建了一个Personal access tokens，加入到请求头中
	headers = {'Authorization': 'token 88d17919243472fa389218cbc5e67031daaaa9c1'}
	# 获取user/emails信息
	response = requests.get(construct_url('user/emails'), headers=headers)
	print response.request.headers
	print better_print(response.text)
	print response.status_code


# requests库中的auth认证
from requests.auth import AuthBase

class GithubAuth(AuthBase):
	def __init__(self, token):
		self.token = token
	def __call__(self, r):
		r.headers['Authorization'] = ' '.join(['token', self.token])
		return r

def oauth_advanced():
	auth = GithubAuth('88d17919243472fa389218cbc5e67031daaaa9c1')
	response = requests.get(construct_url('user/emails'), auth=auth)
	print better_print(response.text)

if __name__ == '__main__':
	# basic_auth()
	# basic_oauth()
	oauth_advanced()
