"""
函数注解（annotation）: 用于为函数声明中的参数和返回值附加元数据，仅仅是存储在函数的__annotations__属性里，此外不做任何处理
各参数可以在 : 后添加注解表达式，参数有默认值注解则放在参数名和 = 之间；
返回值的注解在 ) 和函数声明结尾的 : 之间添加 ->和一个表达式；
注解可以是类（str, int, ...），或者是一个字符串；
函数的__annotations__属性的值是一个字典，其中返回值注解对应的键是'return'

inspect.signature函数返回的对象有一个 return_annotation属性，它的parameters属性中每一个Parameter对象也有annotation属性
"""

from inspect import signature

def func(text:str, max_len:'int > 0'=80) -> str: pass

print(func.__annotations__)

sig = signature(func)
print(sig.return_annotation)
for param in sig.parameters.values():
	note = repr(param.annotation).ljust(13)
	print(note, ':', param.name, '=', param.default)
	