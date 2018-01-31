# coding: utf-8

'''
实现一个连续浮点数发生器FloatRange(start, end, step)
reversed(l): 返回一个l的反向迭代器，与iter(l)相对，实质上是现实了内部的__reversed__方法
'''

class FloatRange:
	def __init__(self, start, end, step=0.1):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		k = self.start
		while k <= self.end:
			yield k
			k += self.step

	def __reversed__(self):
		k = self.end
		while k >= self.start:
			yield k
			k -= self.step

print u'正向迭代'
for i in FloatRange(1.0, 5.0, 0.5):
	print i

print u'\n反向迭代'
for i in reversed(FloatRange(1.0, 5.0, 0.5)):
	print i