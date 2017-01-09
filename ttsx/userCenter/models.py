#coding=utf-8
from django.db import models
from shopping.models import *
from django.contrib.auth.models import User



class cart(models.Model):
    num = models.IntegerField()
    user = models.ForeignKey(User)
    goods_info = models.ForeignKey(GoodsInfo)
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
class OrderInfo(models.Model):
    user = models.ForeignKey(User)
    state = models.BooleanField()
    total = models.DecimalField(max_digits=5,decimal_places=2)
    class Meta:
        db_table = 'OrderInfo'
class OrderDetailInfo(models.Model):
    bpub_date = models.DateTimeField()
    ordernum = models.CharField(max_length=20)
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey(GoodsInfo)
    goods_price = models.DecimalField(max_digits=5,decimal_places=2)
    count = models.DecimalField(max_digits=5,decimal_places=2)
    class Meta:
        db_table = 'OrderDetailInfo'

