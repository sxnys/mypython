# coding: utf-8

'''
并行：同时迭代多个列表（每个列表存储不同数据）
串行：一组数据分别存储在多个列表

1、并行：使用内置函数zip，能将多个可迭代对象合并，每次迭代返回一个元组
2、串行：使用标准库的itertools.chain，能将多个可迭代对象连接
'''

from random import randint

''' 并行迭代
'''
chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]
total = []

# 使用zip合并三个列表，迭代计算总分，每次迭代的是一个元组
for c, m, e in zip(chinese, math, english):
	total.append(c + m + e)

print u'语文成绩：'
print chinese
print u'数学成绩：'
print math
print u'英语成绩：'
print english
print u'总分：'
print total


''' 串行迭代
'''
from itertools import chain
class1 = [randint(60, 100) for _ in xrange(40)]
class2 = [randint(60, 100) for _ in xrange(42)]
class3 = [randint(60, 100) for _ in xrange(45)]
class4 = [randint(60, 100) for _ in xrange(43)]

count = 0

for student in chain(class1, class2, class3, class4):
	if student > 90:
		count += 1

print count