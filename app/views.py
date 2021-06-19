from django.shortcuts import render,redirect
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, redirect_to_login
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegisterForm

def index(request):
    items = Items.objects.filter(new_device = True)
    phones = Items.objects.filter(category__in = '1')
    context = {'items':items,'phones':phones}
    return render(request,'index.html',context)

def checkout(request):
    context = {}
    return render(request,'checkout.html',context)

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

def register(request):
        if request.method == 'GET':
            form  = RegisterForm()
            context = {'form': form}
            return render(request, 'register.html', context)
        if request.method == 'POST':
            form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

def user(request):
    context = {}
    return render(request,'profile.html',context)