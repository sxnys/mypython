# coding:utf-8

# os模块
import os

# os模块打开文件
# os.open(filename, flag[,mode])
# flag: 文件打开方式
#        os.O_CREAT: 创建文件
#		 os.O_RDONLY: 只读方式打开
#		 os.O_WRONLY: 只写方式打开
#		 os.O_RDWR: 读写方式打开
fd = os.open('sxn.txt', os.O_CREAT | os.O_RDWR)

# 写入文件
# os.write(fd, string)
n = os.write(fd, 'sxn hys')

# 文件指针操作
# os.lseek(fd, pos, how)
l = os.lseek(fd, 0, os.SEEK_SET) # 返回文件开端
print l

# 读取文件
# os.read(fd, buffersize)
str1 = os.read(fd, 3)
print str1

# 关闭文件
# os.close(fd)
os.close(fd)


# access(path, mode)
# 判断文件权限: 
# F_OK存在，权限: R_OK, W_OK, X_OK
print os.access('sxn.txt', os.F_OK)
print os.access('1.txt', os.F_OK)
print os.access('sxn.txt', os.R_OK)
print os.access('sxn.txt', os.W_OK)
print os.access('sxn.txt', os.X_OK)

# listdir(path)
# 返回当前目录下所有文件组成的列表
print os.listdir('./')

# rename(old, new)
# 修改文件或目录名
os.rename('sxn.txt', 'hys.txt')

# remove(path) 
# 删除文件
os.remove('hys.txt')

# mkdir(path[,mode])
# 创建目录
os.mkdir('sxn')

# makedirs(path[,mode])
# 创建多级目录
os.makedirs('hys/hys1/hys2')

# removedirs(path)
# 删除多级目录
os.removedirs('hys/hys1/hys2')

# rmdir(path)
# 删除目录（必须是空目录）
os.rmdir('sxn')


# os.path
# exists(path)
# 当前路径是否存在
print os.path.exists('./code.txt')

# isdir(s)
# 是否是一个目录
print os.path.isdir('./')
print os.path.isdir('code.txt')

# isfile(path)
# 是否是一个文件
print os.path.isfile('code.txt')

# getsize(filename)
# 返回文件大小
print os.path.getsize('code.txt')

# dirname(p)
# 返回路径目录
print os.path.dirname('./code.txt')

# basename(p)
# 返回路径文件名
print os.path.basename('./code.txt')
