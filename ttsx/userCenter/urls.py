#coding=utf-8
from django.conf.urls import url
from userCenter import views
urlpatterns = [
   url(r'^login/$', views.login_split,{'get':views.login,'post':views.toLogin},name='login'),
   url(r'^register/$', views.register_split,{'get':views.register,'post':views.createUser},name='register'),
 ]