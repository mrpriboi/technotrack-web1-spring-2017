from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from blog.models import Post

# Create your models here.

class Comment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.ForeignKey(Post,related_name='comments')
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.content