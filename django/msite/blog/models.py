from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')     # 允许通过类User反向查询到BlogArticles, on_delete定位参数必选, 2.0版本之前是没有的
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:    # 规定了按照publish字段倒序显示
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
