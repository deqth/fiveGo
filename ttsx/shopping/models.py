#coding=utf-8
from django.db import models

class GoodsInfo(models.Model):
    title = models.CharField(max_length=20)    #商品名字
    type = models.CharField(max_length=20)     #商品类型
    price = models.DecimalField(max_digits=5,decimal_places=2)            #商品价格
    unit = models.CharField(max_length=20)     #商品单位
    smallImg = models.ImageField()#商品图片
    info = models.CharField(max_length=200)   #商品简介
    info_detail = models.CharField(max_length=3000) #商品详情
    bigImg = models.ImageField()#商品图片
    class Meta():
        db_table = 'goods'
