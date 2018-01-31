#coding:utf-8

# 迭代   for..in..
# for循环迭代数列 1-100 并打印出7的倍数
for i in range(1, 101)[6::7]:
	print i

# 迭代永远是取出元素本身，而非元素的索引
# 想在 for 循环中拿到索引，使用enumerate()函数
# 索引迭代也不是真的按索引访问，而是由 enumerate() 函数
# 自动把每个元素变成 (index, element)这样的tuple，
# 再迭代，就同时获得了索引和元素本身
L = ['A', 'B', 'C', 'D']
for index, name in enumerate(L):
	print index, '-', name
# 实际上是这样的
for t in enumerate(L):
	index = t[0]
	name = t[1]
	print index, '-', name

# zip()函数可以把两个 list 变成一个 list
print zip([1, 2, 3], ['A', 'B', 'C'])

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1,5), L):
    print index, '-', name


# dict的迭代
# dict 对象有一个 values() 方法，
# 这个方法把dict转换成一个包含所有value的list
# 还有一个 itervalues() 方法，用 itervalues() 方法
# 替代 values() 方法，迭代效果完全一样
d = {
	'sxn': 21,
	'hys': 22,
	'lcx': 23
}
for v in d.values():
	print v
for v in d.itervalues():
	print v
# 1. values() 方法实际上把一个dict转换成了包含value的list
# 2. 但是itervalues()方法不会转换，它会在迭代过程中依次从 
#    dict 中取出 value，所以itervalues()方法比values() 方法
#    节省了生成 list 所需的内存。
# 3. 打印itervalues()发现它返回一个<dictionary-valueiterator>
#    对象，这说明在Python中，for 循环可作用的迭代对象远不止 
#    list，tuple，str，unicode，dict等，任何可迭代对象都可以
#    作用于for循环，而内部如何迭代我们通常并不用关心。

# dict 对象的 items() 方法返回key和value
# items() 方法把dict对象转换成了包含tuple的list
print d.items()
for key, value in d.items():
	print key, '-', value
# 和 values() 有一个 itervalues() 类似，
# items() 也有一个对应的 iteritems()，iteritems()
# 不把dict转换成list，而是在迭代过程中不断给出 tuple，
# 所以， iteritems() 不占用额外的内存
for key, value in d.iteritems():
	print key, '-', value