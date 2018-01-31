#coding:utf-8
print 45678 + 0x12fd2
print "Learn Python in imooc"
print 100 < 99
print 0xff == 255

print 'hello, python'	# 字符串单引号和双引号均可，中文注释Line1不能少
print '100 + 200 = ', 100 + 200

# python是动态语言，变量类型不固定
a = 1
print a
a = 'sxn'
print a
a = u'桑笑楠'	# 要输出中文字符串，必须在字符串前面加上u
print a

print '\"I\'m sxn\", he says.'	# 转义字符
# raw字符串，r'' 表示里面的字符串中不需要转义
print r'I am sxn.\n She is hys.\n'
# 但是不能表示多行字符串，还有含'和"的字符串，必须使用 r''' '''
print r'''\n"I'm sxn", he says.
"I'm hys", she says.\n'''

# 输出中文字符串，前面加u，输出多行用r''' '''
print ur'''
  静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
'''

# 四则运算
print 1 + 2 * 3
print 1 / 2 + 3
print 1 / 2.0 + 3
print 8 / 3
print 8 % 3
print 2.75 % 0.5
print 1.0 // 2.0  # 强制整除

# 乘方
print 2 ** 3
print -3 ** 2
print (-3) ** 2

# 十六进制、八进制
print 0xAF
print 010

# 布尔类型
# 与
print True and True
print True and False
print False and True
print False and False
# 或
print True or True
print True or False
print False or True
print False or False
# 非
print not True
print not False
# 0，空字符串''，None 看成False，其他数值和字符串看成True
# 并且满足短路原则，a & b -> a真则输出b，否则输出a，a | b -> a真则输出a，否则输出b
a = True
b = False
c = 'sxn'
d = 'hys'
print a and c
print b and c
print a or c
print b or c
print a and c or d
a = 'python'
b = ''
print 'hello,', a or 'world'
print 'hello,', b or 'world'