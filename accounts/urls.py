from django.contrib import admin
from .views import RigsterView
from django.urls import path,include
from django.contrib.auth.views import LoginView
from .forms import UserLogin , UserRegister

urlpatterns = [
path('login/',LoginView.as_view(authentication_form=UserLogin), name='login'),    
path('register/',RigsterView.as_view(), name='register'),
path('',include('django.contrib.auth.urls')),
]