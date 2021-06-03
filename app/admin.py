from django.contrib import admin
from .models import *

admin.site.register([
    Phones,Laptop,Headphones,Chargers,Batteries
])