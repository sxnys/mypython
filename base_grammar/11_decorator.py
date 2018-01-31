# coding:utf-8

# Python的 decorator 本质上就是一个高阶函数，它接收一个函数
# 作为参数，然后，返回一个新函数
# 使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 
# f = decorate(f) 这样的代码

# @log
# 不带参数
def log(f):
	def fn(x):
		print 'call', f.__name__ + '()...'
		return f(x)
	return fn
@log
def fac(n):
	return reduce(lambda x, y: x * y, range(1, n + 1))
print fac(10)

# 带参数
def log(prefix):
	def log_decrotor(f):
		def wrapper(*args, **kw):
			print '[%s] %s()..' %(prefix, f.__name__)
			return f(*args, **kw)
		return wrapper
	return log_decrotor
@log('DEBUG')
def test():
	pass
print test()




# @performance
import time
# 不带参数
def performance(f):
	# 打印出函数调用时刻
    def print_time(*args, **kw):	# 接受任意个数的参数
        print 'call '+f.__name__+'() in '+time.strftime('%Y-%m-%d',time.localtime(time.time()))
        return f(*args,**kw)
    return print_time
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

# 带参数
def performance(unit):
	def per(f):
		def wrapper(*args, **kw):
			t1 = time.time()
			r = f(*args, **kw)
			t2 = time.time()
			t = (t2 - t1) if unit == 's' else (t2 - t1) * 1000
			print 'call %s() in %f%s' % (f.__name__, t, unit) 
			return r
		return wrapper
	return per

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)




# 完善
# 使用了装饰器后，函数名会改变，也包括其他的一些属性
def log(f):
	def wrapper(*args, **kw):
		print 'name is "%s" before using decorator!' % (f.__name__)
		return f(*args, **kw)
	return wrapper
@log
def pow(n):
	return map(lambda x: x * x, range(1, 1 + n))
print 'name is "%s" after using decorator!' % (pow.__name__)
print pow(10)

# Python内置的functools可以用来自动化完成“复制”的任务
import functools

def log(f):
	@functools.wraps(f) # 带参数的也是把它放在wapper之前
	def wrapper(*args, **kw):
		print 'name is "%s" before using decorator!' % (f.__name__)
		return f(*args, **kw)
	return wrapper
@log
def pow(n):
	return map(lambda x: x * x, range(1, 1 + n))
print 'name is "%s" after using decorator!' % (pow.__name__)
print pow(10)