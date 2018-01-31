from django.db import models

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 35, default = 'Title')
	content = models.TextField(null = True)
	# pub_time = models.DateTimeField(auto_now = True)
	pub_time = models.DateTimeField(null=True)

	def __unicode__(self):
		return  self.title