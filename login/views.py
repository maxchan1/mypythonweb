from django.shortcuts import render,redirect,HttpResponse
from . import models
from login.forms import UserForm,RegisterForm
import hashlib,datetime,json
from django.conf import  settings
from captcha.models import CaptchaStore
from captcha.helpers import  captcha_image_url
# Create your views here.

def hash_code(s,salt='controldown'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    pass
    return render(request, 'login/index.html')

def captcha():
    hashkey = CaptchaStore.generate_key()   #验证码答案
    image_url = captcha_image_url(hashkey)  #验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha

def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')

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
                user = models.User.objects.get(name=username)
                if not user.has_confirmed:
                    message = '该用户邮件还没有确认！'
                    return render(request,'login/login.html',locals())
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
                same_name = models.User.objects.filter(name=username)
                if same_name:
                    message = "用户名已经被注册，请重新输入！"
                    return render(request,'login/register.html',locals())
                same_email = models.User.objects.filter(email=email)
                if same_email:
                    message = "邮箱已经被注册，请重新输入！"
                    return render(request,'login/register.html',locals())
                new_user = models.User.objects.create(name=username,password=hash_code(password1),email=email,sex=sex)
                code = make_confirm_string(new_user)
                send_mail(email, code)
                return redirect('login/')
        return render(request, 'login/register.html', locals())
    register_form = RegisterForm()
    return render(request, 'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/index/')
    request.session.flush()
    return redirect("/index/")

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name,now)
    models.ConfirmString.objects.create(code=code,user=user)
    return code

def send_mail(email,code):
    from django.core.mail import EmailMultiAlternatives

    subject = '注册确认邮件'

    text_content = '''感谢注册，如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''<p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.myweb.com</a></p>
                        <p>请点击站点链接完成注册确认！</p>
                        <p>此链接有效期为{}天！</p>
                        '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def user_confirm(request):
    code = request.GET.get('code',None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求'
        return render(request,'login/confirm.html',locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期，请重新注册！'
        return render(request,'login/confirm.html',locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，欢迎使用账户登录！'
        return render(request,'login/confirm.html',locals())