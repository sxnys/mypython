#coding:utf-8

# 切片
# 切片是序列的通用操作，包括list，tuple，字符串等
# list[index1:index2]，包含的元素范围是[index1, index2)
# 若包含首元素，则可省略index1(0)，若包含末元素，也是如此
# 但是如果采用负数索引，包含末元素时只能省略index2
L = ['A', 'B', 'C', 'D', 0, 1, 2, 3, 4]
print L[0: 5]
print L[: 5]
print L[:]
print L[0: -4]
print L[-4:-1]
print L[-4:]
# 加步长，list[index1:index2:step]
# 步长不能为0，但是可以为负数，即从左到右提取元素，
# 且index1 > index2
print L[1:7:2]
print L[::2]
print L[7:1:-2]
print L[::-2]
# 切片更新
L[-4:] = [11, 12]
print L
L[-2:] = list('hys')
print L
del L[-3:]
print L

# 利用切片取出：
# 1. 前10个数
# 2. 3的倍数
# 3. 不大于50的5的倍数
# 4. 最后10个数
# 5. 最后10个5的倍数
L = range(1, 101)
print L[:10]
print L[2::3]
print L[4:50:5]
print L[-10:]
print L[4::5][-10:]   # 先取出所有5的倍数再取出其中最后10个

# 对字符串的切片操作
print 'ABCDEFG'[:3]
print 'ABCDEFG'[-3:]
print 'ABCDEFG'[::2]
print u'桑笑楠'[:2]

def firstCharUpper(s):		# 单词首字母大写函数
    return s[0:1].upper() + s[1:]
print firstCharUpper('hello')