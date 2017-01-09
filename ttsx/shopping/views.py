#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from django.core.paginator import Paginator
from models import *
from userCenter.models import *
from django.contrib.auth.models import User
import random
from django.contrib import auth


def index(request):
    fruit = GoodsInfo.objects.all().filter(type='新鲜水果')
    seafood = GoodsInfo.objects.all().filter(type='海鲜水产')
    meat = GoodsInfo.objects.all().filter(type='猪牛羊肉')
    egg = GoodsInfo.objects.all().filter(type='禽类蛋品')
    vegetables = GoodsInfo.objects.all().filter(type='新鲜蔬菜')
    ice = GoodsInfo.objects.all().filter(type='速冻食品')
    count = cart.objects.all().count()
    context = {'fruit':fruit[0:4], 'fruit1':fruit[5:8], 'seafood':seafood[0:4], 'seafood1':seafood[5:8], 'meat':meat[0:4], 'meat1':meat[5:8], 'egg':egg[0:4], 'egg1':egg[5:8], 'vegetables':vegetables[0:4], 'vegetables1':vegetables[5:8], 'ice':ice[0:4], 'ice1':ice[0:4], 'count':count}
    return render(request, 'shopping/index.html', context)


def list(request, type, attr, pIndex):
    if request.method == 'POST':
        return addgoods(request)
    goods = GoodsInfo.objects.all().filter(type=type)
    goods_order = goods.order_by(attr)
    count = cart.objects.all().count()
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


def search(request, attr, pIndex):
    if request.method == 'POST':
        return addgoods(request)
    search_good = request.GET['search_good']
    results = GoodsInfo.objects.filter(info__contains=search_good)
    count = cart.objects.all().count()
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


def addgoods(request):
    user = User.objects.get(id=1)
    goodsid = request.POST.get('goodsid')
    goodsnum = long(request.POST.get('goodsnum'))
    goods_info = GoodsInfo.objects.get(id=goodsid)
    try:
        cart_good = cart.objects.get(goods_info=goodsid)
        num = cart_good.num
        cart_good.num = num+goodsnum
        cart_good.save()
    except Exception,e:
        cart.objects.create(num=goodsnum, user=user, goods_info=goods_info)
    count = cart.objects.all().count()
    return JsonResponse({'count': count})


def detail(request, type, goods_id):
    if request.method == 'POST':
        return addgoods(request)
    allgoods = GoodsInfo.objects.all().filter(type=type)
    count = cart.objects.all().count()
    newgoods = [temp for temp in allgoods]
    goods = GoodsInfo.objects.get(id=goods_id)
    context = {'type':type, 'goods':goods, 'newgoods':newgoods[-2:], 'count':count}
    return render(request, 'shopping/detail.html', context)
