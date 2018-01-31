# coding:utf-8

import os

file_name = raw_input('Please name your key-file:\n');
os.makedirs(file_name)
os.chdir(file_name)

# 在同一文件夹内创建名为0~n-1这n个目录
def build(n):
	for i in range(n):
		os.makedirs(str(i))

# 递归创建树形密码文件夹
def dir(m, n):
	if m == 0:
		return
	L = os.listdir('.')
	if len(L) == 0:
		build(n)
	for i in range(n):
		os.chdir(str(i))
		dir(m-1, n)
		os.chdir('..')

n = raw_input('Please set your key-file\'s layer-number:\n')
dir(int(n), 10)
