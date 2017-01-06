from django.shortcuts import render
from models import *

def index(request):
    return render(request,'shopping/index.html')
def detail(request):
    goods_info = GoodsInfo.objects.get(pk=3)
    context = {'goods_info':goods_info}
    return render(request,'shopping/detail.html',context)
