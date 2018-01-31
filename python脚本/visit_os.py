# coding: utf-8

# 用户和电脑信息
import os
# print dir(os)
# print os.getlogin()  Not Windows
# print os.getuid()    Not Windows
print os.umask(511)   # 权限，返回旧值
print os.name   # 操作系统

# 进程信息
print os.getpid()   # 当前进程ID
# print os.getppid()	# 父进程ID
print os.getcwd()    # 当前目录
print len(os.environ)  # os.environ: 当前进程的所有环境变量的字典
# print os.environ['HOME']

# 管理其它程序