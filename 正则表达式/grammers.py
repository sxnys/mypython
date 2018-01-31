# coding: utf-8

# 基本语法
# 匹配单个字符
# . 		匹配任意字符（除\n）
# [...]		匹配字符集
# \d  \D 	匹配数字  非数字
# \s  \S 	匹配空白  非空白
# \w  \W 	匹配单词字符[a-z A-Z 0-9]	非单词字符

import re
ma = re.match(r'{[abc]}', '{a}')
print ma.group()

ma = re.match(r'{[a-z]}', '{c}')
print ma.group()

ma = re.match(r'{[a-zA-Z0-9]}', '{1}')
print ma.group()

ma = re.match(r'\[[\w]\]', '[a]')
print ma.group()


# 匹配多个字符
# *					匹配前一个字符0次或无限次
# +					匹配前一个字符1次或无限次
# ?					匹配前一个字符0次或1次
# {m} / {m,n}		匹配前一个字符m次或m到n次
# *? / +? / ??		匹配模式变为非贪婪（尽可能少的匹配字符）

# 匹配开头字母大写其余小写的单词
# 必须从头开始匹配，什么地方收尾无所谓
ma = re.match(r'[A-Z][a-z]*', 'China1')
print ma.group()

# 匹配python变量名
ma = re.match(r'[_a-zA-Z]+[_\w]*', '_sxn123')
print ma.group()

# 匹配0~99
ma = re.match(r'[1-9]?[0-9]', '90')
print ma.group()
ma = re.match(r'[1-9]?[0-9]', '09')
print ma.group()

# 匹配{m}, {m,n}
ma = re.match(r'[a-zA-Z0-9]{6}', 'abc123')
print ma.group()
ma = re.match(r'[a-zA-Z0-9]{6,10}', 'abc12345')
print ma.group()

# 
ma = re.match(r'[0-9][a-z]*?', '1abc')
print ma.group()
ma = re.match(r'[0-9][a-z]+?', '1abc')
print ma.group()
ma = re.match(r'[0-9][a-z]??', '1abc')
print ma.group()


# 边界匹配
# ^		匹配字符串开头
# $		匹配字符串结尾
# \A / \Z 	指定的字符串匹必须出现在开头/结尾

# 以字符开头，以@163.com结尾
ma = re.match(r'^[\w]{4,10}@163.com$', 'imooc@163.com')
print ma.group()

# 以imooc开头 
ma = re.match(r'\Aimooc[\w]*', 'imoocpython')
print ma.group()


# 分组匹配
# |				匹配左右任意一个表达式
# (ab)			括号中表达式作为一个分组
# \<number>		引用编号为num的分组匹配到的字符串
# (?P<name>)	分组起一个别名
# (?P=name)		引用别名为name的分组匹配字符串

# 匹配0~100
ma = re.match(r'[1-9]?\d$|100', '9')
print ma.group()

# 匹配163，126邮箱
ma = re.match(r'[\w]{4,6}@(163|126).com', 'imooc@126.com')
print ma.group()

#
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print ma.group()

ma = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)', '<book>python</book>')
print ma.group()