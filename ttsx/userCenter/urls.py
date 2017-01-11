#coding=utf-8
from django.conf.urls import url
from userCenter import views
urlpatterns = [
    url(r'^cart/$',views.cart, name='cart'),
    url(r'^cartdel$', views.cartdel, name='cartdel'),
    url(r'^cartchange$', views.cartchange, name='cartchange'),
    url(r'^isselect$', views.isselect, name='isselect'),
    url(r'^allselect$', views.allselect, name='allselect'),
    url(r'^login/$', views.login_register_split, {'get': views.login, 'post': views.toLogin}, name='login'),
    url(r'^logout/$', views.logout_view),
    url(r'^register/$', views.login_register_split, {'get': views.register, 'post': views.createUser}, name='register'),
    url(r'^userCenterInfo/$', views.userCenterInfo),
    url(r'^userCenterSite/$', views.userCenterSite),
    url(r'^userCenterOrder([0-9]*)/$', views.userCenterOrder),
    url(r'^userCenterSite/userAddressUpdate$', views.updatehandler),
]

