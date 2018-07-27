from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    if request.method == "post":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
    return render(request,"index.html")