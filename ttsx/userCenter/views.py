#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from  models import *
from shopping.models import *

def register(request):
    return render(request,'userCenter/register.html')

def createUser(request):
    user = User.objects.create_user(username=request.POST['name'],password=request.POST['pwd'],email=request.POST['email'])
    user.save()
    return HttpResponseRedirect('userCenter/login.html')

#用户信息
def userCenterInfo(request):
    #判断用户是否登陆
    puser = User.objects.get(pk=2)
    addr = address_info.objects.get(user=puser.pk)
    context = {'user':puser,'addr':addr}
    return  render(request,'userCenter/user_center_info.html',context)

#用户地址
def userCenterSite(request):
    puser = User.objects.get(pk=2)
    addr = address_info.objects.get(user=puser.pk)
    context = {'user': puser, 'addr': addr}
    return  render(request,'userCenter/user_center_site.html',context)


#用户全部订单
def userCenterOrder(request):
    #根据登陆用户id查处他的订单
    orders = OrderInfo.objects.filter(user=2)
    #print (orders.total)
    #根据订单号查询订单详情
    orderdet = OrderDetailInfo.objects.filter(order=1)
   # print (orderdet.ordernum)
    #根据订单详情查出对应商品
    goods = OrderDetailInfo.objects.filter(goods__id__in=[0,1,2,3])
    # print(goods.goods.title)
    context = {'orders':orders,'orderdet':orderdet,'goods':goods}
    return  render(request,'userCenter/user_center_order.html',context)

#修改地址数据
def updatehandler(request):

    uname = request.POST['uname']
    uaddress = request.POST['address']
    uzipcode = request.POST['zipcode']
    utelp = request.POST['tel']
    # context = {'uname':uname,'address':address,'zipcode':zipcode,'tel':tel}
    #存储数据到数据库
    temp=address_info.objects.filter(id=1)[0]
    temp.receiver=uname
    temp.address=uaddress
    temp.tel=utelp
    temp.zipcode=uzipcode
    temp.save()

    return redirect('/user_center_site')




