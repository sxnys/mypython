# coding:utf-8

f = open('code.txt', 'w')
# f.write(u'胡云裳') 报错

a = unicode.encode(u'胡云裳', 'utf-8')
print a
f.write(a)
f.close()


# 创建utf-8文件
import codecs
f = codecs.open('code1.txt', 'w', 'utf-8')
print f.encoding
f.write(u'胡云裳')
f.close()