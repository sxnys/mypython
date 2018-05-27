"""
自定义可调用类型，只需实现__call__方法，必须在内部维护一个状态
"""

import random

class BingoCage():

	def __init__(self, item):
		self._item = list(item)
		random.shuffle(self._item)  # 随机打乱

	def pick(self):
		try:
			return self._item.pop()
		except IndexError:
			raise LookupError('pick from empty BingoCage')

	def __call__(self):
		return self.pick()


if __name__ == '__main__':
	bingo = BingoCage(range(5))
	print(bingo.pick(), bingo())   # 两者等效
