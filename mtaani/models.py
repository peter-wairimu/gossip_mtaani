from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')
    

class User(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email =models.CharField(max_length=200,null=True)
    profile= models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name






class NeighbourHood(models.Model):
     Name = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     Count = models.IntegerField()
     author = models.ForeignKey(User,on_delete=models.CASCADE)
     image = models.ImageField(blank=True,null=True)

     def __str__(self):
         return self.Name


class Business(models.Model):
    businessname = models.ForeignKey(NeighbourHood,null=True,on_delete=models.CASCADE)
    bssEmail = models.CharField(max_length=200,null=True)
    


        
