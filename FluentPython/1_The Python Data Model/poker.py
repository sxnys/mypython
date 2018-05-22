# 魔术方法也称为双下方法（dunder method）
# 

import collections
from random import choice

# namedtuple用来构建只有少数属性但是没有方法的对象
# 访问其中的属性，可以像元组那样使用索引，也可以像一般对象那样使用点操作符(.)
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(i) for i in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	# 可以利用索引查找元素，而且使得它的对象可迭代
	def __getitem__(self, pos):
		return self._cards[pos]

	def __repr__(self):
		return 

if __name__ == '__main__':
	deck = FrenchDeck()
	print(len(deck))
	print()

	print(deck[0], deck[-1], deck[:3], deck[12::13], sep='\n')
	print()

	# 随机选择一个元素
	print(choice(deck))
	print(choice(deck))
	print(choice(deck))
	print()

	for card in deck:
		print(card, card[0], card.suit)	# 打印每一张牌，打印数字，打印花色
	
	# 扑克牌排序
	suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
	def spades_high(card):
		rank_value = FrenchDeck.ranks.index(card.rank)
		return len(suit_values) * rank_value + suit_values[card.suit]
	for card in sorted(deck, key=spades_high):
		print(card)