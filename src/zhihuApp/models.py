from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=13)
	password = models.CharField(max_length=50)
	head =models.FileField(upload_to='./zhihuApp/static/upload/')
	
	def __unicode__(self):
		return self.name