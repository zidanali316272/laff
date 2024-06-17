from typing import Any
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django import forms

attrs = {'class': 'form-control'}

class UserLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLogin,self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)    
    ) 



class UserRegister(UserCreationForm):
   
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs=attrs)
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)    
    )           
    password2 = forms.CharField(
        label='Password Confirmation',
        strip=False,
        widget=forms.PasswordInput(attrs=attrs)    
    )           

    class Meta(UserCreationForm.Meta):
        fields = ('first_name' , 'last_name' , 'username' , 'email') # زيادة عن الموجود في (UserCreationForm والمحجوزة في جانغو