#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.contrib import auth
from django import forms


class ttsxUser(forms.Form):
    name = forms.CharField(max_length=20,min_length=3)
    pwd = forms.CharField(max_length=20,min_length=6)
    email = forms.EmailField(max_length=30,min_length=3)

def register_split(request,get,post):

    if request.method == 'GET':
        return get(request)
    elif request.method == 'POST':
        return post(request)
    else:
        raise Http404

def register(request):
    return render(request,'userCenter/register.html')

def createUser(request):
    form = ttsxUser(request.POST)
    isCreate = False
    if form.is_valid():
        info = form.cleaned_data
        try:
            user = User.objects.create_user(username=info['name'],password=info['pwd'],email=info['email'])
            user.save()
        except Exception,e:
            pass
        else:
            isCreate = True
    return JsonResponse({'register':isCreate})

def login_split(request,get,post):
    if request.method == 'GET':
        return get(request)
    elif request.method == 'POST':
        return post(request)
    else:
        raise Http404

def login(request):
    return  render(request,'userCenter/login.html')
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

# def test(request):
#     if  request.user.is_authenticated():
#         user = request.user
#         return HttpResponse(user.password)
#     raise Http404