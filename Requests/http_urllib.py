# coding: utf-8

import urllib, urllib2

URL_IP = "http://httpbin.org/ip"
URL_GET = "http://httpbin.org/get"

def use_simple_urllib2():
	response = urllib2.urlopen(URL_IP)
	print '>>>>Response Headers:'
	print response.info()
	print '>>>>Response Body:'
	print ''.join([line for line in response.readlines()])

def use_params_urllib2():
	# 构建请求参数
	params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
	print 'Request Params: '
	print params
	# 发送请求
	response = urllib2.urlopen('?'.join([URL_GET, '%s']) % params)
	# 处理响应
	print '>>>>Response Headers:'
	print response.info()
	print '>>>>Status Code:'
	print response.getcode()
	print '>>>>Response Body:'
	print ''.join([line for line in response.readlines()])

if __name__ == '__main__':
	print '>>>Use simple urllib2: '
	use_simple_urllib2()
	print '>>>Use params urllib2: '
	use_params_urllib2()