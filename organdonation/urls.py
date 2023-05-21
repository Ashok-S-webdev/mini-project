from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dregister/', views.dregister, name='dregister'),
    path('rregister/', views.rregister, name='rregister'),
    path('login/', views.userlogin, name='login'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('donor/home/', views.donorhome, name='donorhome'),
    path('recipient/profile/', views.recipientprofileview, name='recipientprofile'),
    path('recipient/home/', views.recipientdonorsearch, name='recipientdonorsearch'),
]