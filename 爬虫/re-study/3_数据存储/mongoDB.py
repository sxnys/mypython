# coding: utf-8

from pymongo import MongoClient

client = MongoClient('localhost', 27017)	# 主机地址 + 端口号
db = client.test_db		# 连接数据库test_db，如果不存在则会创建
collection = db.student	# 选择该数据库下的集合，也就是table

student1 = {
	'name': 'xn',
	'gender': 'male',
	'age': '23',
	'school': 'njust',
}

student2 = {
	'name': 'ys',
	'gender': 'female',
	'age': '24',
	'school': 'nust',
}

# 存入数据库只需要存json数据，这里就是字典
collection.insert_one(student1)
collection.insert_one(student2)
# 或者存入多个
collection.insert_many([student1, student2])