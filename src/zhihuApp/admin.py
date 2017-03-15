from django.contrib import admin
from zhihuApp.models import User,Question, Answers

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'password', 'head']

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'content', 'release_date']

class AnswersAdmin(admin.ModelAdmin):
	list_display = ['question', 'user', 'content', 'release_date']
	
admin.site.register(User, UserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answers, AnswersAdmin)