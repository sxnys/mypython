# coding: utf-8

# // 定位根节点
# / 往下层寻找
# 提取文本内容: /text()
# 提取属性内容: /@xxx

from lxml import etree

html = '''
<!DOCTYPE html>
<html>
<head lang="en">
	<meta charset="UTF-8">
	<title>测试-常规用法</title>
</head>
<body>
<div id="content">
	<ul id="useful">
		<li>这是第一条信息</li>
		<li>这是第二条信息</li>
		<li>这是第三条信息</li>
	</ul>
	<ul id="useless">
		<li>不需要的信息1</li>
		<li>不需要的信息2</li>
		<li>不需要的信息3</li>
	</ul>

	<div id="url">
		<a href="http://jikexueyuan.com">极客学院</a>
		<a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
	</div>
</div>

</body>
</html>
'''

selector = etree.HTML(html)

# 提取文本
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
	print each

# 提取属性
link = selector.xpath('//a/@href')
# 或者更加具体 
# //div[@id="url"]/a/@href
for each in link:
	print each

title = selector.xpath('//a/@title')
print title[0]


# 特殊用法
# 以相同的字符开头
# starts-with(@属性名称，属性字符相同部分)
html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
	<meta charset="UTF-8">
	<title>测试-以相同的字符开头</title>
</head>
<body>
	<div id="test-1">需要的内容1</div> 
	<div id="test-2">需要的内容2</div> 
	<div id="testfault">需要的内容3</div> 
</body>
</html>
'''

selector = etree.HTML(html1)
content = selector.xpath('//div[starts-with(@id, "test")]/text()')
for each in content:
	print each

# 标签套标签
# string(.)
html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
	<meta charset="UTF-8">
	<title>测试-标签套标签</title>
</head>
<body>
	<div id="test3">
		我左青龙，
		<span id="tiger">
			右白虎，
			<ul>上朱雀，
				<li>下玄武。</li>
			</ul>
			老牛在当中，
		</span>
		龙头在胸口。
	</div>
</body>
</html>
'''

selector = etree.HTML(html2)
content_1 = selector.xpath('//div[@id="test3"]/text()')
for each in content_1:
	print each

data = selector.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
content_2 = info.replace('\n', '').replace(' ', '').replace('\t', '')
print content_2