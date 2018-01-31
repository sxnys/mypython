# coding: utf-8

'''
使用字符串的str.startswith()和str.endswith()方法，多个匹配时使用元组
'''

s = 'sxn.py'

print s.endswith('.py')
print s.endswith('.sh')
print s.endswith(('.py', '.sh'))	# 以其中一个结尾即可