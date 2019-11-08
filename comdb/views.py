from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from comdb.models import userinfo
from django.contrib.auth import authenticate,login
from django.views import generic
from .models import userinfo,FileForm,Comment
from django.urls import reverse
from .forms import uploadfileform
import csv
from django.http import StreamingHttpResponse
from django.template import loader,Context

# Create your views here.
'''def cmtview(request):
    if request.is_ajax():
        content = request.POST.get('content',None)
        if content:'''
#https://www.cnblogs.com/yb635238477/p/9508458.html
def comment(request):
    res = {'code':1}
    if request.method == 'POST':
        res = {'code':0}
        title = request.POST.get('title')
        content = request.POST.get('content')
        comment_obj = Comment.objects.create(title=title, content=content)
        res['data'] = {'title':comment_obj.title,
                       'content':comment_obj.content,
                       'ctime':comment_obj.ctime.strftime('%Y-%m-%d %H:%M')}
    return JsonResponse(res,safe=False)


class Echo(object):
    def write(self, value):
        return value
def index(request):
    '''rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # The data is hard-coded here, but you could load it from a database or
    # some other source.
    csv_data = (
        ('First row', 'Foo', 'Bar', 'Baz'),
        ('Second row', 'A', 'B', '"Testing"', "Here's a quote"),
    )

    t = loader.get_template('comdb/my_template_name.txt')
    c = {
        'data': csv_data
    }
    response.write(t.render(c))
    return response'''
    if request.method == 'POST':
        mdform = FileForm(request.POST,request.FILES)
        if mdform.is_valid():
            mdform.save()
            return render(request,'indexnew.html',locals())
    else:
        lform = uploadfileform()
        mdform = FileForm()
        comment_list = Comment.objects.all()
    return render(request, "indexnew.html",locals())

def mylogin(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"post.html")
        else:
            return render(request, "indexnew.html", {"loginfo": "用户名或密码错误"})

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