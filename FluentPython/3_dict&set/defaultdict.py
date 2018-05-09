"""
defaultdict处理找不到的键，背后实际上调用的时__missing__特殊方法
实例化：需要给构造方法提供一个可调用对象，该对象会在__getitem__找不到键的时候被调用
		用来生成默认值的可调用对象存放在default_factory的实例属性中
		defaultdict里的default_factory只会在__getitem__里被调用，所以dd.get(k)在k不是键时会返回None，而不是设定的默认值
dd = defaultdict(list)  key不在dd中，dd[key]会：
(1) 调用list()建立一个新列表
(2) 这个新列表作为值，key作为键放入dd中
(3) 返回这个列表的引用
"""

import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

# 实例化defaultdict对象
index = collections.defaultdict(list)

with open('article.txt') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word], sep=' : ')
