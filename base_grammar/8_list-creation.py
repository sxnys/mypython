#coding:utf-8

# 1 ~ 10
print range(1, 11)

# 列表生成式
# 写列表生成式时，把要生成的元素如x * x 放到前面，
# 后面跟 for 循环，就可以把list创建出来
# 1 * 1 ~ 10 * 10
print [x * x for x in range(1, 11)]
# [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x * (x + 1) for x in range(1, 100, 2)]

# 复杂的表达式
# HTML表格
d = {
	u'桑笑楠': 21,
	u'胡云裳': 22,
	u'吕超贤': 23
}
tds = ['<tr><td>%s</td><td>%s</td></tr>'
		%(name, age) for name, age in d.iteritems()]
print '<table border = "1">'
print '<tr><th>Name</th><th>Age</th><tr>'
print '\n'.join(tds)	# 字符串的join()方法把list拼接成一个字符串
print '</table>'

# 在生成的表格中，对于没有及格的同学，请把分数标记为红色
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        td = '<td style = "color:red">'
    else:
        td = '<td>'
    s = '<tr><td>%s</td>' + td + '%s</td></tr>'
    return s % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

# 条件过滤
# 2^2, 4^2, ..., 10^2
print [x * x for x in range(1, 11) if x % 2 == 0]
# 把list中的所有字符串变成大写后返回，非字符串元素将被忽略
#  isinstance(x, str) 可以判断变量 x 是否是字符串
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]
print toUppers(['Hello', 'world', 101])

# 多层表达式
print [m + n for m in 'ABC' for n in '123']
# 效果等同于
L = []
for m in 'ABC':
	for n in '123':
		L.append(m + n)
print L