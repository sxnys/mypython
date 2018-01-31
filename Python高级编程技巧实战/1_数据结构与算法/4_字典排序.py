# coding: utf-8

''' 根据字典中值的大小对字典排序
使用内置函数sorted
1、利用zip将字典数据转化为元祖列表
2、传递sorted函数中的key参数
Tips：使用values、keys、items的迭代对象更加省存储
'''

from random import randint
d = {x: randint(60, 100) for x in 'xyzabc'}
print d

# 使用zip转换
d1 = zip(d.itervalues(), d.iterkeys())	# 值作为元祖第一项
print sorted(d1)

# 传递key参数
print sorted(d.iteritems(), key=lambda x: x[1])