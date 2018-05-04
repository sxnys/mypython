# use http

import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'

def geocode(address):
	path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
	print(path)
	# 请求连接一台特定的主机
	connection = http.client.HTTPConnection('maps.googleapis.com')
	# 构造带path参数的GET查询
	connection.request('GET', path)

	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf8'))
	print(reply['result'][0]['geometry']['location'])


if __name__ == '__main__':
	geocode('207 N. Defiance St, Archbold, OH')