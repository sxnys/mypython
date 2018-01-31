# coding:utf-8

# 文件读取方式
# read([size]): 读取文件（读取size个字节，默认读取全部）
# readline([size]): 读取一行
# readlines([size]): 读取完文件，返回每一行所组成的列表

f = open('read.txt')
print f.read()
f.close()

f = open('read.txt')
print f.readline(2)
f.close()

f = open('read.txt')
L = f.readlines()
print L
f.close()

# 迭代器访问文件
f = open('read.txt')
iter_f = iter(f)
lines = 0
for line in iter_f:
	lines += 1
print lines
f.close()