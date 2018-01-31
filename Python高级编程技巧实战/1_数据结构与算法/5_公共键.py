# coding: utf-8

'''
快速找出多个字典中的公共键
利用集合的交集操作：
1、使用字典的viewkeys方法得到字典keys的集合
2、使用map函数得到所有字典的keys的集合
3、使用reduce函数得到所有字典keys的集合的交集
'''

from random import randint, sample

# 随机取样生成字典
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print s1, s2, s3

print reduce(lambda a, b: a & b, map(dict.viewkeys, [s1, s2, s3]))