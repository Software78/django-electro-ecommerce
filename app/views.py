from django.shortcuts import render

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