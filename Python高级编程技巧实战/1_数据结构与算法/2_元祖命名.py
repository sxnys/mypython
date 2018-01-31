# coding: utf-8

''' 为元祖中的每个元素命名提高可读性
1、定义类似于其他语言的枚举类型，即一系列数值常量
2、使用标准库collections.namedtuple代替内置的tuple
	namedtuple(TupleClassName, ListOfProperty)
'''

# 枚举类型
NAME, AGE, SEX, EMAIL = range(4)
Student = ('Sxn', 23, 'male', '1119112647@qq.com')
print(Student[NAME], Student[AGE], Student[SEX], Student[EMAIL])

# namedtuple
from collections import namedtuple
Stu = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Stu('Sxn', 23, 'male', '1119112647@qq.com')
# OR.  s = Student(name='Sxn', age=23, sex='male', email='1119112647@qq.com')
print(s)
print(s.name, s.age, s.sex, s.email)
# OR.  s[0], s[1], s[2], s[3]