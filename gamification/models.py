from django.db import models
from accounts.models import *
# Create your models here.
class Badge(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=True, null=True)
    level = models.CharField(max_length=100,default='bronze')
    progress = models.IntegerField(default=0)

    title = models.CharField(max_length=200,null=True,blank=True)
    b_type = models.CharField(max_length=200,null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)


class Coins(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    value =  models.IntegerField(default=5)
    expire_date = models.DateTimeField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)

    