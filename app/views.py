from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


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
    phones = Items.objects.filter(category__in = '1')
    laptops = Items.objects.filter(category__in = '2')
    context = {'phones':phones,'laptops':laptops}
    return render(request,'phones.html',context)

class ProductDetail(DetailView):
    model = Items
    context_object_name = 'product'
    template_name = 'product.html'
