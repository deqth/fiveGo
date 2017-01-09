#coding=utf-8
from django.shortcuts import render
from django.http import Http404,JsonResponse,HttpResponse
from django.contrib import auth
from django import forms
import userCenter
from shopping.models import *

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


# def test(request):
#     if  request.user.is_authenticated():
#         user = request.user
#         return HttpResponse(user.password)
#     raise Http404
