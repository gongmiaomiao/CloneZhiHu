from django.contrib import admin
from zhihuApp.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'password', 'head']

admin.site.register(User, UserAdmin)