# coding:utf-8

# 函数式编程
# 1、变量可以指向一个函数
# 2、函数名其实就是指向函数的变量
# 3、高阶函数是指能够接收函数作为参数的函数

f = abs
print f(-1)

# 高阶函数
def add(x, y, f):
	return f(x) + f(y)
print add(-3, 5, abs)

# map()函数
# 它接收一个函数 f 和一个 list，并通过把函数 f 
# 依次作用在 list 的每个元素上，得到一个新的 list 并返回
def f(x):
	return x * x
print map(f, [1, 2, 3, 4, 5])

def format_name(s):
    t = s[0].upper()
    t = t + s[1:].lower()
    return t
# str.capitalize() 首字母大写其余小写
print map(format_name, ['adam', 'LISA', 'barT'])


# reduce()函数
# reduce()函数接收一个函数 f，一个list，传入的函数f必须只能接收
# 两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
# reduce()还可以接收第3个可选参数，作为计算的初始值
def f(x, y):
	return x * y
print reduce(f, [1, 2, 3, 4, 5]) # 即连乘
print reduce(f, range(1, 121)) # 求阶乘


# filter()函数 很有用哦
# filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对
# 每个元素进行判断，返回 True或 False，filter()根据判断结果
# 自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
def is_odd(x):
	return x % 2 == 1
print filter(is_odd, [1, 2, 3, 4, 5, 6]) # 删除偶数

def is_not_empty(s):	# 删除 None 或者空字符串
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符
# 当rm为空时，默认删除空白符(包括'\n', '\r', '\t', ' ')


# 自定义排序函数
# sorted()可以接收一个比较函数来实现自定义
# 排序，比较函数的定义是，传入两个待比较的元素x, y，如果x 
# 应该排在 y 的前面，返回-1，如果 x 应该排在 y 的后面，
# 返回 1。如果 x 和 y 相等，返回 0
print sorted([3, 2, 6, 1, 5, 4])

def reverse_cmp(x, y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0
print sorted([3, 2, 6, 1, 5, 4], reverse_cmp)


# 偏函数
# functools.partial可以把一个参数多的函数变成一个参数少的新函数，
# 少的参数需要在创建时指定默认值
import functools
int2 = functools.partial(int, base = 2)
print int2('1010')

sorted_ignore_case = functools.partial(sorted, key = str.lower)
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])



# 返回函数
# Python的函数可以返回函数
def calc_prod(lst):
    def prod(x, y):
        return x * y
    def c_prod():
        return reduce(prod, lst)
    return c_prod
f = calc_prod([1, 2, 3, 4])
print f()
# 闭包
# 内层函数引用了外层函数的变量（参数也算变量），
# 然后返回内层函数的情况，称为闭包（Closure）
# 闭包的特点是返回的函数还引用了外层函数的局部变量，
# 所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变
def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i * i
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的 x 表示函数参数
# 只能有一个表达式，不写return，返回值就是该表达式的结果
print sorted([1, 3, 9, 5, 0], lambda x, y: -cmp(x, y))
print map(lambda x: x * x, [1, 2, 3, 4, 5])
myabs = lambda x: x if x >= 0 else -x
print myabs(-1)
print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])