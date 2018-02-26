# coding: utf-8

import requests
import hmac
import hashlib
import base64
import time
import random
import re
from screenShot import screenshot

num = 0
while True:
	num += 1
	raw_input()
	screenshot(str(num))

	appid = "1255648476"
	bucket = "imgregnise"
	secret_id = "AKIDCJG2gAwbdVIvMcobKsFfyAD5mIdnuYAe"  #我更改了，不要复制我的
	secret_key = "SjpjS0NZbS8dx63pRr7HSXcZLwMc8UCr"  #我更改了，不要复制我的
	expired = time.time() + 2592000
	onceExpired = 0
	current = time.time()
	rdm = ''.join(random.choice("0123456789") for i in range(10))
	userid = "0"
	fileid = "tencentyunSignTest"

	info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + str(expired) + "&t=" + str(current) + "&r=" + str(
	    rdm) + "&u=0&f="

	signindex = hmac.new(secret_key, info, hashlib.sha1).digest()  # HMAC-SHA1加密
	sign = base64.b64encode(signindex + info)  # base64转码

	url = "http://recognition.image.myqcloud.com/ocr/general"
	headers = {'Host': 'recognition.image.myqcloud.com',
	           "Content-Length": "187",
	           "Content-Type": "application/json",
	           # "Content-Type": "multipart/form-data",
	           "Authorization": sign
	           }

	f = open('./screenshot/%s.png' % str(num), 'rb')
	payload = {
	    "appid": appid,
	    "bucket": bucket,
	    # "url": "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3891329904,2194121161&fm=27&gp=0.jpg"
	    'image': base64.b64encode(f.read())
	}
	f.close()

	r = requests.post(url, json=payload, headers=headers)
	responseinfo = r.content

	r_index = r'itemstring":"(.*?)"'  # 做一个正则匹配
	result = re.findall(r_index, responseinfo)

	with open('1.txt', 'w') as f:
		for i in result:
		    # print i
		    f.write(i)

	print 'ocr sucess'