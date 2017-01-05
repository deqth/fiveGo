from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
def register(request):
    return render(request,'userCenter/register.html')


def cart(request):
    return render(request,'userCenter/cart.html')
