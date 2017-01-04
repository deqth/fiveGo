#coding=utf-8
from django.conf.urls import url
from userCenter import views
urlpatterns = [
   url(r'^register/$', views.register),
   url(r'^register/create/$', views.createUser),
 ]