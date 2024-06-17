from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegister
class RigsterView(CreateView):
    form_class = UserRegister
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'