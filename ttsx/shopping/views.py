#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404,HttpResponseRedirect
from django.core.paginator import Paginator
from models import *
from userCenter.models import *
from django.contrib.auth.models import User
import random
from django.contrib import auth


def index(request):
    fruit = GoodsInfo.objects.all().filter(type='fruit')
    seafood = GoodsInfo.objects.all().filter(type='seafood')
    meat = GoodsInfo.objects.all().filter(type='meat')
    egg = GoodsInfo.objects.all().filter(type='egg')
    vegetables = GoodsInfo.objects.all().filter(type='vegetables')
    ice = GoodsInfo.objects.all().filter(type='ice')
    count = cart.objects.all().count()
    context = {'fruit':fruit[0:4], 'fruit1':fruit[5:8], 'seafood':seafood[0:4], 'seafood1':seafood[5:8], 'meat':meat[0:4], 'meat1':meat[5:8], 'egg':egg[0:4], 'egg1':egg[5:8], 'vegetables':vegetables[0:4], 'vegetables1':vegetables[5:8], 'ice':ice[0:4], 'ice1':ice[0:4], 'count':count}
    return render(request, 'shopping/index.html', context)


def list(request, kind, name, attr, pIndex):
    goods = GoodsInfo.objects.all().filter(type=kind)
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
    context = {'goods': goods_now, 'name':name, 'newgoods':newgoods[-2:], 'kind':kind, 'attr':attr, 'pIndex':pIndex, 'num':page_num, 'pNext':pNext, 'pPrev':pPrev, 'count':count}
    return render(request, 'shopping/list.html', context)


def search(request, attr, pIndex):
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


#详情页
def detail(request,id):
    id=int(id)
    goods_detail = GoodsInfo.objects.get(pk=id)
    context = {'goods_detail':goods_detail}
    return render(request,'shopping/detail.html',context)


def addgoods(request):
    user = User.objects.get(id=1)
    goodsid = request.GET.get('goodsid')
    goods_info = GoodsInfo.objects.get(id=goodsid)
    try:
        cart_good = cart.objects.get(goods_info=goodsid)
        num = cart_good.num
        cart_good.num = num+1
        cart_good.save()
    except Exception,e:
        cart.objects.create(num=1, user=user, goods_info=goods_info)
    return HttpResponse('ok')



def buy_now(request):
    if request.user.is_authenticated():
        goods_id = request.GET["goods_id"]
        goods_count = request.GET["goods_count"]
        print(goods_id)
        id=int(goods_id)
        user = request.user
        goods_order=GoodsInfo.objects.get(pk=id)
        money=goods_order.price*goods_count
        context ={'user':user,'goods_order':goods_order,
                  'money':money
                  }
        return render(request,'shopping/place_order.html',context)
    else:
        return HttpResponseRedirect('/userCenter/login')


