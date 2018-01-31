# coding: utf-8

'''
修改'yyyy-mm-dd' => 'mm/dd/yyyy'

使用正则表达式的re.sub()方法做字符串替换，利用正则表达式的捕获组，
捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
'''

log = '''2017-04-19 23:06:23 sbafjhdbfjadbfjkbjkdasfbksnakf
2017-04-20 19:06:23 sbafjhdbfjadbfjkbjkdasfbksnakf\n'''

print log

import re

# 捕获分组
print re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
# 分组别名
print re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)
