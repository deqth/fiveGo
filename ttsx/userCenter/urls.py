#coding=utf-8
from django.conf.urls import url
from userCenter import views
urlpatterns = [
    url(r'^cart/$', views.cart),
    url(r'^login/$', views.login_register_split, {'get': views.login, 'post': views.toLogin}, name='login'),
    url(r'^register/$', views.login_register_split, {'get': views.register, 'post': views.createUser}, name='register'),
    url(r'^user_center_info/$', views.userCenterInfo),
    url(r'^user_center_site/$', views.userCenterSite),
    url(r'^user_center_order/$', views.userCenterOrder),
    url(r'^user_center_site/useraddressupdate$', views.updatehandler),
    # url(r'^test/$', views.test_login),
 ]

