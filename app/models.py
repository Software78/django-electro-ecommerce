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
    discount = models.CharField(max_length=2,blank=True,null=True)
    original_price = models.FloatField(null=True,blank=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Smart Phones'

class Laptop(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    original_price = models.FloatField(null=True,blank=True)
    discount = models.CharField(max_length=2,blank=True,null=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Headphones(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.CharField(max_length=2,blank=True,null=True)
    original_price = models.FloatField(null=True,blank=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Headphones'

class Chargers(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.CharField(max_length=2,blank=True,null=True)
    original_price = models.FloatField(null=True,blank=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Chargers'

class Batteries(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.CharField(max_length=2,blank=True,null=True)
    original_price = models.FloatField(null=True,blank=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Batteries'