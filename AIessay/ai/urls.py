from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('feedModel', views.feedModel, name='feedModel'),
    path('addThemes', views.addThemes, name='addThemes'),
    path('checkEssays', views.checkEssays, name='checkEssays'),
]