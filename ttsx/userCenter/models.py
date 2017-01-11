#coding=utf-8
from shopping.models import *
from django.contrib.auth.models import User


class cart(models.Model):
    num = models.IntegerField(verbose_name='数量')
    user = models.ForeignKey(User)
    goods_info = models.ForeignKey(GoodsInfo)
    isselect = models.BooleanField()
    class Meta:
        db_table = 'cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
class address_info(models.Model):
    receiver = models.CharField(max_length=15,verbose_name='收件人')
    tel = models.CharField(max_length=15,verbose_name='电话号码')
    email = models.EmailField(verbose_name='邮箱')
    zipcode = models.CharField(max_length=10,verbose_name='邮编')
    address = models.CharField(max_length=50,verbose_name='地址')
    user = models.ForeignKey(User)
    isDelete = models.BooleanField(default=0)
    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name
        db_table = 'address_info'
    # 后台admin站点添加数据显示名字而不是对象
    def __str__(self):
        # __unicode__
        return self.user.username.encode('utf-8')

class OrderInfo(models.Model):
    user = models.ForeignKey(User)
    state = models.BooleanField(verbose_name='支付状态')
    total = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='支付金额')
    ordernum = models.CharField(max_length=30,verbose_name='订单号')
    bpub_date = models.DateTimeField(verbose_name='订单日期',auto_now_add=True)
    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        db_table = 'OrderInfo'
    def __str__(self):
        return str(self.total)

class OrderDetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey(GoodsInfo)
    goods_price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='商品价格')
    count = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='商品数量')
    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
        db_table = 'OrderDetailInfo'

