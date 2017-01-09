#coding=utf-8
from django import forms
import userCenter
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User
from models import *
from shopping.models import *
from django import forms
from django.contrib import auth


def login_register_split(request,get,post):
    if request.method == 'GET':
        return get(request)
    elif request.method == 'POST':
        return post(request)
    else:
        raise Http404
#注册页面

def register(request):
    return render(request,'userCenter/register.html')


def cart(request):
    cartAll = userCenter.models.cart.objects.all()
    context = {'cartAll':cartAll}
    return render(request,'userCenter/cart.html', context)


def cartdel(request):
    cart_good_id = request.GET.get('cart_good_id')
    userCenter.models.cart.objects.get(pk = cart_good_id).delete()
    return HttpResponse('ok')


def cartchange(request):
    num = request.GET.get('num')
    cart_good_id = request.GET.get('cart_good_id')
    good = userCenter.models.cart.objects.get(pk=cart_good_id)
    good.num = num
    good.save()
    return HttpResponse('ok')

#验证提交信息的正确性
class ttsxUser(forms.Form):
    name = forms.CharField(max_length=20,min_length=3)
    pwd = forms.CharField(max_length=20,min_length=6)
    email = forms.EmailField(max_length=30,min_length=3)
#注册用户
def createUser(request):
    form = ttsxUser(request.POST)
    isCreate = False
    if form.is_valid():
        info = form.cleaned_data
        try:
            #用户名已经存在抛异常
            user = User.objects.create_user(username=info['name'],password=info['pwd'],email=info['email'])
            user.save()
        except Exception,e:
            pass
        else:
            isCreate = True
    return JsonResponse({'register':isCreate})

#登陆页面
def login(request):
    return  render(request,'userCenter/login.html')

#用户登陆
from django.contrib.auth.models import User
def toLogin(request):
    username = request.POST.get('username', '')
    pwd = request.POST.get('pwd', '')
    user = auth.authenticate(username=username, password=pwd)
    isLogin = False
    if user is not None and user.is_active:
        auth.login(request,user)
        isLogin = True
    return  JsonResponse({'login':isLogin})
#退出登陆
def logout_view(request):
    auth.logout(request)
# 可以根据需求跳转到特定页面
    return HttpResponseRedirect("/userCenter/login/")

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




# def test(request):
#     if  request.user.is_authenticated():
#         user = request.user
#         return HttpResponse(user.password)
#     raise Http404

# from django.contrib.auth.decorators import login_required
# @login_required()
# def test_login(request):
#     '''利用装饰器判断登陆，如果没有登陆直接跳转至登陆页面，如果登陆成功会跳转至相应的页面'''
#     return HttpResponse('xxx')

