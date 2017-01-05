#coding=utf-8
from django.conf.urls import url
from userCenter import views
from userCenter import *
urlpatterns = [
    url(r'^register/$', views.register),
    # url(r'^register/create/$', views.createUser),
    url(r'^cart/$',views.cart),

 ]