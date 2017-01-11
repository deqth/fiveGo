#coding=utf-8
import userCenter
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from models import *
from shopping.models import *
from django import forms
from django.contrib import auth
from django.core.paginator import *
from django.contrib.auth.decorators import login_required
from shopping.views import *
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

@login_required()
def cart(request):
    userId = request.user.id
    userCenter.models.cart.objects.filter(user_id=userId).update(isselect=1)
    cartAll = userCenter.models.cart.objects.filter(user_id=userId)
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


def isselect(request):
    goodsid = request.GET.get('goodsid')
    val = request.GET.get('val')
    good = userCenter.models.cart.objects.get(pk=goodsid)
    good.isselect = int(val)
    good.save()
    return HttpResponse('ok')


def allselect(request):
    val = request.GET.get('val')
    userCenter.models.cart.objects.all().update(isselect=int(val))
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
            #用户注册后自登陆
            user = auth.authenticate(username=info['name'], password=info['pwd'])
            auth.login(request, user)
        except Exception,e:
            pass
        else:
            isCreate = True

    return JsonResponse({'register':isCreate})


#登陆页面
def login(request):
    # print request.META['HTTP_REFERER']
    return  render(request,'userCenter/login.html')

#用户登陆
from django.contrib.auth.models import User
def toLogin(request):
    come = request.GET.get('next',None)
    username = request.POST.get('username', '')
    pwd = request.POST.get('pwd', '')
    user = auth.authenticate(username=username, password=pwd)
    isLogin = False
    if user is not None and user.is_active:
        auth.login(request,user)
        isLogin = True
    return  JsonResponse({'login':isLogin,'come':come})
#退出登陆
def logout_view(request):
    auth.logout(request)
# 可以根据需求跳转到特定页面
    return HttpResponseRedirect("/")
#用户信息
@login_required()
def userCenterInfo(request):
    #判断用户是否登陆
    if request.method == 'POST':
        return addgoods(request)
    userId = request.user.id
    puser = User.objects.get(pk=userId)
    addr = address_info.objects.filter(user=puser.pk)
    if not addr:
        addr = ['']
    recents = []
    if request.session.get('recent_goods'):
        recent_goods = request.session.get('recent_goods')
        for recent_good in recent_goods:
            recent = GoodsInfo.objects.get(id=recent_good)
            recents.append(recent)
    context = {'user':puser,'addr':addr[0], 'recents':recents[::-1]}
    return  render(request,'userCenter/user_center_info.html',context)

#用户地址
def userCenterSite(request):
    userId = request.user.id
    puser = User.objects.get(pk=userId)
    addr = address_info.objects.filter(user=puser.pk)
    if not addr:
        addr=['']
    context = {'user': puser, 'addr': addr[0]}
    return render(request,'userCenter/user_center_site.html',context)


#用户全部订单

@login_required()
def userCenterOrder(request,pIndex):
    userId=request.user.id
    #根据登陆用户id查处他的订单
    if request.GET.get('orderid'):
        orderid = request.GET.get('orderid')
        OrderInfo.objects.filter(id=orderid).update(state=1)
    orders = OrderInfo.objects.filter(user=userId)[::-1]
    #分页
    pgi = Paginator(orders,3)
    if pIndex =='':
        pIndex='1'
    orders2 = pgi.page(int(pIndex))
    pagelist = pgi.page_range
    context = {'orders':orders2,'pagelist':pagelist,'pIndex':pIndex}
    return  render(request,'userCenter/user_center_order.html',context)

#修改地址数据
def updatehandler(request):
    userId = request.user.id
    uname = request.POST['uname']
    uaddress = request.POST['address']
    uzipcode = request.POST['zipcode']
    utelp = request.POST['tel']
    # context = {'uname':uname,'address':address,'zipcode':zipcode,'tel':tel}
    #存储数据到数据库
    try :
        temp=address_info.objects.filter(id=userId)[0]
    except:
        temp = address_info()
    temp.receiver=uname
    temp.address=uaddress
    temp.tel=utelp
    temp.zipcode=uzipcode
    temp.user=request.user
    temp.save()
    return redirect('/userCenterSite/')
