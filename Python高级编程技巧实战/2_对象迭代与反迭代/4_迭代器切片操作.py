# coding: utf-8

'''
使用标准库中的itertools.islice，返回一个迭代对象切片的生成器，会消耗迭代器对象
islice(iterable, [start,] stop[, step]), stop不能为负数
'''

from itertools import islice

l = range(1, 21)
print l

t = iter(l)

print u'\n切片5:10'
for i in islice(t, 5, 10):
	print i

# islice会消耗迭代器对象，即下面的迭代会从上一次迭代结束的地方开始
print u'\n正常迭代'
for i in t:
	print i

print u'\n切片5:'
for i in islice(t, 5, None):
	print i