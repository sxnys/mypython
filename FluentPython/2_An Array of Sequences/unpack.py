# 元组拆包，但拆包的操作同样适用于任何可迭代对象

# 平行赋值
lax_coordinates = (33.9425, -118.409056)
latitude, longitude = lax_coordinates
print(latitude, longitude)

a, b = 1, 2
b, a = a, b
c = a, b
d = (b, a)
print(a, b, c, d)


# *
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)

a, b, *rest = range(5)
print(a, b, rest)
a, *rest, b, c = range(10)
print(a, b, c, rest)


# 嵌套元组拆包
# 接受元组的嵌套结构符合表达式本身的嵌套结构
metro_areas = [
	('Tokyo', 'JP', 36.933, (35.689722, 169.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
	('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
	('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
	if longitude <= 0:
		print(fmt.format(name, latitude, longitude))