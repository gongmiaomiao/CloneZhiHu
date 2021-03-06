"""CloneZhiHu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from zhihuApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
#     url(r'^home/', views.home, name= 'home'),
    url(r'^$',  views.signin, name= 'signin'),
    url(r'^people/(?P<user_id>\d+.*)', views.people,name='people'), 
    url(r'^asks/(?P<user_id>\d+.*)', views.asks,name='asks'), 
    url(r'^answers/(?P<user_id>\d+.*)', views.answers,name='answers'),
    url(r'^collections/(?P<user_id>\d+.*)', views.collections, name='collections'), 
    url(r'^asksdetail/(?P<user_id>\d+.*)/(?P<question_id>\d+.*)', views.asksdetail,name='asksdetail'), 
]
