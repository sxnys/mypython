# coding:utf-8

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class douyu:
	def __init__(self):
		print u'让我们来看看正在直播的炉石主播吧...'

	# 获取炉石首页源代码
	def get_source(self, url):
		html = requests.get(url)
		# f = open('html.txt', 'a')
		# f.write(html.text)
		# f.close()
		return html.text

	# 获取每个主播对应的源代码
	def get_hosthtml(self, html):
		new_html = re.search('"item_data"(.*?)"text/javascript"', html, re.S).group(1)
		everyhost = re.findall('(<li><a href="/.*?" class="list" .*?"icon_live">)', new_html, re.S)
		return everyhost
		
	# 获取每个主播直播链接
	def get_live(self, everyhost):
		live_urls = []
		for each in everyhost:
			name = re.search('href="(/.*?)"', each, re.S).group(1);
			if str(name) == '/131420' or str(name) == '/imba2' or str(name) == '/shenchoudi':
				continue 
			live_urls.append('http://www.douyutv.com' + name)
		return live_urls

	# 获取每个主播的信息
	def get_host(self, live_html):
		host = {}
		host['title'] = re.search('<h1>(.*?)</h1>', live_html, re.S).group(1)
		host['name'] = re.search('"zb_name redcolor">(.*?)</i>', live_html, re.S).group(1)
		# host['renqi'] = re.search('"ol_num">(.*?)</span>', live_html, re.S)
		# host['weight'] = re.search('"weighttit">(.*?)</span>', live_html, re.S)
		label_html = re.search('"room_tags"(.*?)</dl>', live_html, re.S).group(1)
		# print label_html
		host['label'] = re.findall('title="(.*?)">', label_html, re.S)
		# host['guanzhu'] = re.search('"关注人气">(.*?)</span>', live_html, re.S)
		return host

	# 保存信息到文件
	def save(self, hostinfo):
		f = open('dy.txt', 'w')  # 只写方式打开，存在则覆盖否则创建
		for each in hostinfo:
			f.writelines(u'主播：' + each['name'] + '\n')
			f.writelines(u'标题：' + each['title'] + '\n')
			# f.writelines(u'人气：' + each['renqi'] + '\n')
			# f.writelines(u'鱼丸体重：' + each['weight'] + '\n')
			f.writelines(u'标签：')
			for label in each['label']:
				f.writelines(label + ' ')
			f.writelines('\n\n')
			# f.writelines(u'关注人数：' + each['guanzhu'] + '\n\n')
		f.close()


if __name__ == '__main__':
	url = 'http://www.douyutv.com/directory/game/How'

	dy = douyu()
	html = dy.get_source(url)
	everyhost = dy.get_hosthtml(html)

	live_urls = dy.get_live(everyhost)

	# 主播信息
	hostinfo = []
	i = 1
	for each in live_urls:
		print u'正在处理 ' + each
		live_html = requests.get(each)
		# if i == 1:
		# 	f = open('qiuri.txt', 'a')
		# 	f.write(live_html.text)
		# 	f.close()
		host = dy.get_host(live_html.text)
		hostinfo.append(host)
		i += 1
	print u'已全部记录！'

	# 保存
	dy.save(hostinfo)


