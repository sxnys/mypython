"""
集合中的元素必须是可散列的，set本身不可散列，但是frozenset可散列（不可变集合）
{1, 2, 3}这样的字面量句法比set([1, 2, 3])这样的构造方法更快
"""

e = 1
s = {1, 2, 3, 4, 5}
z = {3, 4, 6, 7}
''' 集合的数学运算 '''
''' 所有的中缀运算符操作数必须是集合类型 '''
# 交集
s & z  # s.__and__(z)   s.intersection(it, ...) 它的参数可以是多个可迭代对象，不一定是set
z & s  # s.__rand__(z)
s &= z  # 就地修改  s.__iand__(z)   s.intersection_update(it, ...)

# 并集
s | z  # s.__or__(z)   s.union(it, ...) 不是就地修改，仅是求值
z | s  # s.__ror__(z)
s |= z  # s.__ior__(z)   s.update(it, ...) 就地修改

# 差集
s - z  # s.__sub__(z)    s.difference(it, ...)
z - s  # s.__rsub__(z)
s -= z  # s.__isub__(z)   s.difference_update(it, ...)

# 对称差集（并集和交集的差集）
s ^ z  # s.__xor__(z)    s.symmetric_difference(it, ...)
z ^ s  # s.__rxor__(z)
s ^= z  # s.__ixor__(z)    s.symmetric_difference_update(it, ...)



''' 集合的比较运算 '''
# 元素是否属于集合
e in s   # s.__contains__(e)
# s和z是否有公共元素
s.isdisjoint(z)
# 子集
s <= z   # s.__le__(z)   s.issubset(it, ...)
# 真子集
s < z    # s.__lt__(z)
# 父集
s >= z   # s.__ge__(z)   s.issuperset(it, ...)
# 真父集
s > z    # s.__gt__(z)



''' 集合中的其他方法 '''
s.add(e)
s.clear()
s.copy()   #浅复制
s.discard(e)   # if e in s then s.remove(e)
s.pop()
s.remove(e)    # 和 s.discard(e)不同的是，这里如果 e不是 s中的元素会抛出 KeyError异常
