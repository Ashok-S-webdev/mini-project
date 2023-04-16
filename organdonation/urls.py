from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dregister/', views.dregister, name='dregister'),
    path('rregister/', views.rregister, name='rregister'),
    path('login/', views.userlogin, name='login'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('home/', views.home, name='home'),
]