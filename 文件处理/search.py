# coding: utf-8
import os

print u'请输入您要在哪个盘符查找文件（直接输入盘符字母）：'
a = raw_input()
print u'请输入您要查找的文件名或关键字：'
file = raw_input()

path = a.upper() + ':\\'
res = list()

def search(direction, fname, path):
	try:
		os.chdir(direction)
		if ':' not in direction:
			path = path + direction + '\\'
		files = os.listdir('.')
		for file in files:
			if os.path.isdir(file):
				search(file, fname, path)
				os.chdir('..')
			elif fname.upper() in file.upper():
				res.append(path + file)
	except WindowsError, e:
		print u'拒绝访问' + path + direction

search(a + ':', file, path)
if len(res) == 0:
	print u'没有找到您要的文件'
else:
	print u'您要查找的文件可能如下：'
	for r in res:
		print r
