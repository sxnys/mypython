# coding: utf-8
import urllib2
import cookielib

url = 'http://www.baidu.com'

# 方法一
response1 = urllib2.urlopen(url)
print response1.getcode()
# print response1.read()
f1 = open('1.txt', 'w')
f1.write(response1.read())

# 方法二
requset = urllib2.Request(url)
requset.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(requset)
print response2.getcode()
# print response2.read()
f2 = open('2.txt', 'w')
f2.write(response2.read())

# 方法三
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
# print response3.read()
f3 = open('3.txt', 'w')
f3.write(response3.read())
