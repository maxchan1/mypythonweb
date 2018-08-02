from django.shortcuts import render
from django.shortcuts import HttpResponse
from comdb.models import userinfo

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
    return render(request,"index.html")

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
