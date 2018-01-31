# coding: utf-8

'''
实现历史纪录功能
猜数字游戏中加入历史纪录功能，显示最近猜过的数字

1、使用collections中的deque，一个双端循环队列
2、程序退出前可以使用pickle将队列对象存入文件，再次运行程序时将其导入
''' 

from random import randint
from collections import deque
import pickle

N = randint(1, 100)
q = []
# 加载历史纪录文件
try:
	q = pickle.load(open('history'))
except:
	pass
# print q
history = deque(q, 5)

def guess(k):
	if k == N:
		print 'Right!'
		return True
	elif k < N:
		print '%d is less-than N' % k
	elif k > N:
		print '%d is greater-than N' % k
	return False

while True:
	line = raw_input('please input your number: ')
	if line.isdigit():
		k = int(line)
		history.append(k)
		if guess(k):
			break
	elif line == 'history' or line == 'h?':
		print list(history)

# 更新历史纪录文件
pickle.dump(history, open('history', 'w'))