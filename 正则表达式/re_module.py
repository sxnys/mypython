# coding: utf-8

import re

str1 = 'imooc python'
pa = re.compile(r'imooc')  # 一个模板，r匹配原字符串
ma = pa.match(str1)
print ma
# print dir(ma)
print ma.group()	# 匹配的结果集合
print ma.span()		# 匹配结果位置
print ma.string		# 被匹配的字符串
print ma.re			# pattern的实例

pa1 = re.compile(r'imooc', re.I)		# 忽略大小写
ma1 = pa1.match('ImoOc python')
print ma1.group()

# 不创建pattern对象
ma = re.match(r'imooc', str1)


# 在一个字符串中查找匹配
# search(pattern, string, flags=0)
str1 = 'imooc videonum = 1000'
info = re.search(r'\d+', str1)
print info.group()

# 找到匹配，返回所有匹配部分的列表
# findall(pattern, string, flags=0)
str2 = 'c++=100, java=90, python=80'
info = re.search(r'\d+', str2)
print info.group()
info = re.findall(r'\d+', str2)
print info

# 将字符串匹配正则表达式的部分替换为其他值
# sub(pattern, repl, string, count=0, flags=0)
str3 = 'imooc videonum = 1000'
info = re.sub(r'\d+', '1001', str3)
print info

def add1(match):	# match为匹配的对象
	val = match.group()
	num = int(val) + 1
	return str(num)
info = re.sub(r'\d+', add1, str3)
print info

# 根据匹配分割字符串，返回分割字符串组成的列表
# split(pattern, string, maxsplit=0, flags=0)
str4 = 'imooc:C C++ Java Python'
info = re.split(r':| ', str4)
print info