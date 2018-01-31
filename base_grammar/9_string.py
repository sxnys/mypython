#coding:utf-8

# 格式化（较详细内容见书 P46）
# 格式化操作符 %, 右操作数可以是任意东西
format = 'Hello, %s! What\'s your %s?'
s = ('hys', 'age')
print format % s

format = '%.3f'	# 对于其他数据类型类似
import math
print format % math.pi
print '%.3f' % math.pi
# 模板字符串 $
from string import Template
s = Template('Hello $name!')
print s.substitute(name = 'hys')

s = Template("Hello $name! What's your $thing?")
d = {}		# 利用dict来实现多个模板
d['name'] = 'hys'
d['thing'] = 'age'
print s.substitute(d)

s = Template('Hello, ${x}s!')	# 替换单词的一个部分用{}括起来
print s.substitute(x = 'hy')


# 常用字符串常量（string模块中）
import string
print string.digits		# 包含所有0~9数字的字符串
print string.letters	# 包含所有字母（大小写）的字符串
print string.lowercase	# 包含所有小写字母的字符串
print string.uppercase	# 包含所有大写字母的字符串
print string.printable	# 包含所有可打印字符的字符串
print string.punctuation	# 包含所有标点符号的字符串


# 常用字符串方法
# find() 查询子字符串的索引（最左端），找不到返回-1
print 'I love you, hys!'.find('hys')
print 'I love you, hys! hys!'.find('hys', 13)  # 提供起点
print 'I love you, hys! hys!'.find('hys', 13, 14)  # 提供始末点

# join() 连接字符串列表
print '+'.join(['1', '2', '3'])
print '+'.join('12345')

# upper()和lower()大小写转换
print 'hys'.upper()
print 'hys'.upper().lower()

# replace() 返回某字符串所有匹配项均被替换后的字符串
print 'I love hys! I love hys very much!'.replace('hys', 'lcx')

# split() 将字符串分割成序列，是join()方法的逆方法
print 'I love hys!'.split()	 # 不提供参数则将所有空格作为分隔符
print '1+2+3+4'.split('+')	# 接受分隔符参数
print '1+2+3+4'.split(',')

# strip() 将字符串两侧的空格去掉，lstrip()和rstrip()类似的左右
print '   I love you,  hys!  '.strip()
# 接受参数s，删除两侧包含s中有的字符
print '*** I love you,  *hys! .!!  '.strip('* !')

# translate() 与replace()方法类似，但只处理单个字符，可以进行多个替换
# maketrans()方法接受两个等长字符串，表示第一个字符串中每个字符都
# 用第二个字符串相同位置的字符替换，但长度始终是256(ASCII)
# maketrans()方法创建的表可以作为translate()方法的参数
table = string.maketrans('cs', 'kz')
print len(table)
print table[97:123]
print string.maketrans('', '')[97:123]	# 空字符不改变什么

table = string.maketrans('hys', 'lcx')
print 'I love hys! hhda'.translate(table)
# 接受第二个参数，删除相应字符，与strip()参数类似
print 'I love hys! hhda'.translate(table, '! ')
