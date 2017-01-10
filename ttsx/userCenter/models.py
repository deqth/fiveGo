#coding=utf-8
from django.db import models
from shopping.models import *
from django.contrib.auth.models import User



class cart(models.Model):
    num = models.IntegerField()
    user = models.ForeignKey(User)
    goods_info = models.ForeignKey(GoodsInfo)
    isselect = models.BooleanField()
    class Meta:
        db_table = 'cart'
class address_info(models.Model):
    receiver = models.CharField(max_length=15)
    tel = models.CharField(max_length=15)
    email = models.EmailField()
    zipcode = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    isDelete = models.BooleanField(default=0)
    receiver = models.CharField(max_length=15)
    class Meta:
        db_table = 'address_info'
    # 后台admin站点添加数据显示名字而不是对象
    def __str__(self):
        # __unicode__
        return self.user.username.encode('utf-8')

class OrderInfo(models.Model):
    user = models.ForeignKey(User)
    state = models.BooleanField()
    total = models.DecimalField(max_digits=5,decimal_places=2)
    ordernum = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    class Meta:
        db_table = 'OrderInfo'
    def __str__(self):
        return str(self.total)

class OrderDetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey(GoodsInfo)
    goods_price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.DecimalField(max_digits=5,decimal_places=2)
    class Meta:
        db_table = 'OrderDetailInfo'

