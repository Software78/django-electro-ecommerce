from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.name


class Items(models.Model):

    class types(models.IntegerChoices):
        phones = 1
        laptops = 2
        batteries = 3
        chargers = 4

    name = models.CharField(max_length=50)
    category = models.IntegerField(choices=types.choices,default=1)
    price = models.FloatField()
    discount = models.IntegerField(blank=True,null=True)
    original_price = models.FloatField(null=True,blank=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'
