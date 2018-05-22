"""
python3的str对象获取的对象是unicode字符，就是python2中的unicode对象
码位：字符的标识，0~1114111十进制数字
编码：码位转换为字节序列
解码：字节序列转换为码位
bytes字面量以b开头
"""

s = 'café'
print(len(s))
b = s.encode('utf8')
print(b, len(b), b.decode('utf8'), sep=' | ')



"""
bytes和bytearray对象的各个元素是0~255的整数，但切片是同一类型的二进制序列
"""
cafe = bytes('café', encoding='utf8')
print(cafe, cafe[0], cafe[:1], sep=' | ')
cafe_arr = bytearray(cafe)
print(cafe_arr, cafe_arr[-1:], sep=' | ')


"""
二进制序列的字面量表示可能有三种方式显示：
1、可打印的ACSII范围内的字节，使用ASCII字符本身
2、使用转义字符的制表符、换行符、回车符、\
3、其他字节的值，使用十六进制转义序列
"""