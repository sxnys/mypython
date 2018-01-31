# coding: utf-8
from PIL import Image
from pytesser import pytesser

import re
import requests
import urllib

login_url = 'http://202.119.81.112:8080/Logon.do?method=logon'
yzm_url = 'http://202.119.81.112:8080/verifycode.servlet'
# 前面的IP地址每个人可能不同，在登陆成功之后获取
kccj_url = '/njlgdx/kscj/cjcx_list'

login_info = {
	'USERNAME': '',
	'PASSWORD': '',
	'RANDOMCODE': ''
}

headers = {
	'User-Agent': 'sxnhys'
}

# 存储登陆成功之后的cookie
cookie = ''

# 首次登陆获取cookie，本次登陆注定不成功，只是获取cookie
# first_failedLogin_response = requests.get(login_url, params=urllib.urlencode(login_info), headers=headers)
first_failedLogin_response = requests.post(login_url, data=login_info, headers=headers)
headers['Cookie'] = first_failedLogin_response.headers['Set-Cookie'].split(';')[0]
# print headers['Cookie']

# 输入用户名和密码
login_info['USERNAME'] = raw_input('Username: ')
login_info['PASSWORD'] = raw_input('Password: ')

# 由于验证码识别误差，循环获取验证码直至正确，登陆成功
while True:
	# 根据首次登陆时的cookie，获取验证码
	yzm_response = requests.get(yzm_url, headers=headers)
	yzmfile = open('yzm.jpg', 'wb')
	yzmfile.write(yzm_response.content)
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
	# print yzmtext
	login_info['RANDOMCODE'] = yzmtext

	# 重新登陆，若验证码正确则登陆成功
	# should_success_response = requests.get(login_url, params=urllib.urlencode(login_info), headers=headers)
	should_success_response = requests.post(login_url, data=login_info, headers=headers)
	html = should_success_response.content
	mainjsp = open('mainjsp.txt', 'w')
	mainjsp.write(html)
	mainjsp.close()
	# 验证码若正确则退出循环
	if re.search('RANDOMCODE', html) == None:
		# 测试发现不同的学号登陆之后的IP地址不一样，就112和113的差别，
		# 一开始枚举了这两个不同的IP对应的课程成绩地址，但是不清楚还有多少不同的，所以
		# 这里直接获取登陆之后的IP
		kccj_url = 'http://' + should_success_response.url.split('/')[2] + kccj_url
		# 登陆成功的cookie
		cookie = should_success_response.request.headers['Cookie']
		# print cookie
		break

# 成绩列表页面
# 测试发现不同的学号登陆
headers['Cookie'] = cookie
kccj_response = requests.get(kccj_url, headers=headers)
kccj = open('kccj.txt', 'w')
kccj.write(kccj_response.content)
kccj.close()

from bs4 import BeautifulSoup as bs
soup = bs(kccj_response.content, 'html.parser')
# 学期
term = [x.string for x in soup.find_all('td', string=re.compile(r'\d{4}-\d{4}-[1,2]'))]
# for i in  term:
# 	print i

# 课程名称
course = [x.string for x in soup.find_all('td', align='left', string=re.compile(r'\D+$'))]
# for i in course:
# 	print i

# 分数，重修分数和非重修分数一样的匹配规则
score = [x.string for x in soup.find_all('td', style=re.compile(r'^\s{1}'))]
# print score

# print u'学期\t\t\t课程名\t\t\t\t分数'
# for i in xrange(len(term)):
# 	print term[i] + '\t\t' + course[i].ljust(40, '*'), score[i].rjust(10)

# print len(term)
# print len(course)
# print len(score)

# 存储到xlsx
import xlwt
book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')
sheet.write(0, 0, u'学期')
sheet.write(0, 1, u'课程')
sheet.write(0, 2, u'成绩')
for i in xrange(1, len(term) + 1):
	sheet.write(i, 0, term[i-1])
	sheet.write(i, 1, course[i-1])
	sheet.write(i, 2, score[i-1])
book.save('C:\Users\sxn\Desktop\\' + u'课程成绩' + '.xlsx')


'''
也利用xpath爬取（scrapy选择器中的xpath方法，也可以使用lxml的etree的xpath，前者基于lxml）
'''
'''
from scrapy.selector import Selector
import xlwt

f = open('kccj.txt', 'r')
html = f.read()
f.close()

# 类似于from lxml import etree
# selectObj = etree.Html(html)
selectObj = Selector(text=html)

# 针对课程成绩爬取数据
# 先抓取所有包含成绩信息的行<tr>
allCjInfo = selectObj.xpath('//tr').extract()[2:]
# print allCjInfo[0]
# 每一行成绩信息构成一个selector
CjInfoSelector = [Selector(text=allCjInfo[i]) for i in xrange(len(allCjInfo))]

# 爬取成绩信息
length = len(CjInfoSelector)
# print length
term = []
courseId = []
course = []
score = []
xuefen = []
courseTime = []

# 数据存进excel
excel = xlwt.Workbook()
sheet = excel.add_sheet('sheet1')
sheet.write(0, 0, u'开课学期')
sheet.write(0, 1, u'课程编号')
sheet.write(0, 2, u'课程名称')
sheet.write(0, 3, u'成绩')
sheet.write(0, 4, u'学分')
sheet.write(0, 5, u'总学时')

for i in xrange(length):
	content = CjInfoSelector[i].xpath('//td').extract()
	# 如果上面的写成 content = CjInfoSelector[i].xpath('//td/text()').extract()
	# 那么如果是空字符串''，则不会在content里面，而有的<td>标签下是有内容的，有的没有
	term.append(Selector(text=content[1]).xpath('//text()').extract())
	courseId.append(Selector(text=content[2]).xpath('//text()').extract())
	course.append(Selector(text=content[3]).xpath('//text()').extract())
	score.append(Selector(text=content[4]).xpath('//text()').extract())
	xuefen.append(Selector(text=content[6]).xpath('//text()').extract())
	courseTime.append(Selector(text=content[7]).xpath('//text()').extract())
	sheet.write(i + 1, 0, term[i])
	sheet.write(i + 1, 1, courseId[i])
	sheet.write(i + 1, 2, course[i])
	sheet.write(i + 1, 3, score[i])
	sheet.write(i + 1, 4, xuefen[i])
	sheet.write(i + 1, 5, courseTime[i])

excel.save(u'课程成绩' + '.xlsx')
'''