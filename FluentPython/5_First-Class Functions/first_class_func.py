"""
python所有函数都是一等对象
一等对象：
·在运行时创建
·能赋值给变量或数据结构中的元素
·能作为参数传给函数 （高阶函数）
·能作为函数的返回结果 （高阶函数）
"""


'''
高阶函数（higher-order function）
接受函数作为参数，或者把函数作为返回结果 （map，filter - 依然是内置函数，reduce - 不再是内置函数）
'''
from functools import reduce
from operator import add
# reduce 和 sum都是一种归约函数，all和any也是内置的归约函数
print(reduce(add, range(100)))
print(sum(range(100)))
# all(iterable) : iterable每个元素都返回真值，返回True；all([]) => True
# any(iterable) : iterable中只要有真值，返回True；any([]) => Flase


'''
匿名函数：只能使用纯表达式，定义体中不能赋值，也不能使用while等Python语句
'''


'''
调用运算符(括号())可以应用到函数之外的其他对象上，内置函数callable()可以判断对象能否调用
可调用对象：
1、 用户定义的函数(def语句和lambda)
2、 内置函数
3、 内置方法
4、 方法 （类中定义的）
5、 类
6、 类的实例 （类中定义了__call__方法）
7、 生成器函数 （yield）
'''
print([callable(obj) for obj in (abs, str, 13)])