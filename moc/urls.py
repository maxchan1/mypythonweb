from django.urls import path,re_path
from . import views

app_name = 'moc'

urlpatterns = [
    re_path(r'^main/$', views.mainmoc),
]