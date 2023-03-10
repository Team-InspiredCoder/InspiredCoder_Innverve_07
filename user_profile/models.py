from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Experience(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=100,null=True,blank=True)
    position = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


class Skills(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


class Education(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    school_name = models.CharField(max_length=100,null=True,blank=True)
    percentage = models.CharField(max_length=100,null=True,blank=True)
    pass_out_year = models.CharField(max_length=100,null=True,blank=True)

    