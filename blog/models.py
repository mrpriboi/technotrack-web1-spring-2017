from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

class Blog(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	caption = models.CharField(max_length=50) 
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	category = models.ManyToManyField(Category)

	def __unicode__(self):
		return self.caption

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	content = models.TextField()
	blog = models.ForeignKey(Blog)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=50, default="NameOfPost")

	def __unicode__(self):
		return self.title

class Like(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	created_at = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)