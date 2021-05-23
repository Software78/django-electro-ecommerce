from django.urls import path
from .views import NewsList,NewsDetail,NewsCreate,NewsUpdate,AuthNewsDetail,NewsDelete,CustomLoginView,RegisterView,AuthNewsList
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',NewsList.as_view(),name='index'),
    path('news/<int:pk>/',NewsDetail.as_view(),name='detail'),
    path('create/',NewsCreate.as_view(),name='create'),
    path('update/<int:pk>/',NewsUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',NewsDelete.as_view(),name='delete'),
    path('accounts/login/',CustomLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='index'),name='logout'),
    path('register/',RegisterView.as_view(),name='register'),
    path('authindex',AuthNewsList.as_view(),name='authindex'),
    path('authnews/<int:pk>/',AuthNewsDetail.as_view(),name='authnews'),
]