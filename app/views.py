from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .models import NewsItem
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsList(ListView):
    model = NewsItem
    context_object_name = 'newslist'
    template_name = 'index.html'

class NewsDetail(DetailView):
    model = NewsItem
    template_name = 'detail.html'
    context_object_name = 'newsdetail'

class NewsCreate(LoginRequiredMixin,CreateView):
    model = NewsItem
    fields = '__all__'
    success_url = reverse_lazy('authindex')
    template_name = 'newsform.html'

class NewsUpdate(LoginRequiredMixin,UpdateView):
    model = NewsItem
    fields = '__all__'
    success_url = reverse_lazy('authindex')
    template_name = 'newsform.html'
    context_object_name = 'newsupdate'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewsUpdate, self).form_valid(form)

class NewsDelete(LoginRequiredMixin,DeleteView):
    model = NewsItem
    fields = '__all__'
    success_url = reverse_lazy('index')
    template_name = 'deletenews.html'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('authindex')
        return super(RegisterView, self).get(*args, **kwargs)

class AuthNewsList(LoginRequiredMixin,ListView):
    model = NewsItem
    context_object_name = 'auth_news_list'
    template_name = 'authindex.html' 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['auth_news_list'] = context['auth_news_list'].filter(author = self.request.user)
        return context

class AuthNewsDetail(LoginRequiredMixin,DetailView):
    model = NewsItem
    template_name = 'authdetail.html'
    context_object_name = 'authdetail'
