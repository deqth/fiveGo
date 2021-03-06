#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#首页
    url(r'^list/(\w+)/(\w+)/(\d*)$', views.list, name='list'),#列表页
    url(r'^search/(\w+)/(\d+)$', views.search, name='search'),#搜索页
    url(r'^detail/(\w+)/(\d+)$', views.detail, name='detail'),#详情页
    url(r'^addgoods/$', views.addgoods, name='addgoods'),
    url(r'^order/$', views.buy_now, name='order'),#立即购买
    url(r'^notpaid/$', views.notpaid, name='notpaid'),
]



