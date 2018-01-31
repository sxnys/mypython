# coding: utf-8

'''
1、使用字符串的str.ljust()，str.rjust()，str.center()进行左、右、居中对齐
2、使用format()方法，传递类似'<20'，'>20'，'^20'的参数
'''

d = {
	'DistCull': 500.0,
	'SmallCull': 0.04,
	'farclip': 477,
	'lodDist': 100.0,
	'trilinear': 40
}

w = max(map(len, d.keys()))

for k in d:
	print k.ljust(w), ':', d[k]

print '\n'

for k in d:
	print format(k, '<' + str(w)), ':', d[k]