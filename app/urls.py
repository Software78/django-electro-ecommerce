from django.urls import path
from .views import *



urlpatterns = [
    path('',index,name='index'),
    path('checkout/',checkout,name='checkout'),
    path('blank/',blank,name='blank'),
    path('phones/',phones,name='phones'),
    ]
