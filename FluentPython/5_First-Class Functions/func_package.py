"""
Python函数式编程最常用的两个模块 —— operator , functools
operator中有很多实用的算数计算的函数，functools中的常用函数较少（reduce, partial），具体 dir一下
"""

from functools import reduce, partial
from operator import mul, itemgetter, attrgetter, methodcaller
from collections import namedtuple


# operator模块中的多个算术运算函数避免写一些匿名函数，虽然我更喜欢匿名函数
def fact1(n):
	return reduce(lambda a, b: a * b, range(1, n + 1))

def fact2(n):
	return reduce(mul, range(1, n + 1))



# operator模块中还有能够替代从序列中取出元素(itemgetter)或读取对象属性(attrgetter)的lambda表达式
# itemgetter(0) 作用等同于 lambda fileds: fileds[0]
# itemgetter支持序列以及映射和任何实现了__getitem__方法的类
# attrgetter创建的函数根据名称提取对象的属性
# itemgetter和attrgetter会自行创建函数
metro_data = [
	('Tokyo', 'JP', 36.933, (35.689722, 169.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
for city in sorted(metro_data, key=itemgetter(1)):  # 按国家简称排序
	print(city)
print()
# 若多个参数传给itemgetter，返回提取的值构成的元组
for city in metro_data:
	print(itemgetter(1, 0, 3)(city))
print()

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
for city in metro_areas:
	print(city, city.coord.lat)
print()

name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):  # 按纬度排序
	print(name_lat(city))
print()



# methodcaller也会自行创建函数，会在对象上调用参数指定的方法，还可以冻结参数（与functools.partial类似）
# 指定的参数一定要是作用对象拥有的方法
s = 'The time has gone'
upcase = methodcaller('upper')
hiphenate = methodcaller('replace', ' ', '-')
print(upcase(s), hiphenate(s), sep='\n')
print()



# functools.partial冻结参数，基于一个函数创建一个新的可调用对象，把原函数的某些参数固定
triple = partial(mul, 3)
print( list(map(triple, range(1, 10))) )

import unicodedata
nfc = partial(unicodedata.normalize, 'NFC')
s1, s2 = 'café', 'cafe\u0301'
print(s1 == s2, nfc(s1) == nfc(s2))  # 和书上不一样，第一个我这里是Ture，难道3.6和3.4在这个地方有区别？

def tag(name, *content, cls=None, **attrs):
	""" 生成一个或多个HTML标签 """
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attrs_str = ''.join(' %s="%s"' % (attr, value) for attr, value in attrs.items())
	else:
		attrs_str = '' 
	if content:
		return '\n'.join('<%s%s>%s</%s>' % (name, attrs_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attrs_str)

picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='img.jpg'), picture.func, picture.args, picture.keywords, sep='\n')
print()

bin_to_dec = partial(int, base=2)
print(bin_to_dec('10101100010101101010'))
