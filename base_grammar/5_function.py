#coding:utf-8

# 一些常见函数
# 绝对值
print abs(-20)
# 比较函数，返回-1，0，1
print cmp(1, 2)
print cmp(2, 1)
print cmp(1, 1)
# 数据类型转换函数
print int('123')
print int(3.14)
print str(1234)
print str(3.14)
# sum函数，可以接受list作为参数
L = []
x = 1
while x <= 100:
	L.append(x * x)
	x += 1
print sum(L)

L = xrange(1, 101)
print sum([i * i for i in L])
# range, xrange创建数列
# xrange用法与range完全相同，所不同的
# 是生成的不是一个数组，而是一个生成器
# 要生成很大的数字序列的时候，用xrange会比range性能优很多
print range(10)
L = range(1, 11)  # 不包含最后一个数字
print L
print range(1, 21, 2)
L = list(xrange(8))		# list也是一个函数
print L
# 大小写字母转换函数
print 'abc'.upper()
print 'AbC'.lower()
# 一些数学包里的函数
import math
print math.pi
print math.sin(math.pi / 2.0)
print math.cos(math.pi)
print math.sqrt(3)


### 自定义函数 ###
# 若没有return返回值，则结果显示None
def Abs(x):
	if x >= 0:
		return x
	else:
		return -x

# 返回多值，表面上可以返回多个值，但是实际返回的还是单一值
# 事实上，Python的函数返回多值其实就是返回一个tuple
def get_pos_2(x, y):
	return x ** 2, y ** 2
x2, y2 = get_pos_2(2, 3)
print x2, y2
r = get_pos_2(2, 3)
print r
print get_pos_2(2, 3)

# 递归函数
# 斐波那契
def fabi(n):
	if n == 1 or n == 2:
		return n
	else:
		return fabi(n-1) + fabi(n-2)
n = 10
print fabi(n)
# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print a, '-->', c
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

# 默认参数
# int(a, n)第二个参数为传入的进制数，不传入默认十进制
print int('10110111', 2)
print int('123', 8)
print int('ABCD', 16)
# 由于函数的参数按从左到右的顺序匹配，
# 所以默认参数只能定义在必需参数的后面
def power(x, n = 2):
	return x ** n
print power(3, 4)
print power(5)

# 可变参数
# 可变参数的名字前面有个 * 号，
# 可以传入0个、1个或多个参数给可变参数
# Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，
# 因此，在函数内部，直接把变量 args 看成一个 tuple 就好了
def average(*v):
	if len(v) == 0:
		return 0
	sum = 0.0
	for i in v:
		sum += i
	return sum / len(v)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)