from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
path('',views.index,name='res.index'),
path('li/',views.client,name='res.testimonial'),
path('about/',views.about,name='res.about'),
path('booking/',views.booking,name='res.booking'),
path('menu/',views.menu,name='res.menu'),
path('service/',views.service,name='res.service'),
path('team/',views.team,name='res.team'),
path('contact/',views.contact,name='res.contact'),
path('profile/',views.profile,name='res.profile'),
path('ingredients/<int:fid>',views.ingredients,name='res.ingredients'),
path('create/',views.PCV.as_view(), name='res.reservation'),
path('complete/',views.complete,name='res.complete'),


]