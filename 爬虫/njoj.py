# coding: utf-8

import requests
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def write(problem):
	f.writelines(u'题目：' + str(problem['title']).replace(' ', '') + '(' + str(problem['order']) + ')\n')
	f.writelines(u'时间限制：' + unicode(str(problem['timelimit'])) + '\n')
	f.writelines(u'空间限制：' + unicode(str(problem['memorylimit'])) + '\n')
	f.writelines(u'题目描述：\n' + unicode(str(problem['description'])) + '\n')
	f.writelines(u'题目输入：\n' + unicode(str(problem['input'])) + '\n')
	f.writelines(u'题目输出：\n' + unicode(str(problem['output'])) + '\n')
	f.writelines(u'输入样例：\n' + unicode(str(problem['sampleinput'])) + '\n')
	f.writelines(u'输出样例：\n' + unicode(str(problem['sampleoutput'])) + '\n')
	f.writelines(u'提示：\n' + unicode(str(problem['hint'])) + '\n\n\n\n')
	# f.writelines(u'来源：' + unicode(str(problem['source'])) + '\n\n')


def spider(url):
	# 每一页所有题目
	html = requests.get(url)
	selector = etree.HTML(html.text)
	problems = selector.xpath('//tbody/tr')

	page_num = re.search('page=(\d+)', url, re.S).group(1)

	print u'正在抓取第' + str(page_num) + u'页的题目...'
	# 针对每一页每一个题目
	for each in problems:
		eurl = 'http://njoj.org' + each.xpath('td[@class="title-tags"]/div[@class="title"]/a/@href')[0]
		# print eurl
		ehtml = requests.get(eurl)
		eselector = etree.HTML(ehtml.text)
		# if eurl == 'http://njoj.org/Problem/Local/1034/':
		# 	f1 = open('test.txt', 'w')
		# 	f1.writelines(ehtml.text)
		# 	f1.close()

		problem_body = eselector.xpath('//div[@id="problem_body"]')
		for each_ in problem_body:
			problem = {}
			problem['order'] = re.search('Local/(\d+)/', eurl, re.S).group(1)
			problem['title'] = each_.xpath('div[@id="problem_title"]/h1/text()')[0].replace('\n', '')
			problem['timelimit'] = each_.xpath('div[@id="problem_title"]/p/span[@id="timelimit_text"]/text()')[0].replace('\n', '')
			problem['memorylimit'] = each_.xpath('div[@id="problem_title"]/p/span[@id="memorylimit_text"]/text()')[0].replace('\n', '')
			problem['description'] = each_.xpath('div[@id="problem_description"]/div[@class="desc_text"]')[0].xpath('string(.)')
			problem['input'] = each_.xpath('div[@id="problem_input"]/div')[0].xpath('string(.)')
			try:
				problem['output'] = each_.xpath('div[@id="problem_output"]/div')[0].xpath('string(.)')
				problem['sampleinput'] = each_.xpath('div[@id="problem_sampleinput"]/div')[0].xpath('string(.)')
				problem['sampleoutput'] = each_.xpath('div[@id="problem_sampleoutput"]/div')[0].xpath('string(.)')
				problem['hint'] = each_.xpath('div[@id="problem_hint"]/div')[0].xpath('string(.)')
				# problem['source'] = each_.xpath('div[@id="problem_source"]/div')[0].xpath('string(.)')
				write(problem)
			except:
				special = each_.xpath('div[@id="problem_input"]')[0]
				problem['output'] = special.xpath('div[@id="problem_output"]/div')[0].xpath('string(.)')
				problem['sampleinput'] = special.xpath('div[@id="problem_sampleinput"]/div')[0].xpath('string(.)')
				problem['sampleoutput'] = special.xpath('div[@id="problem_sampleoutput"]/div')[0].xpath('string(.)')
				problem['hint'] = special.xpath('div[@id="problem_hint"]/div')[0].xpath('string(.)')
				# problem['source'] = special.xpath('div[@id="problem_source"]/div')[0].xpath('string(.)')
				write(problem)
				

if __name__ == '__main__':
	pool = ThreadPool(8)
	f = open('problems.txt', 'w')
	page = []

	for i in range(1, 10):
		url = 'https://njoj.org/Problem/Local/?page=' + str(i)
		page.append(url)

	results = pool.map(spider, page)
	pool.close()
	pool.join()
	f.close()