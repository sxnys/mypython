# coding: utf-8

'''
让字典保持有序
使用collections.OrderedDict
'''

from random import randint
from time import time
from collections import OrderedDict

d = OrderedDict()
players = list('ABCDEFG')
start = time()
l = len(players)

for i in xrange(l):
	raw_input()
	p = players.pop(randint(0, len(players) - 1))
	end = time()
	print p, i + 1, end - start
	d[p] = (i + 1, end - start)

print '-' * 20
for i in d:
	print i, d[i]