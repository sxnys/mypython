#coding:utf-8

import requests
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# http://www.jikexueyuan.com/course/
# 前20页 课程名称+课程介绍+课程时间+课程等级+学习人数

class spider(object):
    def __init__(self):
        print u'开始爬取内容...'

    # 获取网页源代码
    def getsource(self, url):
        html = requests.get(url)
        # f = open('html.txt', 'a')
        # f.write(html.text)
        # f.close()
        return html.text

    # 获取不同页数的链接
    def changepage(self, url, total_page):
        now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page + 1):
            link = re.sub('pageNum=\d+', 'pageNum=%s' % i, url, re.S)
            page_group.append(link)
        return page_group

    # 抓取每个课程块的信息
    def geteveryclass(self, source):
        everyclass = re.findall('<li id=(.*?)</li>', source, re.S)
        return everyclass

    # 从每个课程块中提取出我们需要的信息
    def getinfo(self, eachclass):
        info = {}
        info['title'] = re.search('title="(.*?)"', eachclass, re.S).group(1)
        info['content'] = ' '.join(str(re.search('<p style=.*?>(.*?)</p>', eachclass, re.S).group(1)).split())
        timeandlevel = re.findall('<em>(.*?)</em>', eachclass, re.S)
        info['classtime'] = ' '.join(timeandlevel[0].split())
        info['classlevel'] = timeandlevel[1]
        info['learnnum'] = re.search('"learn-number">(.*?)</em>', eachclass, re.S).group(1)
        return info

    # 保存结果到info.txt文件中
    def saveinfo(self, classinfo):
        f = open('info.txt', 'a')
        for each in classinfo:
            f.writelines('title:' + each['title'] + '\n')
            f.writelines('content:' + each['content'] + '\n')
            f.writelines('classtime:' + each['classtime'] + '\n')
            f.writelines('classlevel:' + each['classlevel'] + '\n')
            f.writelines('learnnum:' + each['learnnum'] +'\n\n')
        f.close()

if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()

    # 获取所有课程网页的链接
    all_links = jikespider.changepage(url, 5)

    for link in all_links:
        print u'正在处理页面：' + link
        # 获取网页源代码
        html = jikespider.getsource(link)
        # 获取所有课程所对应的源代码
        everyclass = jikespider.geteveryclass(html)
        # 获取每门课程的信息
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
    # 保存信息到文件
    jikespider.saveinfo(classinfo)