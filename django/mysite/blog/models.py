# coding: utf-8

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 30, default = 'Title')
	content = models.TextField(null = True)

	# 在admin管理页面中显示的名称，不加的话就是默认的'Article object'
	def __str__(self):
		return self.title