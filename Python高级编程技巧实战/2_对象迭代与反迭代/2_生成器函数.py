# coding: utf-8

'''
实现一个可迭代对象的类，能够迭代出给定范围内的所有素数
将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
'''

class PrimeNumbers:
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isPrime(self, k):
		if k < 2:
			return False
		for i in xrange(2, k):
			if k % i == 0:
				return False

		return True

	def __iter__(self):
		for k in xrange(self.start, self.end + 1):
			if self.isPrime(k):
				yield k

# print PrimeNumbers(1, 100)
for x in PrimeNumbers(1, 100):
	print x