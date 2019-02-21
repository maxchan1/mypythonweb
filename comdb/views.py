from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from comdb.models import userinfo
from django.contrib.auth import authenticate,login
from django.views import generic
from .models import userinfo

# Create your views here.

def index(request):
    return render(request,"index.html")

def mylogin(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"post.html")
        else:
            return render(request,"index.html",{"loginfo":"用户名或密码错误"})

def testdb(request):
    '''test1 = userinfo(name="mike",email="43533@163.com",addr="下胡同城北村")
    test1.save()'''

    lt = userinfo.objects.filter(id=1).update(name="francesico")
    print(lt)
    return HttpResponse("<p>数据库修改成功!</p>")

def searchtext(request):
    message = ""
    if request.method == "POST":
        message = request.POST.get("findtext",None)
    print("message is " + message)
    return render(request,"post.html",{"result":message})

def joke(request,page_id):
    return HttpResponse("the page num is %s"%page_id)

class DetailView(generic.DetailView):
    model = userinfo
    template_name = 'comdb/listenup.html'

def hell(request):
    return render(request,"comdb/fix.html")