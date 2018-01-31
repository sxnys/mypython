# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.
# 博客主页面
def index(request):
	articles = models.Article.objects.all()
	return render(request, 'blog/index.html', {'articles': articles})

# 博客文章页面
def article_page(request, article_id):
	article = models.Article.objects.get(pk = article_id)
	return  render(request, 'blog/article_page.html', {'article': article})

# 博客撰写页面
def edit_page(request, article_id):
	if str(article_id) == '0':
		return render(request, 'blog/edit_page.html')
	article = models.Article.objects.get(pk = article_id)
	return render(request, 'blog/edit_page.html', {'article': article})


# 新建文章
def edit_action(request):
	# POST字典获取参数值，get方法第二个参数是设默认值，避免异常
	title = request.POST.get('title', 'TITLE')
	content = request.POST.get('content', 'CONTENT')
	article_id = request.POST.get('article_id', '0')

	# 新建文章
	if article_id == '0':
		models.Article.objects.create(title=title, content=content)

		articles = models.Article.objects.all()
		# return render(request, 'blog/index.html', {'articles': articles}) 这样写在提交表单之后不会跳转到index页面，这里只是渲染了它，实际的url还是在它post的目标url，所以刷新会重复提交表单
		return HttpResponseRedirect(reverse('blog:index'))	# 重定向
		# return HttpResponseRedirect('../../index/')   可以这样写，但是麻烦，且容易出错

	# 修改文章
	article = models.Article.objects.get(pk = article_id)
	article.title = title
	article.content = content
	article.save()
	return  render(request, 'blog/article_page.html', {'article': article})
	# return  HttpResponseRedirect(reverse('blog:article_page'))  有问题，因为url中有模板匹配的数字，先放着
