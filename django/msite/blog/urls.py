from django.urls import path, re_path   # path 不支持正则
from . import views

urlpatterns = [
    re_path(r'^$', views.blog_title, name='blog_name'),
    re_path(r'(?P<article_id>\d)/$', views.blog_article, name='blog_detail')
]
