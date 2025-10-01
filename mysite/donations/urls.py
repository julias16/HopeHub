# donations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('donate/', views.donationform, name='donationform'),
    path('receive/food/', views.foodreceive, name='foodreceive'),
    path('receive/clothes/', views.clothesreceive, name='clothesreceive'),
    path('receive/furniture/', views.furniturereceive, name='furniturereceive'),
]
