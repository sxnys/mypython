'''python2.x 与 python3.x 的差异'''

# 字符
# 很关键的差别，py3中的str类型就是py2中的 Unicode类型，但是py3中的bytes类型不是py2中的 str 换个名称那么简单，
# 而且和py2中的bytes还不一样

# print
# py2 和 py3 最直观的差别
# py2 中的 print 语句 变成了py3中的 print 函数


# range
# python2 中 range返回列表，xrange返回迭代器，不产生额外空间，所以xrange更适用于迭代
# python3中去掉了 xrange，保留了range，但是此时的range就是py2中的xrange，不再是一个列表，而是迭代器


# 除法
# python2 中 x / y 为整除运算，x // y 为浮点数除法
# python3 刚好相反


# reduce
# python2：内置方法
# python3：在functools模块中


# python2中许多对象方法的返回值都是列表，比如range、zip、map、filter很多很多
# python3中的这些方法都不会直接返回list，而都是返回对应的可迭代对象，其实是视图


# dict的.keys()、.items 和.values()方法在python3中返回字典视图，可以理解为迭代器，而之前python2的iterkeys()等函数都被废弃
# 同时去掉的还有 dict.has_key()，用 in替代它吧