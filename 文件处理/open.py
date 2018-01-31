# coding:utf-8

# 文件打开方式
# open(name[,mode[buf]]) 默认只读方式打开
# name: 文件路径
# mode: 打开方式(只读，只写，读写)
# buf: 缓冲buffering大小

#    mode     
#    'r'  ---------  只读方式打开（文件必须存在）
#    'w'  ---------  只写方式打开（文件不存在新建否则清空）
#    'a'  ---------  追加方式打开（文件不存在创建文件）
#  'r+'/'w+'  -----  读写方式打开
#    'a+' ---------  追加和读写方式打开
#  'rb', 'wb', 'ab', 'rb+', 'wb+', 'ab+': 二进制方式打开

f = open('read.txt', 'w')
f.write('sxn')
f.close()

f = open('read.txt', 'a')
f.close()

f = open('read.txt', 'w')
f.close()

f = open('read.txt', 'w')
f.write('sxn\nhys\nlcx\n')
f.close()