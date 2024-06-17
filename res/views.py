from django.shortcuts import render,redirect,get_object_or_404
from .models import Foods,CategoryMenu,Clients,Reser,User
from django.views.generic import ListView,CreateView
from . import forms
from . import models
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse
from django.views.generic.edit import ModelFormMixin
from .forms import Client , CreateReser 
from accounts.forms import UserRegister
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import time

def index(request):
    foods = Foods.objects.filter(featured=True)
    return render(request, 'index.html',
                  {
                      'foods' : foods
                  }
                  
                  
                  )



def ingredients(request,fid):
    
    food=Foods.objects.get(pk=fid)
    
    return render(request, 'food_details.html',{
      'food':food,
    })
                  

def profile(request):

    p = request.user
   
   

    return render(request, 'profile.html',{
        'p':p,
        

    })


def about(request):

    return render(request, 'about.html')

def booking(request):

    tes =Reser.objects.filter(user_id=request.user.id)

    return render(request, 'booking.html',{
                  
                  'tes':tes
    }
                  )

def contact(request):

    return render(request, 'contact.html')

def menu(request):
    
   sand= Foods.objects.filter(categorymenu=1)
   drn= Foods.objects.filter(categorymenu=2)
   mel= Foods.objects.filter(categorymenu=3)
   return render(request, 'menu.html',{
       
    'sand': sand,
    'drn':drn,
    'mel':mel,
   

   })

def food_cards(request):
    
 foods = Foods.objects.select_related('categorymenu').all()

 return render(request, 'food_cards.html',{
       
     'foods':foods       


   })
     
    
def team(request):

    return render(request, 'team.html')

def complete(request):

    return render(request, 'complete.html')


def service(request):

    return render(request, 'service.html')

class PCV(LoginRequiredMixin, CreateView):
      model = models.Reser
      form_class = forms.CreateReser
      template_name= 'reservation.html'
      success_url = reverse_lazy('res.index')
      
      def form_valid(self, form):                                    #يطلع الحجز الخاص بالمستخدم
        form.instance.user = self.request.user
        return super().form_valid(form) 
      
       


    
    
def client(request):
    c = Clients.objects.all()
   
    form = Client()

    if request.method == 'POST':
        form = Client(request.POST)
        if form.is_valid():
            form.save()
            return redirect('res.testimonial')  # يمكنك تغيير 'success' إلى اسم الصفحة التي ترغب في توجيه المستخدم إليها بعد إضافة العميل
    

    return render(request, 'testimonial.html', {
        
        'form': form,
        'c':c
        })

      
      
      
     

     
        
    
      
      
        

      
      
 
 
