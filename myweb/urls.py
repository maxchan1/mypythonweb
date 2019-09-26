"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from login import views
from django.conf.urls import url

urlpatterns = [
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('comdb/',include("comdb.urls",namespace='adminpull')),
    path('comdb2/',include('comdb.urls',namespace="normaluser")),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    re_path(r'^captcha/',include('captcha.urls')),
    re_path(r'^confirm/$',views.user_confirm),
    path('moc/',include(("moc.urls"))),
    #re_path("",views.index),
    #re_path(r'.*', views.index),
]
