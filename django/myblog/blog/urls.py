# coding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'), # 组名必须和响应函数中添加的参数名一致
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
]