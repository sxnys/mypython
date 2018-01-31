#coding:utf-8

# 正则表达式

# 导入re库文件
import re
# 常用方法
# findall: 匹配所有符合规律的内容，返回包含结果的列表
# search: 匹配并提取第一个符合规律的内容，返回一个正则表达式对象
# sub: 替换符合规律的内容，返回替换后的值

secret_code = 'gsdfgdnjxxIxxjnfkdjnkdjnxxlovexx2343jn3xxyouxxjfj3'

# .: 匹配任意字符，换行符'\n'除外
a = 'xz123'
b = re.findall('x.', a)
c = re.findall('x..', a)
print b
print c

# *: 匹配前一个字符0次或无限次
a = 'xyxy123'
print re.findall('x*', a)

# ?: 匹配前一个字符0次或者1次
a = 'xy123'
print re.findall('x?', a)

# .*: 贪心算法，提取最多的内容
b = re.findall('xx.*xx', secret_code)
print b

# .*?: 非贪心算法，提取尽可能多的满足条件的串
b = re.findall('xx.*?xx', secret_code)
print b

# (): 括号内的数据作为结果返回
b = re.findall('xx(.*?)xx', secret_code)
print b
for each in b:
	print each

# 字符串占多行
s = '''dsfxxhello
xxfddfxxworldxxasfs'''
print re.findall('xx(.*?)xx', s)  # .无法匹配'\n'
# re.S使得.匹配任意字符（包括'\n'）
print re.findall('xx(.*?)xx', s, re.S)

# search
s = 'dsaxxIxx123xxlovexxdsad'
b1 = re.search('xx(.*?)xx123xx(.*?)xx', s)
b2 = re.findall('xx(.*?)xx123xx(.*?)xx', s);
# print b1 是一个正则表达式对象 
print b2
# group(x)代表第x个()的匹配内容
print b1.group(1)
print b1.group(2)
# b2为一个以元组为元素的列表，若匹配内容有多个，
# 则在某个匹配内容内的括号为元祖的元素
print b2[0][0]
print b2[0][1]

# sub
s = 'xx21321xx'
s1 = re.sub('xx(.*?)xx', '123456789', s)
print s1



# 匹配数字
a = 'sdfssd3244324jksd23432ds'
print re.findall('(\d+)', a)