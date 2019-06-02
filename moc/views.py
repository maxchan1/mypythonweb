from django.shortcuts import render

# Create your views here.

def mainmoc(request):
    return render(request,"moc/main.html")
