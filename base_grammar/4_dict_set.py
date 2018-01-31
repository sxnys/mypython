#coding:utf-8

# dict(字典)
# key:value形式
# 特点：
# 1. dict的第一个特点是查找速度快，
#    无论dict有10个元素还是10万个元素，查找速度都一样
# 2. 存储的key-value序对是没有顺序的
# 3. 作为 key 的元素必须不可变，字符串、整数、浮点数
#     都可以作为key，但是list不可以
d = {
	'sxn': 21,
	'hys': 22,
	'lcx': 23
}
# 返回长度key:value算一个
print len(d)
# 返回最值——key的字典序大小
print min(d)
print max(d)
# 访问，list必须使用索引返回对应的元素，而dict使用key
# 也可以使用get方法，若key不存在则返回None
# 所以key不能重复
print d['sxn']
print d.get('sxn')
print d.get('mxy')
# 更新，key元素是不可变的，但是dict本身是可变的
d['qjl'] = 24	# key不存在则添加
d['sxn'] = 20	# key存在则修改
print d    # 是按照key的字典序输出的
# 判断
if 'sxn' in d:
	print d['sxn']
# 删除
del d['sxn']
print d
print d.pop('hys')	# 删除key并返回其value
print d

# 字符串、整数、浮点数都可以作为key，但是list不可以
d1 = {
	21: 'sxn',
	22: 'hys',
	23: 'lcx'
}
print d1[21]
print d1.get(22)

# 遍历
for key in d:
	print key + ':', d[key]

# dict() 函数，通过其他映射或者序列对创建，或者通过
# 关键字参数创建
print dict([('name', 'hys'), ('age', '21')])
print dict(name = 'hys', age = 21)

# 字典的格式化字符串
# 在转换说明符中的%后面加上key值，后面再跟上说明元素
d1 = {
	'sxn': '21',
	'hys': '22',
	'lcx': '23'
}
print "hys's age is %(hys)s" % d1

# 常用字典方法
# 见书 P59 -



# set
# set持有一系列元素，这一点和 list 很像，
# 但是set的元素没有重复，而且是无序的，这点和dict的key很像
# 创建，set()方法传入一个list
s = set(['A', 'A', 'C', 'B', 'C', 1, 2])
print s
print len(s)
print min(s)
print max(s)

# 访问，set存储的无序集合，无法通过索引访问
# 可以使用in操作符判断
if 'A' in s:
	print 'A'
if 'a' in s:
	print 'a'

# 遍历
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]

# 更新
s = set([1, 2, 3])
s.add(4)	# 添加
print s
s.add(4)	# 若元素已存在在，add()不会报错，但是不会加进去
print s
s.remove(4)   # 删除，若元素不存在则会报错，所以删除操作应该
				# 要判断元素是否存在
if 3 in s:
	s.remove(3)
print s