# coding: utf-8

'''
拆分含有多种分隔符的字符串
1、连续使用str.split()方法，每次处理一种分隔符
2、使用正则表达式的re.split()方法，一次性拆分字符串
'''

s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'

# 1、连续使用str.split()方法
def mySplit(s, ds):
	res = [s]
	for d in ds:
		t = []
		map(lambda x: t.extend(x.split(d)), res)
		res = t
	return [x for x in res if x]	# 当字符串非空才保留

print mySplit(s, ';,|\t')


# 2、使用正则表达式的re.split()方法
import re
print re.split('[,;|\t]+', s)