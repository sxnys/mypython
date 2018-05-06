# dict是python的基石，跟dict有关的内置函数都在__builtins__.__dict__模块中
# dict依赖于散列表，是dict性能出众的根本原因
# 标准库里面所有映射类型都是用dict实现的
# 只有可散列的数据类型才可以用作这些映射里的键，原子不可变数据类型都是可散列的（str，bytes，数值类型），frozenset也是可散列的，当元组包含的所有元素都是可散列的话才是可散列的
# defaultdict和OrderedDict是dict的变种，在collections模块中


# dict不同的构造方法
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])   # 亲测这里列表元组都可以，不管是里面的键值对还是外面整体
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)  # True


# 字典推导
# python3中dict没有了iteritems类似的方法了，items方法就是py2里面的iteritems方法
DIAL_CODES = [
	(86, 'China'),
	(91, 'India'),
	(1, 'United States'),
	(62, 'Indonesia'),
	(55, 'Brazil'),
	(92, 'Pakistan'),
	(880, 'Bangladesh'),
	(234, 'Nigeria'),
	(7, 'Russia'),
	(81, 'Japan'),
]
country_code = {country: code for code, country in DIAL_CODES}
example = {code: country.upper() for country, code in country_code.items() if code < 66}


# dict中一些常见的映射方法，一些特殊方法没有列出，defaultdict和OrderedDict会有一些各自独有的方法
# d.clear()
# d.copy()：浅拷贝
# * d.fromkeys(it, [initial])：将迭代器it里的元素设置为映射里的键，如果有initial参数则把它作为这些键对应的初始值（默认None）
# * d.get(k, [default])
# d.items()
# d.keys()
# d.values()
# d.pop(k, [default])
# d.popitem()：随机返回一个键值对并从字典里删除
# * d.setdefault(k, [default])：d.get(k) if k in d.keys() else d[k] = default and return it  书中表里描述错误
# * d.update(m, [**kargs])

# 关于setdefault的妙用见setdefault.py