#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from userCenter.models import *
from django.contrib.auth.models import User
import random
from django.contrib.auth.decorators import login_required
import time


# 起始页面，将数据按照type发送到前端
def index(request):
    fruit = GoodsInfo.objects.all().filter(type='新鲜水果')
    seafood = GoodsInfo.objects.all().filter(type='海鲜水产')
    meat = GoodsInfo.objects.all().filter(type='猪牛羊肉')
    egg = GoodsInfo.objects.all().filter(type='禽类蛋品')
    vegetables = GoodsInfo.objects.all().filter(type='新鲜蔬菜')
    ice = GoodsInfo.objects.all().filter(type='速冻食品')
    if request.user.is_authenticated():
        userId = request.user.id
        count = cart.objects.filter(user_id=userId).count()
    else:
        count = 0
    context = {'fruit':fruit[0:4], 'fruit1':fruit[5:8], 'seafood':seafood[0:4], 'seafood1':seafood[5:8], 'meat':meat[0:4], 'meat1':meat[5:8], 'egg':egg[0:4], 'egg1':egg[5:8], 'vegetables':vegetables[0:4], 'vegetables1':vegetables[5:8], 'ice':ice[0:4], 'ice1':ice[0:4], 'count':count}
    return render(request, 'shopping/index.html', context)


#列表页面，按照attr进行排序，新品为每种类型商品最后两个，并进行分页
def list(request, type, attr, pIndex):
    if request.method == 'POST':
        return addgoods(request)
    goods = GoodsInfo.objects.all().filter(type=type)
    if attr=='cliNum':
        goods_order = goods.order_by("-"+attr)
    else:
        goods_order = goods.order_by(attr)
    if request.user.is_authenticated():
        userId = request.user.id
        count = cart.objects.filter(user_id=userId).count()
    else:
        count = 0
    newgoods = [temp for temp in goods]
    p = Paginator(goods_order, 10)
    pIndex = int(pIndex)
    goods_now = p.page(pIndex)
    page_num = p.page_range
    pPrev = pIndex
    pNext = pIndex
    if goods_now.has_previous():
        pPrev = pIndex - 1
    if goods_now.has_next():
        pNext = pIndex + 1
    context = {'goods': goods_now, 'newgoods':newgoods[-2:], 'type':type, 'attr':attr, 'pIndex':pIndex, 'num':page_num, 'pNext':pNext, 'pPrev':pPrev, 'count':count}
    return render(request, 'shopping/list.html', context)


#搜索页面，get方法获取搜索关键字，将搜索到的商品分页显示
def search(request, attr, pIndex):
    if request.method == 'POST':
        return addgoods(request)
    search_good = request.GET['search_good']
    results = GoodsInfo.objects.filter(info__contains=search_good)
    if request.user.is_authenticated():
        userId = request.user.id
        count = cart.objects.filter(user_id=userId).count()
    else:
        count = 0
    results_order = results.order_by(attr)
    p = Paginator(results_order, 10)
    pIndex = int(pIndex)
    goods_now = p.page(pIndex)
    page_num = p.page_range
    pPrev = pIndex
    pNext = pIndex
    if goods_now.has_previous():
        pPrev = pIndex - 1
    if goods_now.has_next():
        pNext = pIndex + 1
    goods = GoodsInfo.objects.all()
    newgoods = [temp for temp in goods]
    newlist = []
    for i in range(0,2):
        newlist.append(newgoods[random.randint(0,len(newgoods)-1)])
    context = {'newgoods':newlist, 'results':goods_now, 'attr':attr, 'pIndex':pIndex, 'num':page_num, 'pNext':pNext, 'pPrev':pPrev, 'search_good':search_good, 'count':count}
    return render(request, 'shopping/search.html', context)


# 当点击购物车图表或者在详情页加入购入车时，将商品及数量信息加入购物车
@login_required()
def addgoods(request):
    user = request.user
    userId = request.user.id
    goodsid = request.POST.get('goodsid')
    goodsnum = long(request.POST.get('goodsnum'))
    goods_info = GoodsInfo.objects.get(id=goodsid)
    try:
        cart_good = cart.objects.get(goods_info=goodsid)
        num = cart_good.num
        cart_good.num = num+goodsnum
        cart_good.save()
    except Exception,e:
        cart.objects.create(num=goodsnum, user=user, goods_info=goods_info, isselect=1)
    count = cart.objects.filter(user_id=userId).count()
    return JsonResponse({'count': count})


# 商品详情页面，展示商品具体信息
def detail(request, type, goods_id):
    if request.method == 'POST':
        return addgoods(request)
    allgoods = GoodsInfo.objects.all().filter(type=type)
    if request.user.is_authenticated():
        userId = request.user.id
        count = cart.objects.filter(user_id=userId).count()
    else:
        count = 0
    newgoods = [temp for temp in allgoods]
    goods = GoodsInfo.objects.get(id=goods_id)
    #将用户最近浏览的商品加入session
    if request.user.is_authenticated():
        if request.session.get('recent_goods'):
            recent_goods = request.session['recent_goods']
            if len(recent_goods)<5:
                if goods_id not in recent_goods:
                    recent_goods.append(goods_id)
            else:
                recent_goods = recent_goods[-4:]
                if goods_id not in recent_goods:
                    recent_goods.append(goods_id)
            request.session['recent_goods']=recent_goods
        else:
            request.session['recent_goods']=[goods_id,]
    cliNum = goods.cliNum
    goods.cliNum = int(cliNum+1)
    goods.save()
    context = {'type':type, 'goods':goods, 'newgoods':newgoods[-2:], 'count':count}
    return render(request, 'shopping/detail.html', context)


# 定义订单页面商品类
class buy_goods:
    def __init__(self, goods_info, num, subtotal, index=1):
        self.goods_info = goods_info
        self.num = num
        self.subtotal = subtotal
        self.index = index


# 将从详情页面立即购买的商品和购物车里去结算时的商品信息传到订单页面
@login_required()
def buy_now(request):
    user = request.user
    userId = request.user.id
    puser = User.objects.get(pk=userId)
    addr = address_info.objects.filter(user=puser.pk)
    print (addr)
    if not addr:
        addr = ['']
    if request.GET.get("goodsid",None):
        goodsid = request.GET["goodsid"]
        goodsnum = request.GET["goodsnum"]
        goods_info = GoodsInfo.objects.get(pk=goodsid)
        price = goods_info.price
        subtotal = int(goodsnum)*price
        ordernum = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
        order = OrderInfo.objects.create(user=user, state=0 , total=subtotal, ordernum=ordernum)
        OrderDetailInfo.objects.create(order=order, goods=goods_info, goods_price=price, count=1)
        goods = buy_goods(goods_info, goodsnum, subtotal)
        print order.pk
        context ={'goods':[goods], 'addr':addr[0],'orderid':order.pk}
    else:
        goods_order = cart.objects.filter(isselect=1)
        goods = []
        index = 0
        total = 0
        ordernum = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
        for goods_cart in goods_order:
            goods_info = goods_cart.goods_info
            goodsnum = goods_cart.num
            price = goods_info.price
            subtotal = int(goodsnum)*price
            total +=subtotal
            goods_cart.delete()
            index += 1
            good = buy_goods(goods_info, goodsnum, subtotal, index)
            goods.append(good)
        order = OrderInfo.objects.create(user=user, state=0, total=total, ordernum=ordernum, bpub_date='2000-1-1')
        for goods_cart in goods_order:
            goods_info = goods_cart.goods_info
            goodsnum = goods_cart.num
            price = goods_info.price
            OrderDetailInfo.objects.create(order=order, goods=goods_info, goods_price=price, count=goodsnum)
        context = {'goods':goods,'addr':addr[0], 'orderid':order.pk}
    return render(request,'shopping/place_order.html', context)



