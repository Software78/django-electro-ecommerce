from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.name


class Phones(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.CharField(max_length=3,blank=True,null=True)
    
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Laptop(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.CharField(max_length=3,blank=True,null=True)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Accessories(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.CharField(max_length=3,blank=True,null=True)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name