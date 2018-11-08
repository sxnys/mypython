"""
python极为灵活的参数处理机制
调用函数时使用*和**展开可迭代对象，映射到单个参数（*其实是元组拆包，而**可以理解为字典拆包，虽然没有这种说法），*和**在使用时只能有一次
def func(arg1, arg2=None, *args, arg=None, **kwargs): pass
arg1: 传统的定位参数 (potitional argument)
args2 : 关键字参数(keyword argument)，调用函数时提供的实参可以是不指明关键字的
*args : 未指定名称的参数（连续的）会被它捕获，存入元组
arg : 仅限关键字参数，调用函数时提供的实参必须是指明关键字，须放在前面有*的参数后面，即不管是定义时，还是调用时传参，关键字参数必须都是在定位参数之后，所以定义时**kwargs一定是在*args之后的
**kwargs : 未指定名称的关键字参数会被它捕获，存入字典

！！！ 不管是定义还是调用，所有的关键字参数一定是在定位参数（不包括 *参数）之后的 ！！！

"""

def tag(name, *content, cls=None, **attrs):
	""" 生成一个或多个HTML标签 """
	if cls is not None:
		attrs['class'] = cls
	if attrs:
		attrs_str = ''.join(' %s="%s"' % (attr, value) for attr, value in attrs.items())
	else:
		attrs_str = '' 
	if content:
		return '\n'.join('<%s%s>%s</%s>' % (name, attrs_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attrs_str)


if __name__ == '__main__':
	my_tag = {
		'name': 'img',
		'title': 'Sunset',
		'src': 'sunset.jpg',
		'cls': 'framed'
	}
	print(
		tag('br'),
		tag('p', 'hello'),
		tag('p', 'hello', 'world'),
		tag('p', 'hello', id=33),
		tag('p', 'hello', 'world', cls='sidebar'),
		tag(content='testing', name='img'),  # 定位参数也能作为关键字参数传入
		tag(**my_tag),   # 字典中所有元素作为关键字参数传入，同名键会绑定到对应的具名参数上，余下的被**attrs捕获
		sep='\n\n'
		)

	def f(a, *, b):  # *仅是用来指明b是仅限关键字参数，不一定要有默认值
		return a, b
	print(f(1, 2))   # 所以这种传参是错误的
