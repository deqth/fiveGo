#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^detail/(\d+)/', views.detail),#详情页
    url(r'^order/',views.buy_now),#立即购买
    url(r'^index/$', views.index, name='index'),
    url(r'^list/(\w+)/(\w+)/(\w+)/(\d*)$', views.list, name='list'),
    url(r'^search/(\w+)/(\d+)$', views.search, name='search'),
    url(r'^addgoods$', views.addgoods, name='addgoods'),

]



