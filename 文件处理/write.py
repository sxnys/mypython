# coding:utf-8

# 文件写入和写缓存
# write(str): 将字符串写入文件
# writeline(sequence_of_strings): 写多行到文件，参数为可迭代对象

f = open('read.txt', 'w')
f.write('sxn')
f.close()

f = open('read.txt', 'w')
f.writelines(['sxn', 'hys', 'lcx'])
f.close()

# 写缓存
# 当主动调用close()或flush方法时才会写入磁盘
# 或者写入的数据量超过了写缓存的容量也会写入磁盘
f = open('write.txt', 'w')
for i in range(1000):
	f.write('test write ' + str(i) + '\n')
