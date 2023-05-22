from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dregister/', views.dregister, name='dregister'),
    path('rregister/', views.rregister, name='rregister'),
    path('login/', views.userlogin, name='login'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('donor/home/', views.donorhome, name='donorhome'),
    path('donor/requests/', views.donorrequest, name='donorrequest'),
    path('donor/request/<int:recipient_id>/', views.donoracceptrequest, name='donoracceptrequest'),
    path('recipient/profile/', views.recipientprofileview, name='recipientprofile'),
    path('recipient/donors/', views.recipientdonorsearch, name='recipientdonorsearch'),
    path('recipient/send_request<int:donor_id>/', views.recipientsendrequest, name='recipientsendrequest'),
    path('recipient/requests/', views.recipientrequest, name='recipientrequest'),
]