import sys
import re

WORD_RE = re.compile(r'\w+')


def getWords():
    index = {}
    with open(sys.argv[1]) as fp:
        for line_no, line in enumerate(fp, 1):  # enumerate第二个参数是设置初始标号
            for match in WORD_RE.finditer(line):
                word = match.group()
                colum_no = match.start() + 1
                location = (line_no, colum_no)

                # 查询了三次
                # occurrences = index.get(word, [])
                # occurrences.append(location)
                # index[word] = occurrences

                # 用setdefault只需要查询一次
                # 关于为什么直接在后面append就可以改变它的值，首先setdefault都会返回一个值，它是一个列表，
                # 而列表的append方法是一个就地方法，直接把原来的值改变了，类似于sort方法，而内置的sorted方法则会创建一个新的对象
                index.setdefault(word, []).append(location)
                # 效果等同于，至少两次查询
                # if word not in index:
                # 	index[word] = []
                # index[word].append(location)

    # index是字典，对它排序实际上是对index的key进行排序，更本质的将就是对index的迭代对象排序（__iter__），实际上就是它的键值
    for word in sorted(index, key=str.upper):
        print(word, index[word])


if __name__ == '__main__':
    getWords()
