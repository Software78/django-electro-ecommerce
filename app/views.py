from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def index(request):
    items = Items.objects.filter(new_device = True)
    phones = Items.objects.filter(category__in = '1')
    context = {'items':items,'phones':phones}
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

def accessories(request):
    batteries = Items.objects.filter(category__in = '3')
    chargers = Items.objects.filter(category__in = '4')
    headphones = Items.objects.filter(category__in = '5')
    context = {'headphones':headphones,'chargers':chargers,'batteries':batteries}
    return render(request,'accessories.html',context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = False
    
    def get_success_url(self):
        return reverse_lazy('index')
