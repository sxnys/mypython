# coding: utf-8

# 利用爬虫自动下载图片
# 远程下载服务器上的文本文件

import requests

def download_image():
	'''下载图片
	如果拒绝访问，先去浏览器查看，若能正常查看伪造浏览器的agent加入headers
	'''
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
	url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1490282384080&di=5994a31b6059b2c7bde61709f77d8013&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F16%2F42%2F96%2F56e58PICAu9_1024.jpg"
	# 流模式
	response = requests.get(url, headers=headers, stream=True)
	# 打开文件
	with open('demo.jpg', 'wb') as fd:	# with自动调用close()关闭文件
		# 每128写入一次
		for chunk in response.iter_content(128):
			fd.write(chunk)

	# 结果一样，上面的效率更高
	# fd = open('demo.jpg', 'wb')
	# fd.write(response.content)
	# fd.close()

	# print response.content
	# print response.headers


def download_image_improved():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
	url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1490282384080&di=5994a31b6059b2c7bde61709f77d8013&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F16%2F42%2F96%2F56e58PICAu9_1024.jpg"
	# 流模式
	response = requests.get(url, headers=headers, stream=True)
	# 关闭流，避免浪费资源
	from contextlib import closing
	with closing(requests.get(url, headers=headers, stream=True)) as response:
		with open('demo1.jpg', 'wb') as fd:
			for chunk in response.iter_content(128):
				fd.write(chunk)



if __name__ == '__main__':
	download_image()
	download_image_improved()