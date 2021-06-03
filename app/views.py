from django.shortcuts import render
from .models import *

def index(request):
    context = {}
    return render(request,'index.html',context)

def checkout(request):
    context = {}
    return render(request,'checkout.html',context)

def product(request):
    context ={}
    return render(request,'product.html')

def blank(request):
    context = {}
    return render(request,'blank.html')

def phones(request):
    phones = Phones.objects.all()
    laptop = Laptop.objects.all()
    context = {'phones':phones,'laptop':laptop}
    return render(request,'phones.html',context)

def accessories(request):
    batteries = Batteries.objects.all()
    headphones = Headphones.objects.all()
    chargers = Chargers.objects.all()
    context ={'headphones':headphones,'chargers':chargers,'batteries':batteries}
    return render(request,'accessories.html',context)