# coding: utf-8

'''
可迭代对象：存在内置函数__iter__或者__getitem__，可以使用iter()方法得到它的迭代器对象
迭代器对象：只存在next()方法

for循环机制：
for x in l: ......
实质上是，取l的迭代器对象(iter(l))的每一个next()，直到捕捉到StopIteration异常
'''
'''
从网络抓取各个城市的气温信息并依次显示
若一次抓取所有的信息再显示的话，显示第一个城市气温时有延时且浪费存储空间
现在以“用时访问”策略，并且把所有城市气温封装到一个对象里，可以用for语句迭代
'''

from collections import Iterable, Iterator
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 定义天气的迭代器对象，继承Iterator
class WeatherIterator(Iterator):
	def __init__(self, cities):
		self.cities = cities
		self.index = 0

	def getWeather(self, city):
		response = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		data = response.json()['data']['forecast'][0]
		return '%s: %s , %s' % (city, data['low'], data['high'])

	def next(self):
		# 当index到达城市列表尾端，抛出StopIteration异常
		if self.index == len(self.cities):
			raise StopIteration
			
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)

# 定义天气的可迭代对象，继承Iterable
class WeatherIterable(Iterable):
	def __init__(self, cities):
		self.cities = cities

	def __iter__(self):
		return WeatherIterator(self.cities)

if __name__ == '__main__':
	cities = ['北京', '上海', '广州', '深圳', '南京', '成都']
	for x in WeatherIterable(cities):
		print x