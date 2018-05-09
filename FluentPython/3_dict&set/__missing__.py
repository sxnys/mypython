"""
所有的映射类型在处理找不到的键的时候都会涉及到__missing__方法
基类dict没有定义这个方法，但是能够知道它的存在 —— 一个类继承了dict并且实现了__missing__，当__getitem__遇到找不到的键时会自动调用__missing__
__missing__只会被__getitem__调用(如d[k])，对get或者__contains__(如in操作符)没有影响
"""

# 继承dict自定义一个映射类型，查询时将非字符串键转换为字符串


class StrKeyDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d = StrKeyDict([('2', 'two'), ('4', 'four')])
    print("d['2'] : {}".format(d['2']))
    print("d[2] : {}".format(d[2]))
    print("d['4'] : {}".format(d['4']))
    print("d[4] : {}".format(d[4]))
    print("d.get(2) : {}".format(d.get(2)))
    print("d.get('4') : {}".format(d.get('4')))
    print("d.get(1, 'N/A') : {}".format(d.get(1, 'N/A')))
    print('2 in d : {}'.format(2 in d))
    print('1 in d : {}'.format(1 in d))

    print("d[1] : {}".format(d[1]))
