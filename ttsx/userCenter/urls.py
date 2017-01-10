#coding=utf-8
from django.conf.urls import url
from userCenter import views
urlpatterns = [
    url(r'^cart/$',views.cart, name='cart'),
    url(r'^cartdel$', views.cartdel, name='cartdel'),
    url(r'^cartchange$', views.cartchange, name='cartchange'),
    url(r'^login/$', views.login_register_split, {'get': views.login, 'post': views.toLogin}, name='login'),
    url(r'^register/$', views.login_register_split, {'get': views.register, 'post': views.createUser}, name='register'),
    url(r'^user_center_info/$', views.userCenterInfo),
    url(r'^user_center_site/$', views.userCenterSite),
    url(r'^user_center_order([0-9]*)/$', views.userCenterOrder),
    url(r'^user_center_site/useraddressupdate$', views.updatehandler),
    # url(r'^test/$', views.test_login),
]

