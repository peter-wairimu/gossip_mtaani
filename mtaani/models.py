from django.db import models
from django.contrib.auth.models import User





# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='profile_pics')
    


class NeighbourHood(models.Model):
     Name = models.CharField(max_length=255)
     location = models.CharField(max_length=255)
     Count = models.IntegerField()
     profile= models.ImageField(blank=True, null=True)
     author = models.ForeignKey(User,on_delete=models.CASCADE)
     image = models.ImageField(blank=True,null=True)

     def __str__(self):
         return self.Name

    
