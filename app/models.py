from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Items(models.Model):

    class types(models.IntegerChoices):
        phones = 1
        laptops = 2
        batteries = 3
        chargers = 4
        headphones = 5

    name = models.CharField(max_length=50)
    category = models.IntegerField(choices=types.choices,default=1)
    price = models.PositiveIntegerField()
    discount = models.IntegerField(blank=True,null=True)
    original_price = models.FloatField(null=True,blank=True)
    new_device = models.BooleanField(default=False)
    #image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'
