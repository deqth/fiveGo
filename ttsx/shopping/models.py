#coding=utf-8
from django.db import models

class GoodsInfo(models.Model):
    title = models.CharField(max_length=20,verbose_name='商品信息')    #商品名字
    type = models.CharField(max_length=20,verbose_name='商品类型')     #商品类型
    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='商品价格')            #商品价格
    unit = models.CharField(max_length=20,verbose_name='商品单位')     #商品单位
    smallImg = models.ImageField(verbose_name='商品小图')#商品图片
    info = models.CharField(max_length=200,verbose_name='商品简介')   #商品简介
    info_detail = models.TextField(max_length=3000,verbose_name='商品详情') #商品详情
    bigImg = models.ImageField(verbose_name='商品大图')#商品图片
    inventoryNum = models.IntegerField(verbose_name='库存量')
    cliNum = models.IntegerField(verbose_name='点击量')#点击量
    class Meta():
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    #后台admin站点添加数据显示名字而不是对象
    def __str__(self):
        #__unicode__
        return self.title.encode('utf-8')