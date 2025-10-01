from django.urls import path
from . import views

urlpatterns = [
    path('donateform/', views.donationform, name='donateform'),
    path('receive/food/', views.foodreceive, name='foodreceive'),
    path('receive/clothes/', views.clothsreceive, name='clothsreceive'),
    path('receive/furniture/', views.furniturereceive, name='furniturereceive'),
]
