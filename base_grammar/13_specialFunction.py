# coding:utf-8

# 特殊方法
# 定义在class中，不需要直接调用，某些函数或操作符会调用对应的特殊方法
# 只需要编写用到的特殊方法，有关联的特殊方法都必须实现
# 类似于C++里面的重载
# 下面只是一些

# __str__ , __repr__ 把一个类的实例变成 str
# __str__()用于显示给用户，而__repr__()用于显示给开发人员
class Person(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
	def __str__(self):
		return '(Person: %s, %s)' % (self.name, self.gender)
	__repr__ = __str__
p = Person('sxn', 'male')
print p


# __cmp__
class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def __str__(self):
		return '(%s, %s)' % (self.name, self.score)
	__repr__ = __str__

	def __cmp__(self, s):
		if self.name < s.name:
			return -1
		elif self.name > s.name:
			return 1
		else:
			return 0
# 如果list不仅仅包含 Student 类，则 __cmp__ 可能会报错
L = [Student('sxn', '100'), Student('hys', '99'), 
	Student('lcx', '59')]
print sorted(L)


# __len__
# 要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，
# 它返回元素的个数
class Student(object):
	def __init__(self, *args):
		self.names = args
	def __len__(self):
		return len(self.names)
ss = Student('Bob', 'Alice', 'Tim')
print len(ss)


# 数学运算
# 类似于运算符重载
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)
    
    def __str__(self):
        GCD = gcd(self.p, self.q)
        return '%s/%s' % (str(self.p / GCD), str(self.q / GCD))

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2



# 类型转换
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p * 1.0 / self.q

print float(Rational(7, 2))
print float(Rational(1, 3))


# @property
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
s = Student('Bob', 59)
s.score = 60
print s.score
s.score = 1000
print s.score


# __slots__
# Python是动态语言，任何实例在运行期都可以动态地添加属性
# 如果要限制添加的属性，就可以利用__slots__来实现
# __slots__是指一个类允许的属性列表
class Student(object):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score
s = Student('Bob', 'male', 90)
s.name = 'Tim'
s.score = 99
# s.grade = 'A'  不允许


# __call__
# 所有的函数都是可调用对象
# >>> f = abs
# >>> f.__name__
# 'abs'
# >>> f(-123)
# 123
# 一个类实例也可以变成一个可调用对象，只需要实现方法__call__()
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend
p = Person('Bob', 'male')
p('Tim')


class Fib(object):
    def __init__(self):
        self.fib = [0, 1]
    
    def __call__(self, num):
        i = 0
        j = 1
        for k in range(2, num):
            self.fib.append(self.fib[i] + self.fib[j])
            i += 1
            j += 1
        return self.fib
f = Fib()
print f(10)