#coding=utf-8
from django.db import models
from shopping.models import *

class user(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=30)
    email = models.EmailField()
    class Meta:
        db_table = 'user'
class cart(models.Model):
    num = models.IntegerField()
    user = models.ForeignKey(user)
    goods_info = models.ForeignKey(GoodsInfo)
    class Meta:
        db_table = 'cart'
class address_info(models.Model):
    tel = models.CharField(max_length=15)
    email = models.EmailField()
    zipcode = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    user = models.ForeignKey(user)
    isDelete = models.BooleanField(default=0)
    class Meta:
        db_table = 'address_info'
class OrderInfo(models.Model):
    user = models.ForeignKey(user)
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
