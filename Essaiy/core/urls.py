from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('myEssays', views.myEssays, name='myEssays'),
    path('sendEssays', views.sendEssays, name='sendEssays'),
    path('about', views.about, name='about'),
]