#coding=utf-8
from django.conf.urls import url
from userCenter import views
urlpatterns = [
   url(r'^register/$', views.register),
   url(r'^register/create/$', views.createUser),
   url(r'^user_center_info/$', views.userCenterInfo),
   url(r'^user_center_site/$', views.userCenterSite),
   url(r'^user_center_order/$', views.userCenterOrder),
   url(r'^user_center_site/useraddressupdate$', views.updatehandler),

 ]