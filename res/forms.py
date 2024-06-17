from django import forms
from . import models
from django.core.exceptions import ValidationError
import re


class CreateReser(forms.ModelForm):
    class Meta:
        model= models.Reser
        fields=['name' , 'email' , 'datetime' , 'number' , 's_r' ]
        
    
class Client(forms.ModelForm):
    class Meta:
        model= models.Clients
        fields='__all__'    

        
    def clean_name(self):
         name = self.cleaned_data.get('name')
         
         if len(name) < 3 or len(name) >10  or not re.match("^[a-zA-Z\ء-ي)]+$", name):  # تحقق من أن الاسم يحتوي على حرفين على الأقل
            raise forms.ValidationError("الاسم يجب أن يحتوي على 3 احرف على الأقل")
         return name
        
    def clean_say(self):
         say = self.cleaned_data.get('say')
         if len(say) < 15 or len(say) > 100 or not re.match("^[a-zA-Z\ء-ي)]+$",say):  
            raise forms.ValidationError("التعليق يجب أن يحتوي على 30 حرف على الأقل")
         return say
    
    def clean_profession(self):
        profession = self.cleaned_data.get('profession')
         
        if len(profession) < 3  or  len(profession) >10 or not re.match("^[a-zA-Z\ء-ي)]+$", profession):# تحقق من أن الاسم يحتوي على حرفين على الأقل
            raise forms.ValidationError("المهنة يجب أن تحتوي على 3 احرف على الأقل")
        return profession
    


    
    
                    
   
        