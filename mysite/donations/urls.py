from django.urls import path
from . import views

urlpatterns = [
    path('donateform/', views.donationform, name='donateform'),
    path('receive/food/', views.foodreceive, name='foodreceive'),
    path('receive/clothes/', views.clothsreceive, name='clothsreceive'),
    path('receive/furniture/', views.furniturereceive, name='furniturereceive'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/<int:item_id>/send_message/', views.send_message, name='send_message'),
]
