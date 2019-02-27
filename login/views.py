from django.shortcuts import render,redirect
from login.models import User
from login.forms import UserForm,RegisterForm
import hashlib

# Create your views here.

def hash_code(s,salt='controldown'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            try:
                user = User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确!"
            except:
                message = "用户名不存在!"
        return render(request,'login/login.html',locals())
    login_form = UserForm()
    return render(request, 'login/login.html',locals())


def register(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = '请检查输入的内容'
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = "两次输入的密码不正确！"
                return render(request,'login/register.html',locals())
            else:
                same_name = User.objects.filter(name=username)
                if same_name:
                    message = "用户名已经被注册，请重新输入！"
                    return render(request,'login/register.html',locals())
                same_email = User.objects.filter(email=email)
                if same_email:
                    message = "邮箱已经被注册，请重新输入！"
                    return render(request,'login/register.html',locals())
                User.objects.create(name=username,password=hash_code(password1),email=email,sex=sex)
                return redirect('/login/')
        return render(request, 'login/register.html', locals())
    register_form = RegisterForm()
    return render(request, 'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()
    return redirect("/index/")