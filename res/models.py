from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CategoryMenu(models.Model):
    name = models.CharField( max_length=255, unique=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True ,null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


    def __str__(self):
        return self.name

class Clients(models.Model):
   name = models.CharField(max_length=100)
   profession = models.CharField(max_length=100)
   image = models.ImageField(upload_to='static/img' , null=True , blank=True )
   created_at = models.DateTimeField(auto_now_add=True , null=True)
   updated_at = models.DateTimeField(auto_now=True, null=True)
   say = models.TextField()    
   
   

   def __str__(self):
        return self.name

class Foods(models.Model):
    name = models.CharField(max_length=255, unique=True)
    featured = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    ingredient = models.TextField(null=True)
    categorymenu = models.ForeignKey(CategoryMenu,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Reser(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=100,null=True)
 email = models.EmailField(null=True)
 created_at = models.DateTimeField(auto_now_add=True , null=True)
 updated_at = models.DateTimeField(auto_now=True, null=True)
 datetime = models.CharField(max_length=100 ,null=True)
 number = models.IntegerField(null=True)
 s_r = models.TextField(null=True)


 def __str__(self):
        return self.name

    
    

   
   

