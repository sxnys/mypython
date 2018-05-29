"""
UserDict不是dict的子类，但有一个data属性是dict实例。是最终存储数据的地方
UserDict继承的是MutableMapping
"""


from collections import UserDict

class StrKeyDict(UserDict):

	def __missing__(self, key):
		if isinstance(key, str):
			raise KeyError(key)
		return self[str(key)]

	def __contains__(self, key):
		return str(key) in self.data

	def __setitem__(self, key, value):
		self.data[str(key)] = value
		