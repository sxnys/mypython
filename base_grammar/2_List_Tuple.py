#coding:utf-8

# List集合
L = ['sxn', 'hys', 'lcx']
print L
# 动态语言，List元素类型可以不同
L = ['sxn', 21, 'hys', True]
print L
print L[0]
print L[1]
print L[2]
print L[3]
# 下标负的对应集合的倒数第几个
print L[-1]
print L[-2]
print L[-3]
print L[-4]

# 添加新元素
L = ['A', 'B', 'C']
L.append('D')	# 在集合末尾添加
print L
L.insert(1, 'X')	# 在指定索引位置添加
print L
L.extend(['D', 'E', 'F'])	# 在末尾追加另一个序列的多个值，等同于加法
print L

# 删除元素
L = ['A', 'B', 'C', 'D']
print L.pop()		# 删除最后一个元素，并返回这个元素
print L.pop(1)	# 删除指定索引位置的元素，并返回
print L
del L[0]
print L
L.remove('C')	# 删除某个值的第一个匹配项
print L

# 替换元素，直接索引
L = ['A', 'B', 'C']
L[0] = 'C'
L[-1] = 'A'
print L

# list 函数
L = list('Hello')
print L

# 统计元素出现的次数
L = [1, 2, 3, 'A', 1, 'A', 'B', 'A']
print L.count(1)
print L.count(2)
print L.count('A')

# 查询某个值在列表中第一次出现的索引位置
print L.index('A')
print L.index(1)

# 列表反转
L.reverse()
print L

# 列表排序(字典序)
L.sort()
print L
print sorted(L)   # 获得已排序的列表副本，而原序列不变
# sort()函数接受三个参数,cmp,key,reverse
L = [5, 2, 9, 7]
L.sort(cmp)
print L
L = ['aab', 'ba', 'caa', 'abcd']
L.sort(key = len)
print L
L = [5, 2, 9, 7]
L.sort(reverse = True)
print L


### Tuple(元组)，与List的不同在于其不可修改
T = ('A', 'B', 'C')
print T[0]
print T[-1]
# append, pop, insert方法不可用, 也不可以使用索引进行修改 

# 单元素Tuple
T = ()
print T
T = (1)  # ()既可以表示tuple,又可以作为括号表示运算时的优先级，
print T	 # 结果(1)被Python解释器计算出结果1,导致我们得到的不是tuple，而是整数1
T = (1,)	# 单元素应在末尾加一个逗号
print T
T = (1, 2, 3,)	# 多元素无所谓
print T

# Tuple + List
T = ('a', 'b', ['A', 'B'])
L = T[2]	# 为一个List对象，是可变的，Tuple只是指向不变
L[0] = 'a'
L[1] = 'b'
print T
T = ('a', 'b', ('a', 'b'))	# 这样是不可变的，大Tuple里的第三个元素还是Tuple

# tuple函数
print tuple('123abc')
print tuple([1, 2, 3, 'a'])
print tuple((1, 2, 3))

# 几个常用函数
L = [1, 2, 3, 4, 5]
# 获得长度
print len(L)
# 获得最值
print min(L)
print max(L)
L = ['wd', '21w3', 'dcw3']
print min(L)
print max(L)
