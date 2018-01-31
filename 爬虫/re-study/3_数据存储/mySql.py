# coding: utf-8

import MySQLdb

# 建立连接
conn = MySQLdb.connect(host='localhost', user='root', passwd='941205', db='jwc')

# 创建游标
cur = conn.cursor()

# 执行纯SQL语句
a = 9
b = 8
c = 7
d = 6
cur.execute('insert into time values (%s, %s, %s, %s)', (a, b, c, d))

# 关闭游标，提交事务，关闭连接
cur.close()
conn.commit()
conn.close()