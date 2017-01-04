from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.models import User
def register(request):
    return render(request,'userCenter/register.html')

def createUser(request):
    user = User.objects.create_user(username=request.POST['name'],password=request.POST['pwd'],email=request.POST['email'])
    user.save()
    return HttpResponseRedirect('userCenter/login.html')


