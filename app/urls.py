from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('checkout/',checkout,name='checkout'),
    path('product/',product,name='product'),
    path('blank/',blank,name='blank'),
]
