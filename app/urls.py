from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',index,name='index'),
    path('checkout/',checkout,name='checkout'),
    path('blank/',blank,name='blank'),
    path('phones/',phones,name='phones'),
    path('accessories/',accessories,name='accessories'),
    path('detail/<int:pk>',ProductDetail.as_view(),name='detail'),
    path('accounts/login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'index'),name='logout'),
    path('accounts/register/',register,name='register'),
    path('profile/',login_required(user),name='profile'),
]