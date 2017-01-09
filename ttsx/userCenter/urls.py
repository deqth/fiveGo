#coding=utf-8
from django.conf.urls import url
from userCenter import views
from userCenter import *
urlpatterns = [
    url(r'^cart/$',views.cart, name='cart'),
    url(r'^login/$', views.login_register_split,{'get':views.login,'post':views.toLogin},name='login'),
    url(r'^register/$', views.login_register_split,{'get':views.register,'post':views.createUser},name='register'),
    url(r'^cartdel$', views.cartdel, name='cartdel'),
    url(r'^cartchange$', views.cartchange, name='cartchange'),
 ]
