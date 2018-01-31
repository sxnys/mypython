# coding: utf-8

'''
scrapy选择器，最常用的就是xpath和css
selectObj.xpath('....').extract()
selectObj.css('....').extract()
xpath选择器基于lxml
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