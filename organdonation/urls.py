from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dregister/', views.dregister, name='dregister'),
    path('rregister/', views.rregister, name='rregister'),
    path('dlogin/', views.dlogin, name='dlogin'),
    path('rlogin/', views.rlogin, name='rlogin'),
    path('dlogout/', views.dlogout, name='dlogout'),
    path('rlogout/', views.rlogout, name='rlogout'),
    path('donor_home/', views.donor_home, name='donor_home'),
    path('recipient_home/', views.recipient_home, name='recipient_home'),
]