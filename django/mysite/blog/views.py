# coding: utf-8

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from . import models	# 导入数据模型

# Create your views here.

def hello(request):
	return HttpResponse('<html>hello world</html>')

def index(request):
	t = loader.get_template('blog/index.html')
	html = t.render(None)
	return HttpResponse(html)
	# 或者 return render(request, 'blog/index.html')

def article(request):
	art = models.Article.objects.get(pk = 1)
	return render(request, 'blog/article.html', {'article': art})