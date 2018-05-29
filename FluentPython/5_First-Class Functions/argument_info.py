"""
函数对象有一个__defaults__属性，是保存定位参数和关键字参数默认值的元组，
仅限关键字参数默认值在__kwdefaults__属性中，参数的名称在__code__属性中（__code__本身是对象引用，有很多属性）

使用inspect模块提取函数签名更加方便，很多框架和IDE都是以此来验证代码的
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


print(
	tag.__defaults__,
	tag.__code__, 
	tag.__code__.co_varnames, 
	tag.__code__.co_argcount,
	sep = '\n'
	)
print()

from inspect import signature
sig = signature(tag)
print(sig)
for name, param in sig.parameters.items():  # name 和 param.name是一样的
	print(param.kind, ':', name, '=', param.default)
print()
# signature函数返回的是inspect.Signature对象，它的parameters属性是一个有序映射，这里即sig.parameters，
# 是inspect.Parameter对象，它有name、default、kind，还有annotation属性

# inspect.Signature对象有一个bind方法，可以把任意个参数绑定到签名的形参上
my_tag = {
		'name': 'img',
		'title': 'Sunset',
		'src': 'sunset.jpg',
		'cls': 'framed'
	}
bound_args = sig.bind(**my_tag)
print(bound_args)
for name, value in bound_args.arguments.items():  # 一个OrderedDict对象
	print(name, '=', value)
