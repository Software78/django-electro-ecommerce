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
    product = Phones.objects.all()
    context = {'product':product}
    return render(request,'phones.html',context)