# coding: utf-8

''' 词频分析
1、找到某随机序列中出现次数最多的3个元素
2、找到某英文文章中出现次数最多的10个单词
使用collections.Counter
'''

''' 随机列表中的元素
'''
from random import randint
data = [randint(0, 20) for _ in xrange(30)]
print data
# 使用字典
c = dict.fromkeys(data, 0)	# data中的每一个元素作为键，0作为值，统一初始化
for i in data:
	c[i] += 1
print c
# 使用collections.Counter
from collections import Counter
c2 = Counter(data)
print c2
print c2.most_common(3)	# 出现频度最高的三个元素

''' 词频分析
'''
text = open('article.txt').read()
import re
c3 = Counter(re.split('\W+', text))	# 用正则表达式对文章做分割
print c3
print c3.most_common(10)
