#coding:utf-8

# 面向对象
# class 类名(父类名)
class Person(object):
	pass
sxn = Person()
hys = Person()
sxn.name = u'桑笑楠'
hys.name = u'胡云裳'
sxn.age = 21
hys.age = 21
L = [sxn, hys]
for i in range(len(L)):
	print L[i].name, L[i].age

# 初始化实例属性
# 在定义 Person 类时，可以为Person类添加一个特殊的
# __init__()方法，当创建实例时，__init__()方法被自动调用
# __init__() 方法的第一个参数必须是 self（也可以用别的名字，
# 但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别
class Person(object):
	def __init__(self, name, gender, birth):
		self.name = name
		self.gender = gender
		self.birth = birth
sxn = Person(u'桑笑楠', u'男', '1994.12.30')
hys = Person(u'胡云裳', u'女', '1994.12.05')
print sxn.name, sxn.gender, sxn.birth
print hys.name, hys.gender, hys.birth

# 接受任意关键字做参数
class Person(object): 
    def __init__(self, name, gender, birth, **kw): 
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__dict__.update(kw)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student') 
print xiaoming.name 
print xiaoming.job

# 访问限制
class Person(object):
	def __init__(self, name):
		self.name = name
		self._title = 'Mr'
		self.__job = 'Student'  # 不能被外部访
Bob = Person('Bob')
print Bob.name
print Bob._title
# print Bob.__job 无法被访问


# 类属性
# 实例属性每个实例各自拥有，互相独立，而类属性有且只有一份
# 类属性是直接绑定在类上的，所以，访问类属性不需要创建实例，就可以直接访问
# 对一个实例调用类的属性也是可以访问的，所有实例都可以访问到它所属的类的属性
# 由于Python是动态语言，类属性也是可以动态添加和修改的
# 因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了
class Person(object):
	address = 'Earth'
	def __init__(self, name):
		self.name = name
print Person.address
p1 = Person('sxn')
p2 = Person('hys')
print p1.address
print p2.address
Person.address = 'China'
print p1.address
print p2.address
p1.address = 'England' # 不改变类的属性值，当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问
print Person.address

class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
p1 = Person('Bob')
print Person.count
p2 = Person('Alice')
print Person.count
p3 = Person('Tim')
print Person.count


# 定义实例方法
# 它的第一个参数永远是 self，指向调用该方法的实例本身，
# 其他参数和一个普通函数是完全一样
class Person(object):
	def __init__(self, name):
		self.__name = name
	def get_name(self):
		return self.__name
p1 = Person('Bob')
print p1.get_name()  # self不需要显式传入


# 函数绑定到实例，方法也是属性
# types.MethodType()
import types
def f_get_name(self):
	return self.name
class Person(object):
	def __init__(self, name):
		self.name = name
p1 = Person('sxn')
p1.get_name = types.MethodType(f_get_name, p1, Person)
print p1.get_name()

# 定义类方法
# 通过标记一个 @classmethod，该方法将绑定到 Person 类上，
# 而非类的实例，类方法的第一个参数将传入类本身，通常将参数名命名为 cls
class Person(object):
	count = 0
	@classmethod
	def how_many(cls):
		return cls.count
	def __init__(self, name):
		self.name = name
		Person.count += 1
print Person.how_many()
p1 = Person('Bob')
print Person.how_many()



# 继承
# 函数super(子类名, self)将返回当前类继承的父类，
# 然后调用__init__()方法，注意self参数已在super()中传入，
# 在__init__()中将隐式传递，不需要写出（也不能写） 
class Person(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
class Student(Person):
	def __init__(self, name, gender, score):
		super(Student, self).__init__(name, gender)
		self.score = score
s1 = Student('sxn', 'male', '100')
print s1.name, s1.gender, s1.score
# isinstance()判断类型
p1 = Person('sxn', 'male')
print isinstance(p1, Person)
print isinstance(p1, Student)
print isinstance(s1, Person)
print isinstance(s1, Student)


# 多重继承
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a

class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'

class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'
d = D('d')


# 获取对象信息
# type()函数获取变量类型，返回一个Type对象
print type(123)
print type(d)
# dir()函数获取变量的所有属性
print dir(123)
print dir(d)
# getattr() , setattr()
print getattr(d, 'a')
setattr(d, 'a', 'D')
print d.a

class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        self.__dict__.update(kw)	# 提供任意额外的关键字参数
p = Person('Bob', 'Male', age = 18, course = 'Python')
print p.age
print p.course