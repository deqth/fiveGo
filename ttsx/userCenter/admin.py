#coding=utf-8
from django.contrib import admin
from models import *

def make_published(modeladmin, request, queryset):
    queryset.update(state=1)

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('ordernum', 'total', 'state')
    search_fields = ('total', )
    list_filter = ('bpub_date',)
    actions = [make_published]
class address_infoAdmin(admin.ModelAdmin):
    exclude = ('isDelete',)


#2017/1/05注册admin站点
admin.site.register(cart)
admin.site.register(address_info,address_infoAdmin)
admin.site.register(OrderInfo,OrderInfoAdmin)
admin.site.register(OrderDetailInfo)
admin.site.register(GoodsInfo)

