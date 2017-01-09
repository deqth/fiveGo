#coding=utf-8
from django.conf.urls import url
import views



urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^list/(\w+)/(\w+)/(\d*)$', views.list, name='list'),
    url(r'^search/(\w+)/(\d+)$', views.search, name='search'),
    url(r'^detail/(\w+)/(\d+)$', views.detail, name='detail')
]



