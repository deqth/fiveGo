#coding=utf-8
from django.contrib import admin
from models import *

#2017/1/05注册admin站点
admin.site.register(cart)
admin.site.register(address_info)
admin.site.register(OrderInfo)
admin.site.register(OrderDetailInfo)
admin.site.register(GoodsInfo)

