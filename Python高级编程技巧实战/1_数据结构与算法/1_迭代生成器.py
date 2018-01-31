# coding: utf-8

'''
如何在列表、字典、集合中根据条件筛选数据
'''
from random import randint

# 过滤列表中的负数列表
print u'---过滤列表---'
data = [randint(-10, 10) for _ in xrange(10)]
print data
# 1、过滤函数
print u'过滤函数filter: ', filter(lambda x: x >= 0, data)
# 2、列表解析
print u'列表解析：', [x for x in data if x >= 0]

# 筛出字典中值高于90的项
print u'\n---筛选字典---'
d = {x: randint(60, 100) for x in xrange(1, 21)}
print d
# 字典解析
print u'字典解析：', {k: v for k, v in d.iteritems() if v > 90}

# 筛出集合中能被3整除的数
print u'\n---筛选集合---'
s = set(data)
# 集合解析
print u'集合解析：', {x for x in s if x % 3 == 0}