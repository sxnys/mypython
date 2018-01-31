# coding: utf-8

'''
1、字符串strip()、lstrip()、rstrip()方法去掉字符串两端的字符
2、删除单个固定位置的字符，使用切片 + 拼接
3、字符串的replace()方法或正则表达式re.sub()删除任意位置的字符
4、字符串的translate()方法，可以同时删除多种不同的字符
'''

s = '+++abc---'
print s.strip('+-')

s = 'abc:123'
print s[:3] + s[4:]

s = '\tabc\t123\txyz'
print s.replace('\t', '')  # 只能替换一种字符

s = '\tabc\t123\txyz\ropq'
import re
print re.sub('[\t\r]', '', s)  # 正则表达式可替换多种字符


# translate方法
# translate(映射表 [,要删除字符集])
import string
s = 'abc123456xyz'
print s.translate(string.maketrans('abcxyz', 'xyzabc'))

s = 'abc\refg\n1234\t'
print s.translate(None, '\t\r\n')

# unicode的translate方法
u = u'ni\u0301 ha\u030co, chi\u0304 fa\u0300n'
print u.translate(dict.fromkeys([0x0301, 0x030c, 0x0304, 0x0300]))