from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=50)
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    password=models.CharField(max_length=15)
    blog=models.CharField(max_length=1000,null=True,blank=True)
