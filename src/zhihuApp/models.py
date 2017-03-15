from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=13)
	password = models.CharField(max_length=50)
	head =models.FileField(upload_to='./upload/')
	
	def __unicode__(self):
		return self.name

class Question(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=300)
	release_date = models.DateField()
	
	def __unicode__(self):
		return self.title

class Answers(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	content = models.CharField(max_length=300)
	release_date = models.DateField()
	