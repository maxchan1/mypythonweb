from django.urls import path

from . import views

app_name='comdb'
urlpatterns = [
    # ex: /polls/
    path('index/', views.index),
    path('login/', views.mylogin),
    path('testdb/', views.testdb),
    path('search/', views.searchtext),
    path('<page_id>/joke/',views.joke,name='joking'),
    path("listen/<int:pk>/",views.DetailView.as_view()),
    path('hell/', views.hell, name='index'),
]