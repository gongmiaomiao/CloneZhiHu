from django.contrib import admin
from zhihuApp.models import User,Question

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'password', 'head']

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'content', 'release_date']
	
admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)