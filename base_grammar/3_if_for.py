#coding:utf-8

# Python代码的缩进规则:具有相同缩进的代码被视为代码块
# 缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，
# 更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误

# 条件语句
age = 20
if age >= 18:
	print 'your age is', age
	print 'adult'
print 'END'

# if-else
if age >= 18:
	print 'adult'
else:
	print 'non-adult'

# if-elif-else
score = 85
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'


# 循环语句
# for
L = [1, 2, 3]
sum = 0
for i in L:
	sum += i
print sum / 3.0

# while
sum = 0
x = 1
while x <= 100:
	sum += x
	x += 1
print sum
# break退出循环
sum = 0
x = 1
while True:
	sum += x
	x += 1
	if x > 100:
		break
print sum
# continue继续循环
sum = 0
x = 0
while True:
	x += 1
	if x > 100:
		break
	if x % 2 == 0:
		continue
	sum += x
print sum

# 多重循环
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
	for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
		if x < y:
			print str(x) + str(y)
